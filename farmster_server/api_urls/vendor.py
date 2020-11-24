from django.conf.urls import url
from farmster_server.views import vendor
from django.urls import path
from django.conf.urls import include

from rest_framework import routers

# Our Code ----> Starts from here
router = routers.DefaultRouter()
router.register(r'vendor/call/count', vendor.VendorCountAPIView, basename='vendor')

vendor_urlpatterns = [
    path('', include(router.urls)),
]