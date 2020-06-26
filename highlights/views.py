import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.dispatch import receiver
from inbound_email.signals import email_received, email_received_unacceptable

@receiver(email_received, dispatch_uid="something_unique")
def on_email_received(sender, **kwargs):
    """Handle inbound emails."""
    email = kwargs.pop('email')
    request = kwargs.pop('request')

    # your code goes here - save the email, respond to it, etc.
    logging.info(
        "New email received from %s: %s",
        email.from_email,
        email.subject
    )

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

