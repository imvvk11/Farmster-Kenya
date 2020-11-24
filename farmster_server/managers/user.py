from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone

from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError(_('The Phone Number must be set'))
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        print(user.password)
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(phone_number, password, **extra_fields)

    def get_user_by_phone_number(self, phone_number: str):
        return self.filter(phone_number=phone_number).first()

    def set_user_valid(self, phone_number: str, is_valid: bool) -> bool:
        count = self.filter(phone_number=phone_number).update(is_valid=is_valid)
        return count > 0

    def reset_one_time_code(self, phone_number: str) -> bool:
        count = self.filter(phone_number=phone_number).update(password='')
        return count > 0

    def get_user_crops(self, user_id: int):
        user = self.get(id=user_id)
        return user.crops.all()

    def get_user_deals(self, user_id: int):
        user = self.get(id=user_id)
        return user.deals.all()

    def get_user_contacts(self, user_id: int):
        user = self.get(id=user_id)
        return user.contacts.all()

    def get_user_places(self, user_id: int):
        user = self.get(id=user_id)
        return user.places.all()

    def get_user_farmers(self, user_id: int):
        user = self.get(id=user_id)
        return user.farmers.all()

    def get_user_crop_listings(self, user_id: int):
        user = self.get(id=user_id)
        return user.favorite_crop_listings.all().order_by('harvest_date')

    def update_last_login(self, phone_number: str) -> bool:
        count = self.filter(phone_number=phone_number).update(last_login=timezone.now())
        return count > 0
