from django.db import models

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

    def __str__(self):
        return u"%s - %s" % (self.google_id, self.title + " - " + self.subtitle)
