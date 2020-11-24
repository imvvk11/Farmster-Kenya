from django.db import models


class Agent(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
