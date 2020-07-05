import unittest
import logging
from os import path
import copy

from django.test import TestCase, Client
from django.urls import reverse
from django.core.mail import EmailMultiAlternatives
from .test_files.mailgun_post import spirit_animals_payload as mailgun_payload
from highlights.models import Email, Volume, Highlight, Entry
from django.contrib.auth.models import User

from django.utils.encoding import smart_bytes

class IndexTest(TestCase):
    fixtures = ["emails.json", "entries.json", "highlights.json", "users.json", "volumes.json"]

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_entries(self):
        # Issue a GET request.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['entries']), 5)
        # self.assertEqual(response.content ,b'INDEX VIEW')

class EmailTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def _assertEmailParsedCorrectly(self, email, data):
        """Helper assert method that matches email properties to posted data.
        It's pulled out here as this is used in most of the tests to assert that
        the parser worked properly.
        Args:
            email: the EmailMultiAlternatives object to test.
            data: a dict of data that was sent to the parser.
        """
        self.assertIsInstance(email, EmailMultiAlternatives)
        self.assertEqual(email.to, data.get('recipient', '').split(','))
        self.assertEqual(email.from_email, data.get('sender', ''))
        self.assertEqual(email.subject, data.get('subject', ''))
        self.assertEqual(email.body, "%s\n\n%s" % (
            data.get('stripped-text', ''),
            data.get('stripped-signature', '')
        ))
        self.assertEqual(email.cc, data.get('cc', '').split(','))
        self.assertEqual(email.bcc, data.get('bcc', '').split(','))
        if 'html' in data:
            self.assertEqual(len(email.alternatives), 1)
            self.assertEqual(email.alternatives[0][0], data.get('stripped-html', ''))

    def test_email_with_attachment_gets_created(self):
        data = copy.deepcopy(mailgun_payload)
        file_path = path.join(path.dirname(__file__), 'test_files/animal_spirits.html')
        attachment_1 = open(file_path, 'r').read()
        data['attachment-1'] = open(file_path, 'r')

        response = self.client.post(reverse('receive_inbound_email'), data)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check to see if an email was indeed created
        emails = Email.objects.all()

        self.assertEqual(emails.count(), 1)
        self.assertEqual(emails.first().subject, data.get('subject'))
        self.assertEqual(emails.first().body, "%s\n\n%s" % (
            data.get('stripped-text', ''),
            data.get('stripped-signature', '')
        ))
        self.assertEqual(emails.first().sender_email, data.get('sender'))
        self.assertEqual(smart_bytes(emails.first().attachment), smart_bytes(attachment_1))

        # Check to see if a Volume was created
        volumes = Volume.objects.all()
        self.assertEqual(volumes.count(), 1)

        # Check to see if Highlights were created
        highlights = Highlight.objects.all()
        self.assertEqual(highlights.count(), 8)

        # Check to see if Highlights were created
        entries = Entry.objects.all()
        self.assertEqual(entries.count(), 1)

    def test_email_with_no_attachment_fails(self):
        data = copy.deepcopy(mailgun_payload)
        del data['attachment-count']
        del data['content-id-map']

        response = self.client.post(reverse('receive_inbound_email'), data)

        # Check that the response is 400 (no attachment).
        self.assertEqual(response.status_code, 400)

    def test_email_with_two_attachments_gets_created(self):
        data = copy.deepcopy(mailgun_payload)
        file_path_1 = path.join(path.dirname(__file__), 'test_files/animal_spirits.html')
        file_path_2 = path.join(path.dirname(__file__), 'test_files/innovation.html')

        attachment_1 = open(file_path_1, 'r').read()
        attachment_2 = open(file_path_2, 'r').read()

        data['attachment-1'] = open(file_path_1, 'r')
        data['attachment-2'] = open(file_path_2, 'r')


        response = self.client.post(reverse('receive_inbound_email'), data)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check to see if an email was indeed created
        emails = Email.objects.all()

        self.assertEqual(emails.count(), 1)
        self.assertEqual(emails.first().subject, data.get('subject'))
        self.assertEqual(emails.first().body, "%s\n\n%s" % (
            data.get('stripped-text', ''),
            data.get('stripped-signature', '')
        ))
        self.assertEqual(emails.first().sender_email, data.get('sender'))
        # The last valid attachment is the one we keep
        self.assertEqual(smart_bytes(emails.first().attachment), smart_bytes(attachment_2))

        # Check to see if a Volume was created
        volumes = Volume.objects.all()
        self.assertEqual(volumes.count(), 1)

        # Check to see if Highlights were created
        highlights = Highlight.objects.all()
        self.assertEqual(highlights.count(), 10)

        # Check to see if Highlights were created
        entries = Entry.objects.all()
        self.assertEqual(entries.count(), 1)

    def test_two_emails_same_sender_gets_created(self):
        data1 = copy.deepcopy(mailgun_payload)
        file_path_1 = path.join(path.dirname(__file__), 'test_files/animal_spirits.html')
        attachment_1 = open(file_path_1, 'r').read()
        data1['attachment-1'] = open(file_path_1, 'r')

        data2 = copy.deepcopy(mailgun_payload)
        file_path_2 = path.join(path.dirname(__file__), 'test_files/innovation.html')
        attachment_2 = open(file_path_2, 'r').read()
        data2['attachment-1'] = open(file_path_2, 'r')

        # Send first email
        response = self.client.post(reverse('receive_inbound_email'), data1)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Send second email
        response = self.client.post(reverse('receive_inbound_email'), data2)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check to see if an email was indeed created
        emails = Email.objects.all()

        self.assertEqual(emails.count(), 2)

        # Check to see if a Volume was created
        volumes = Volume.objects.all()
        self.assertEqual(volumes.count(), 2)

        # Check to see if Highlights were created
        highlights = Highlight.objects.all()
        self.assertEqual(highlights.count(), 18)

        # Check to see if Highlights were created
        entries = Entry.objects.all()
        self.assertEqual(entries.count(), 2)

        # Check to ensure there is still only one user
        users = User.objects.all()
        self.assertEqual(users.count(), 1)
        self.assertEqual(users.first().username, data1.get('sender'))

    def test_two_emails_different_senders_different_attachments_gets_created(self):
        data1 = copy.deepcopy(mailgun_payload)
        file_path_1 = path.join(path.dirname(__file__), 'test_files/animal_spirits.html')
        attachment_1 = open(file_path_1, 'r').read()
        data1['attachment-1'] = open(file_path_1, 'r')

        data2 = copy.deepcopy(mailgun_payload)
        file_path_2 = path.join(path.dirname(__file__), 'test_files/innovation.html')
        attachment_2 = open(file_path_2, 'r').read()
        data2['attachment-1'] = open(file_path_2, 'r')
        data2['sender'] = 'another_email@gmail.com'

        # Send first email
        response = self.client.post(reverse('receive_inbound_email'), data1)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Send second email
        response = self.client.post(reverse('receive_inbound_email'), data2)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check to see if an email was indeed created
        emails = Email.objects.all()

        self.assertEqual(emails.count(), 2)

        # Check to see if a Volume was created
        volumes = Volume.objects.all()
        self.assertEqual(volumes.count(), 2)

        # Check to see if Highlights were created
        highlights = Highlight.objects.all()
        self.assertEqual(highlights.count(), 18)

        # Check to see if Highlights were created
        entries = Entry.objects.all()
        self.assertEqual(entries.count(), 2)

        # Check to ensure there is still only one user
        users = User.objects.all()
        self.assertEqual(users.count(), 2)
        self.assertEqual(users.first().username, data1.get('sender'))
        self.assertEqual(users.last().username, data2.get('sender'))

    # TODO: test_email_with_two_attachment_gets_created(self):
    # TODO: test_email_with_wrong_content_type(self):
    # TODO: Test a book with a title the books API can't find