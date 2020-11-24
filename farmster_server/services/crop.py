from django.db.models import QuerySet

from farmster_server.models.crop import Crop


def get_all_crops() -> QuerySet:
    return Crop.objects.all()


def get_crop_by_id(crop_id: int):
    return Crop.objects.get(id=crop_id)
