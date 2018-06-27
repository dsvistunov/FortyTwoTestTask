from __future__ import unicode_literals

from django.db import models


class Profile(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_birth = models.DateField(
        null=True, blank=True
    )
    email = models.EmailField(max_length=30)
    jabber = models.EmailField(max_length=30)
    skype = models.CharField(max_length=30)
    other_contacts = models.TextField()
    bio = models.TextField()
