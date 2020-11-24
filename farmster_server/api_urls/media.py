from django.conf.urls import url
from farmster_server.views import media

media_urlpatterns = [
    url(r'^media/$', media.media_upload)
]
