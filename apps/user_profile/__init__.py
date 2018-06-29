from .signals import signals_handler

from django.db.models.signals import post_save
from django.db.models.signals import post_delete


post_save.connect(signals_handler)
post_delete.connect(signals_handler)
