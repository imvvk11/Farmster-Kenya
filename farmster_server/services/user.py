from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _
from datetime import timedelta

from farmster_server import settings
from farmster_server.services import crop as crop_service
from farmster_server.services import crop_listing as crop_listing_service
from farmster_server.services import place as place_service
from farmster_server.services import farmer as farmer_service
from farmster_server.utils import global_methods, at_helper
from django.contrib.auth import get_user_model
from django.utils import timezone


user_model = get_user_model()


def get_all_users() -> QuerySet:
    return user_model.objects.all()


def get_user_crops(user_id: int) -> QuerySet:
    return user_model.objects.get_user_crops(user_id)


def get_user_farmers(user_id: int) -> QuerySet:
    return user_model.objects.get_user_farmers(user_id)


def get_user_deals(user_id: int) -> QuerySet:
    return user_model.objects.get_user_deals(user_id)


def get_user_contacts(user_id: int) -> QuerySet:
    return user_model.objects.get_user_contacts(user_id)


def get_user_crop_listings(user_id: int) -> QuerySet:
    return user_model.objects.get_user_crop_listings(user_id)


def get_user_places(user_id: int) -> QuerySet:
    return user_model.objects.get_user_places(user_id)


def get_user_by_id(user_id: int):
    return user_model.objects.get(id=user_id)


def set_user_valid(phone_number: str, is_valid: bool):
    return user_model.objects.set_user_valid(phone_number, is_valid)


def reset_one_time_code(phone_number: str):
    return user_model.objects.reset_one_time_code(phone_number)


def resend_code(user_id: int):
    user = get_user_by_id(user_id)
    _send_code_to_user(user)


def is_login_code_valid(phone_number: str, code: str) -> bool:
    user = user_model.objects.get_user_by_phone_number(phone_number)
    now = timezone.now()
    print('login_valid',user.__dict__,now < user.code_expiring_date)
    return now < user.code_expiring_date


def get_or_create_new_user(phone_number: str, first_name: str, last_name: str, language: str) -> user_model:
    phone_number = phone_number.strip().strip('+')
    user, created = user_model.objects.get_or_create(
        phone_number=phone_number,
        defaults={
            'phone_number': phone_number,
            'first_name': first_name,
            'last_name': last_name,
            'language': language
        }
    )

    _send_code_to_user(user)
    return user


def _send_code_to_user(user: user_model):
    phone_number = user.phone_number
    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number

    if phone_number == '+972500000000':
        user.code_expiring_date = timezone.now() + timedelta(weeks=52)
        user.set_password('120340')
        user.save()
    else:
        code = global_methods.generate_code()
        msg = _('Your login code for Farmster is:') + ' ' + code
        at_helper.send_sms(phone_number, msg)
        user.code_expiring_date = timezone.now() + timedelta(minutes=settings.TOKEN_EXPIRATION_TIME_MINUTES)
        user.set_password(code)
        user.save()


def add_crop_for_user(crop_id, user_id) -> user_model:
    user = get_user_by_id(user_id=user_id)
    crop = crop_service.get_crop_by_id(crop_id)
    user.crops.add(crop)
    user.save()
    return user


def remove_crop_from_user(crop_id, user_id) -> user_model:
    user = get_user_by_id(user_id=user_id)
    crop = crop_service.get_crop_by_id(crop_id)
    user.crops.remove(crop)
    user.save()
    return user


def add_farmer_for_user(farmer_id, user_id) -> user_model:
    user = get_user_by_id(user_id=user_id)
    farmer = farmer_service.get_farmer_by_id(farmer_id)
    user.farmers.add(farmer)
    user.save()
    return user


def remove_farmer_from_user(farmer_id, user_id) -> user_model:
    user = get_user_by_id(user_id=user_id)
    farmer = farmer_service.get_farmer_by_id(farmer_id)
    user.farmers.remove(farmer)
    user.save()
    return user


def add_place_for_user(place_id, user_id) -> user_model:
    user = get_user_by_id(user_id=user_id)
    place = place_service.get_place_by_id(place_id)
    user.places.add(place)
    user.save()
    return user


def remove_place_from_user(place_id, user_id) -> user_model:
    user = get_user_by_id(user_id=user_id)
    place = place_service.get_place_by_id(place_id)
    user.places.remove(place)
    user.save()
    return user


def add_crop_listing_for_user(crop_listing_id, user_id) -> user_model:
    user = get_user_by_id(user_id=user_id)
    crop_listing = crop_listing_service.get_crop_listing_by_id(crop_listing_id)
    user.favorite_crop_listings.add(crop_listing)
    user.save()
    return user


def remove_crop_listing_from_user(crop_listing_id, user_id) -> user_model:
    user = get_user_by_id(user_id=user_id)
    crop_listing = crop_listing_service.get_crop_listing_by_id(crop_listing_id)
    user.favorite_crop_listings.remove(crop_listing)
    user.save()
    return user


def update_last_login(phone_number: str) -> bool:
    return user_model.objects.update_last_login(phone_number)
