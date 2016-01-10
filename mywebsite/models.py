from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=500)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False)