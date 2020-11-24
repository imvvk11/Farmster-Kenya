from django.db import models

from farmster_server.models.user import User


class Contact(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=255, blank=False, unique=True)
    location = models.CharField(max_length=255, blank=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="contacts", null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



