from django.contrib import admin

from farmster_server.admin.admin_models import *
from farmster_server.models.agent import Agent
from farmster_server.models.api_key import ApiKey
from farmster_server.models.contact import Contact
from farmster_server.models.crop import Crop
from farmster_server.models.crop_listing import CropListing
from farmster_server.models.deal import Deal
from farmster_server.models.farmer import Farmer
from farmster_server.models.media import Media
from farmster_server.models.place import Place
from farmster_server.models.user import OTPStorage

admin.site.register(get_user_model(), FarmsterUserAdmin)
admin.site.register(Crop, CropAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Farmer, FarmerAdmin)
admin.site.register(Deal, DealAdmin)
admin.site.register(CropListing, CropListingAdmin)
admin.site.register(Media)
admin.site.register(ApiKey)
admin.site.register(Contact, ContactAdmin)
admin.site.register(DealPart, DealPartsAdmin)
admin.site.register(OTPStorage)
