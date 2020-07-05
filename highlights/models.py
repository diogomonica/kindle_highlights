from django.db import models
from django.contrib.auth.models import User

class Email(models.Model):
    sender = models.CharField(max_length=255)
    sender_email = models.EmailField(default="EMPTY_EMAIL")
    subject = models.TextField(max_length=1000)
    body = models.TextField()
    received_at = models.DateTimeField(auto_now=True)
    attachment = models.TextField(default="")
    parsed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'emails'
        ordering = ['received_at']

    def __str__(self):
        return u"%s - %s" % (self.sender_email, self.subject)


class Volume(models.Model):
    google_id = models.CharField(unique=True, max_length=100)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    published_date = models.DateField()
    publisher = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    page_count = models.IntegerField()

    class Meta:
        verbose_name_plural = 'volumes'
        ordering = ['created_at']

    def __str__(self):
        return u"%s - %s" % (self.google_id, self.title + " - " + self.subtitle)

class Entry(models.Model):
    volume = models.ForeignKey(to=Volume, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'entries'
        ordering = ['created_at']

    def __str__(self):
        return u"%s : %s" % (self.created_at, self.volume.title)

class Highlight(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    volume = models.ForeignKey(to=Volume, on_delete=models.CASCADE)
    entry = models.ForeignKey(to=Entry, on_delete=models.CASCADE)
    color = models.CharField(max_length=30)
    location = models.IntegerField()
    highlight_type = models.CharField(max_length=20)
    content = models.TextField()

    class Meta:
        ordering = ['location']
        verbose_name_plural = 'highlights'

    def __str__(self):
        return u"%s - %s" % (self.location, self.content)
