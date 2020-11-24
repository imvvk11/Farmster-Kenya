from datetime import datetime, timedelta

from django.core.management import BaseCommand
from django.utils import timezone

from farmster_server.models.choices import CROP_LISTING_STATUS
from farmster_server.models.crop_listing import CropListing


class Command(BaseCommand):
    def handle(self, *args, **options):
        now = datetime.now()
        seven_days_ago = datetime(year=now.year, month=now.month, day=now.day, tzinfo=timezone.get_current_timezone()) - timedelta(days=7)

        queryset = CropListing.objects.all()
        queryset = CropListing.objects.filter_crop_listing_by_queryset_harvest_time_to(queryset, seven_days_ago)
        queryset = CropListing.objects.filter_crop_listing_by_status(queryset, CROP_LISTING_STATUS.ACTIVE)
        queryset.update(status=CROP_LISTING_STATUS.EXPIRED)
