from django.db import models

from farmster_server.models.farmer import Farmer
from farmster_server.models.user import User
from farmster_server.managers import deal as deal_manager


class Deal(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.SET_NULL, related_name="deals", null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="deals", null=True)

    objects = deal_manager.DealManager()

    def __str__(self):
        if self.farmer:
            return f'{self.user} - {self.farmer.first_name} {self.farmer.last_name}'
        else:
            return f'{self.user} - No Farmer'

