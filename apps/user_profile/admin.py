from django.contrib import admin
from .models import Profile, SignalEntry


admin.site.register(SignalEntry)
admin.site.register(Profile)
