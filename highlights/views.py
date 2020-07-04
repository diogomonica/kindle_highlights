import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.dispatch import receiver
from inbound_email.signals import email_received, email_received_unacceptable
from django.core.mail import EmailMessage, EmailMultiAlternatives
from .models import Email

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

@receiver(email_received, dispatch_uid="something_unique")
def on_email_received(sender, **kwargs):
    """Handle inbound emails."""
    email = kwargs.pop('email')
    request = kwargs.pop('request')

    Email.objects.create(sender_email=email.from_email, subject=email.subject, body=email.body)
    # your code goes here - save the email, respond to it, etc.
    logging.info(
        "New email received from %s: %s",
        email.from_email,
        email.subject
    )
    logging.debug(to_dict(email))

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

# pass dispatch_uid to prevent duplicates:
# https://docs.djangoproject.com/en/dev/topics/signals/
# email_received.connect(on_email_received, dispatch_uid="something_unique")

def index(request):
    return HttpResponse("INDEX VIEW")

