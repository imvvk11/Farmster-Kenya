import uuid

from django.db import models


def generate_key():
    return str(uuid.uuid4()).replace("-", "")


class ApiKey(models.Model):
    key = models.CharField(max_length=40, primary_key=True, blank=True)
    name = models.CharField(max_length=255, blank=True)
    is_enabled = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = generate_key()
        return super(ApiKey, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.key
