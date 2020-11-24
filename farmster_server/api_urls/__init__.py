from farmster_server.api_urls.agent import agent_urlpatterns
from farmster_server.api_urls.bot import bot_urlpatterns
from farmster_server.api_urls.contact import contact_urlpatterns
from farmster_server.api_urls.crop_listing import crop_listing_urlpatterns
from farmster_server.api_urls.deal import deal_urlpatterns
from farmster_server.api_urls.farmer import farmer_urlpatterns
from farmster_server.api_urls.media import media_urlpatterns
from farmster_server.api_urls.crop import crop_urlpatterns
from farmster_server.api_urls.place import place_urlpatterns
from farmster_server.api_urls.user import user_urlpatterns
from farmster_server.api_urls.user_crop_listings import user_crop_listings_urlpatterns
from farmster_server.api_urls.user_crops import user_crops_urlpatterns
from farmster_server.api_urls.user_farmers import user_farmers_urlpatterns
from farmster_server.api_urls.user_places import user_places_urlpatterns

from farmster_server.api_urls.vendor import vendor_urlpatterns

api_urlpatterns = []

api_urlpatterns += media_urlpatterns
api_urlpatterns += crop_urlpatterns
api_urlpatterns += user_urlpatterns
api_urlpatterns += user_crops_urlpatterns
api_urlpatterns += agent_urlpatterns
api_urlpatterns += place_urlpatterns
api_urlpatterns += user_places_urlpatterns
api_urlpatterns += crop_listing_urlpatterns
api_urlpatterns += user_crop_listings_urlpatterns
api_urlpatterns += farmer_urlpatterns
api_urlpatterns += deal_urlpatterns
api_urlpatterns += user_farmers_urlpatterns
api_urlpatterns += contact_urlpatterns
api_urlpatterns += bot_urlpatterns
api_urlpatterns += vendor_urlpatterns
