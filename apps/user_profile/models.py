from __future__ import unicode_literals

from PIL import Image
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
    photo = models.ImageField(null=True, blank=True, upload_to='photo/')

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        if self.photo:
            size = 200
            image = Image.open(self.photo)
            wpercent = (size / float(image.size[0]))
            hsize = int((float(image.size[1]) * float(wpercent)))
            image = image.resize((size, hsize), Image.ANTIALIAS)
            image.save(self.photo.path)


class Request(models.Model):
    http_inf = models.CharField(max_length=120)
    added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.http_inf
