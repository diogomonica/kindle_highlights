from django.db import models

class Email(models.Model):
    sender = models.CharField(max_length=255)
    sender_email = models.EmailField(default="EMPTY_EMAIL")
    subject = models.TextField(max_length=1000)
    body = models.TextField()
    received_at = models.DateTimeField(auto_now=True)
    attachment = models.TextField(default="")

    class Meta:
        verbose_name_plural = 'emails'

    def __str__(self):
        return u"%s - %s" % (self.sender_email, self.subject)