import unittest

from django.test import TestCase, Client
from django.urls import reverse
from django.core.mail import EmailMultiAlternatives
from .test_files.mailgun_post import spirit_animals_payload as mailgun_payload

# from unittest import mockfrom contextlib import contextmanager

# Create your tests here.
# @contextmanagerdef catch_signal(signal):
#     """Catch django signal and return the mocked call."""
#     handler = mock.Mock()
#     signal.connect(handler)
#     yield handler
#     signal.disconnect(handler)

class IndexTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        self.assertEqual(response.content ,b'INDEX VIEW')

class EmailTest(unittest.TestCase):
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


    def test_mailgun_post_succeeds(self):
        data = mailgun_payload
        del data['stripped-html']
        response = self.client.post(reverse('receive_inbound_email'), data)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        # self._assertEmailParsedCorrectly(email, mailgun_payload)