from .models import SignalEntry


IGNORELIST = (
    'SignalEntry',
    'Request',
    'LogEntry',
)


def signals_handler(sender, **kwargs):
    if sender._meta.object_name in IGNORELIST:
        return

    action = SignalEntry.DELETE

    if 'created' in kwargs:
        action = kwargs.get('created') and \
                 SignalEntry.CREATE or SignalEntry.UPDATE

    SignalEntry.objects.create(
        model=sender._meta.object_name,
        instance=unicode(kwargs.get('instance')),
        action=action)
