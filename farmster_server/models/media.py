from django.db import models

from farmster_server.utils.random_file_name import RandomFileName


class Media(models.Model):
    file = models.FileField(upload_to=RandomFileName('files'), max_length=255, blank=False)
