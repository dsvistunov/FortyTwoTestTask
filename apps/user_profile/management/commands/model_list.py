from django.core.management.base import BaseCommand
from optparse import make_option
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--stderr',
                    action='store_true',
                    dest='tee',
                    default=False,
                    help='duplicate output to stderr'),
        )

    def handle(self, *args, **options):
        for item in ContentType.objects.all():
            model = item.model_class()
            output = "%s.%s\t%d" % (
                model.__module__,
                model.__name__,
                model._default_manager.count()
            )

            self.stdout.write("%s\n" % output)
