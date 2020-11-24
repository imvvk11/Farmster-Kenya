from django.db.models import QuerySet, Q

from farmster_server.models.choices import PLACE_TYPE
import geopy.distance
from farmster_server.models.place import Place
from farmster_server.services import agent as agent_service


def get_all_places() -> QuerySet:
    return Place.objects.all()


def get_all_regions() -> QuerySet:
    return Place.objects.order_by().values_list('district', flat=True).distinct()


def get_place_by_id(place_id: int):
    return Place.objects.get(id=place_id)


def get_or_create_place_by_name_district(kwargs):
    kwargs['type'] = PLACE_TYPE.VILLAGE
    place, created = Place.objects.get_or_create(
        name=kwargs['name'],
        district=kwargs['district'],
        defaults={**kwargs}
    )
    return place


def add_agent_for_place(place_id: int, agent_id: int) -> Place:
    place = get_place_by_id(place_id)
    agent = agent_service.get_agent_by_id(agent_id)
    place.agents.add(agent)
    place.save()
    return place


def remove_agent_from_place(place_id: int, agent_id: int) -> Place:
    place = get_place_by_id(place_id)
    agent = agent_service.get_agent_by_id(agent_id)
    place.agents.remove(agent)
    place.save()
    return place


def get_all_farmer_by_place_id(place_id: int):
    place = get_place_by_id(place_id)
    return place.farmers.all()


def get_places_by_name_or_district(user_lat: float, user_lon: float, text: str = None) -> []:
    if text:
        return Place.objects.filter(Q(name__startswith=text) | Q(district__startswith=text))
    return Place.objects.all()


def get_user_distance(place: int, user_lat: float, user_lon: float):
    coords_1 = (user_lat, user_lon)
    coords_2 = (place.location_lat, place.location_lon)
    return geopy.distance.vincenty(coords_1, coords_2).km

