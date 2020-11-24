from django.db import models


class Vendor(models.Model):
    phone_number = models.CharField(max_length=255, blank=False, unique=True)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.phone_number}"
