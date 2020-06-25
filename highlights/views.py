import logging

from django.http import HttpResponse
from django.shortcuts import render
from inbound_email.signals import email_received

def on_email_received(sender, **kwargs):
    """Handle inbound emails."""
    email = kwargs.pop('email')
    request = kwargs.pop('request')

    # your code goes here - save the email, respond to it, etc.
    logging.debug(
        "New email received from %s: %s",
        email.from_email,
        email.subject
    )

# pass dispatch_uid to prevent duplicates:
# https://docs.djangoproject.com/en/dev/topics/signals/
email_received.connect(on_email_received, dispatch_uid="something_unique")

def index(request):
    return HttpResponse("INDEX VIEW")

