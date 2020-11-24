from django.core.management import BaseCommand

from farmster_server.utils import at_helper


class Command(BaseCommand):
    def handle(self, *args, **options):
        result = at_helper.send_sms('+972545951236', 'Your login code for Farmster is: 123123')
        print(result)
