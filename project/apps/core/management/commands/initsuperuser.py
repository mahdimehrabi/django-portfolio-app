from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Create initial superuser"

    def handle(self, *args, **options):
        username = settings.SUPERUSER_USERNAME
        superuser_count = User.objects.filter(
            username=username).count()
        if superuser_count == 0:
            user = User.objects.create_user(username=username,
                                            password=settings.SUPERUSER_INITIAL_PASSWORD)
            user.email = settings.SUPERUSER_EMAIL
            user.is_superuser = True
            user.is_staff = True
            user.save()
            print('Created account for %s' % (username,))
        else:
            print('%s Already exists!', (username,))
