from django.conf.urls import url
from farmster_server.views import user
from django.urls import path
from django.conf.urls import include

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'sendotp', user.RegisterUserSendOTPView, basename='sendotp')
router.register(r'verifyotp', user.OTPVerification, basename='OTPVerification')
router.register(r'register', user.RegisterUserVerifyView, basename='Register')
router.register(r'password/reset', user.PasswordResetModelViewSet, basename='PasswordResetModelViewSet')
router.register(r'forgotpassword', user.ForgotPasswordSendOTPView, basename='ForgotPasswordSendOTPView')

user_urlpatterns = [
    path('', include(router.urls)),
    url(r'^users/(?P<user_id>\d+)/deals/$', user.user_retrieve_deals, name='user_retrieve_deals'),
    url(r'^users/(?P<user_id>\d+)/contacts/$', user.user_retrieve_contacts, name='user_retrieve_contacts')
]
