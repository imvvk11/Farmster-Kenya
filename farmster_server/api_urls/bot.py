from django.conf.urls import url
from farmster_server.views import bot

bot_urlpatterns = [
    url(r'^bot/places/$', bot.bot_create_place, name='bot_create_place'),
    url(r'^bot/farmers/$', bot.bot_create_farmer, name='bot_create_farmer'),
    url(r'^bot/deals/$', bot.bot_create_deal, name='bot_create_deal')
]
