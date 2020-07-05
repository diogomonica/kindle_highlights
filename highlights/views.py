import logging
import requests
import json
import re

from django.http import HttpResponse
from django.core.exceptions import SuspiciousOperation
from django.shortcuts import render
from django.dispatch import receiver
from inbound_email.signals import email_received, email_received_unacceptable
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.contrib.auth.models import User
from .models import Email, Volume, Highlight, Entry
from bs4 import BeautifulSoup


__BASEURL = 'https://www.googleapis.com/books/v1'

def _get(path, params=None):
    if params is None:
        params = {}
    params["key"] = "AIzaSyBKgWOv1eA0w73f-VQm0D-deUptP4dvCh4"
    resp = requests.get(__BASEURL+path, params=params)
    if resp.status_code == 200:
        return json.loads(resp.content)

    return resp

def to_dict(email_message):
    """
    Converts the specified email message to a dictionary representation.
    """
    if type(email_message) not in [EmailMessage, EmailMultiAlternatives]:
        return email_message
    email_message_data = {
        'subject': email_message.subject,
        'body': email_message.body,
        'from_email': email_message.from_email,
        'to': email_message.to,
        'bcc': email_message.bcc,
        'attachments': email_message.attachments,
        'headers': email_message.extra_headers,
        'cc': email_message.cc,
        'reply_to': None,
    }
    if isinstance(email_message, EmailMultiAlternatives):
        email_message_data['alternatives'] = email_message.alternatives
    return email_message_data 

def find_or_create_user(email):
    try:
        user = User.objects.get(username=email)
    except User.DoesNotExist:
        # Create a new user. There's no need to set a password
        # because we're going to login via links.
        user = User.objects.create_user(username=email)
    return user

def create_entry(user, volume, content):
    # Attempt to retrieve highlights for this user/volume pair
    entry = Entry.objects.filter(user__id=user.id).filter(volume__id=volume.id)
    # If there are no highlights for this user/volume pair, process the content
    if not entry:
        entry = Entry(user=user, volume=volume)
        entry.save()

        parsed_content = BeautifulSoup(content, "html.parser")
        title = parsed_content.find_all(attrs={"class": "bookTitle"})[0].string.strip()

        highlights = []
        headings = parsed_content.find_all('div', 'noteHeading')

        for heading in headings:
            span = heading.find('span')
            color = heading.find('span').string if span != None else 'blue'

            location = re.findall("location\s(\d*)", str(heading), re.I)
            if len(location) > 0:
                location = location[0]

            content = heading.next_sibling.next_sibling.string.strip()
            highlight_type = 'note' if re.search('Note\s-', str(heading)) else 'highlight'
            highlight = Highlight(user=user, volume=volume, entry=entry, color=color, location=location, highlight_type=highlight_type, content=content)
            highlight.save()

def find_or_create_volume(content):
    parsed_content = BeautifulSoup(content, "html.parser")
    book_title_attrs = parsed_content.find_all(attrs={"class": "bookTitle"})
    if len(book_title_attrs) == 0:
        raise SuspiciousOperation('No book title found on attached highlights')
    book_title = book_title_attrs[0].string.strip()

    logging.info("Attemping to find a book with title: %s" % book_title)
    google_books_reply = find_from_google_books(book_title)

    total_items = google_books_reply['totalItems']
    if total_items != None and int(total_items) > 0:
        google_id = google_books_reply['items'][0]['id']
        try:
            volume = Volume.objects.get(google_id=google_id)
            logging.info("Found volume with ID: %s" % google_id)
        except Volume.DoesNotExist:
            params = dict()
            params['google_id'] = google_id
            params['title'] = google_books_reply['items'][0]['volumeInfo'].get('title',"")
            params['subtitle'] = google_books_reply['items'][0]['volumeInfo'].get('subtitle',"")
            params['description'] = google_books_reply['items'][0]['volumeInfo'].get('description',"")
            params['published_date'] = google_books_reply['items'][0]['volumeInfo'].get('publishedDate')
            params['publisher'] = google_books_reply['items'][0]['volumeInfo'].get('publisher',"Unkown Publisher")
            params['page_count'] = google_books_reply['items'][0]['volumeInfo'].get('pageCount',"0")

            volume = Volume.objects.create(**params)
            logging.info("Created new volume with ID: %s" % google_id)

    return volume

def find_from_google_books(book_title):
    path = '/volumes'
    params = dict()
    params['q'] = "intitle:"+book_title
    params['maxResults'] = 1
    google_books_reply = _get(path,params)
    return google_books_reply

@receiver(email_received, dispatch_uid="something_unique")
def on_email_received(sender, **kwargs):
    """Handle inbound emails."""
    email = kwargs.pop('email')
    request = kwargs.pop('request')

    logging.debug("Parsing new email: %s with %s attachments." % (email.subject, len(email.attachments)))
    if len(email.attachments) == 0:
        raise SuspiciousOperation('Email has no attached highlights')

    # Save the entry in the database and store it for future parsing
    new_email = Email(sender_email=email.from_email, subject=email.subject, body=email.body)
    for attach in email.attachments:
        # we must convert attachment tuple into a file
        # before adding as the property.
        name, content, content_type = attach
        logging.info("Found attachment. Name: %s, Content-type:%s. Content: %s bytes" % (name, content_type, len(content)))
        if content_type == "text/html":
            logging.info("Added Attachment  %s" % name)
            new_email.attachment = content

    new_email.save()

    logging.info(
        "New email received from %s: %s with %s attachments.",
        email.from_email,
        email.subject,
        len(email.attachments)
    )

    # Use the sender email to retrieve or create a new User
    user = find_or_create_user(new_email.sender_email)

    # Use the bookTitle in the HTML attachment to retrieve from Books API
    # the canonical ID, and either return a database object or create a new one
    volume = find_or_create_volume(new_email.attachment)

    # Parse the HTML to retrieve color, location, content for each highlight
    create_entry(user, volume, new_email.attachment)


@receiver(email_received_unacceptable, dispatch_uid="something_unique_1")
def on_invalid_email_received(sender, **kwargs):
    """Handle invalid emails."""
    email = kwargs.pop('email')
    request = kwargs.pop('request')

    # your code goes here - save the email, respond to it, etc.
    if email is None:
        message = "New invalid email received with empty email"
    else:
        message =  "New invalid email received from %s: %s", email.from_email, email.subject
    logging.warning(message)

def index(request):
    entries = Entry.objects.order_by('-created_at')[:10]
    context = {'entries_list': entries}

    return render(request, 'highlights/index.html', context)

