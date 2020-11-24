import requests
from django.core.management import BaseCommand

from farmster_server.models.crop import Crop


class Command(BaseCommand):
    def handle(self, *args, **options):
        for crop in Crop.objects.all():
            if 'farmster.mixinsoftware.com' in crop.image_url:
                old_url = crop.image_url
                new_url = crop.image_url.replace('https://farmster.mixinsoftware.com/media/files/',
                                                 'https://api.farmster.co/static/icons/')

                response = requests.get(new_url)
                if response.status_code == 200:
                    content_type = response.headers.get('Content-Type')
                    if 'image/png' in content_type:
                        crop.image_url = new_url
                        crop.save()
                        print(f'changed {old_url} --> {new_url}')
