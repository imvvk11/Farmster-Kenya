from django.contrib.auth.models import AbstractUser
from django.db import models
from farmster_server.managers import user as user_manager

from farmster_server.models.crop import Crop
from farmster_server.models.crop_listing import CropListing
from farmster_server.models.farmer import Farmer
from farmster_server.models.place import Place
from django.utils import timezone

from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = None
    email = None
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    is_admin = models.BooleanField(default=False)
    default_place = models.ForeignKey(Place, on_delete=models.SET_NULL, related_name="default_place_users", null=True)
    phone_number = models.CharField(max_length=255, blank=False, unique=True)
    language = models.CharField(max_length=2, blank=False)
    profile_picture = models.URLField(max_length=255, blank=True)
    is_valid = models.BooleanField(default=False)
    code_expiring_date = models.DateTimeField(default=timezone.now)
    crops = models.ManyToManyField(Crop, related_name="users")
    places = models.ManyToManyField(Place, related_name="users")
    favorite_crop_listings = models.ManyToManyField(CropListing, related_name="users")
    farmers = models.ManyToManyField(Farmer, related_name="users")

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = user_manager.UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class OTPStorage(models.Model):
    verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6)
    otp_start = models.DateTimeField()
    otp_end = models.DateTimeField()
    expired = models.BooleanField(default=False)
    phone_id = models.CharField(max_length=255, blank=False, unique=True)

    @property
    def is_expired(self):

        time_threshold = self.otp_end

        if timezone.now() <= time_threshold:
            return False
        else:
            return True
