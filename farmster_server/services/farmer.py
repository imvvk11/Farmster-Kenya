from django.db.models import QuerySet

from farmster_server.models.farmer import Farmer
from farmster_server.services import place as place_service


def get_all_farmers() -> QuerySet:
    return Farmer.objects.all()


def get_farmer_by_id(farmer_id: int) -> Farmer:
    return Farmer.objects.get(id=farmer_id)


def add_place_for_farmer(farmer_id: int, place_id: int) -> Farmer:
    farmer = get_farmer_by_id(farmer_id)
    place = place_service.get_place_by_id(place_id)
    farmer.places.add(place)
    farmer.save()
    return farmer


def remove_place_from_farmer(farmer_id: int, place_id: int) -> Farmer:
    farmer = get_farmer_by_id(farmer_id)
    place = place_service.get_place_by_id(place_id)
    farmer.places.remove(place)
    farmer.save()
    return farmer


def get_or_create_farmer_by_phone_number(kwargs):
    farmer, created = Farmer.objects.get_or_create(
        phone_number=kwargs['phone_number'],
        defaults={**kwargs}
    )
    return farmer

