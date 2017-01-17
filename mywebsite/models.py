from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created = models.DateTimeField(max_length=100)
    checked = models.BooleanField(default=False)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    time_added = models.CharField(max_length=100)
    template_file = models.CharField(max_length=100)
