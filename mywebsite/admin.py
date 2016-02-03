from django.contrib import admin

from .models import Message, Blog

admin.site.register(Message)
admin.site.register(Blog)
