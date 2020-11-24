from django.contrib.auth import get_user_model
from rest_framework import serializers, status

import farmster_server.services.user as user_service
from farmster_server.serializers.place import PlaceFullSerializer
from farmster_server.utils.timestamp_field import TimestampField
from farmster_server.models.user import User, OTPStorage
from drf_writable_nested import WritableNestedModelSerializer, NestedCreateMixin, NestedUpdateMixin
from rest_framework.exceptions import ValidationError
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.contrib.auth import authenticate
from rest_framework import exceptions
from django.utils.translation import gettext_lazy as _
from farmster_server.settings import base

user_model = get_user_model()


class UserCreateSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=255, allow_blank=False)
    first_name = serializers.CharField(max_length=255, allow_blank=False)
    last_name = serializers.CharField(max_length=255, allow_blank=False)
    language = serializers.CharField(max_length=2, allow_blank=False)

    class Meta:
        fields = ['phone_number', 'first_name', 'last_name', 'language']


class UserFullSerializer(serializers.ModelSerializer):
    default_place = PlaceFullSerializer()
    date_joined = TimestampField()
    last_login = TimestampField()
    contacts_count = serializers.SerializerMethodField()

    class Meta:
        model = user_model
        fields = ['id', 'is_valid', 'date_joined', 'last_login', 'default_place',
                  'phone_number', 'first_name', 'last_name', 'language', 'profile_picture', 'contacts_count']

    def get_contacts_count(self, user):
        return user.contacts.count() + user.farmers.count()


class UserRetrieveSerializer(serializers.ModelSerializer):
    default_place = PlaceFullSerializer()

    class Meta:
        model = user_model
        fields = ['default_place', 'phone_number', 'first_name', 'last_name', 'language', 'profile_picture']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = ['default_place', 'phone_number', 'first_name',
                  'last_name', 'language', 'profile_picture']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['groups', 'user_permissions']

        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self, validated_data):

            password = validated_data.pop('password')
            user = super().create(validated_data)
            user.set_password(password)
            user.save()
            return user

        def update(self, instance, validated_data):
            for attr, value in validated_data.items():
                if attr == 'password':
                    instance.set_password(value)
                else:
                    setattr(instance, attr, value)
            instance.save()
            return instance


class SendOTPSerializer(WritableNestedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class OTPVerificationSerializer(WritableNestedModelSerializer):
    class Meta:
        model = OTPStorage
        fields = ['otp', 'phone_id']


class RegisterUserSerializer(WritableNestedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):

        password = validated_data['password']
        if len(password) < 6:
            raise ValidationError('Minimum password length is 6', code=400)
        else:

            group_set = validated_data.pop("groups")
            permission_set = validated_data.pop("user_permissions")
            crop_set = validated_data.pop('crops')
            fav_crop_set = validated_data.pop("favorite_crop_listings")
            farmers_set = validated_data.pop("farmers")
            places_set = validated_data.pop("places")

            user = User(**validated_data)
            user.save()
            user.set_password(password)
            user.save()

            user.groups.set(group_set)
            user.user_permissions.set(permission_set)
            user.crops.set(crop_set)
            user.favorite_crop_listings.set(fav_crop_set)
            user.farmers.set(farmers_set)
            user.places.set(places_set)

            print(user)

            if user:
                return user
            else:
                user.delete()


class ForgotPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserpasswordResetSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    otp = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['otp', 'password', 'confirm_password']
        extra_kwargs = {
            'email': {
                'validators': [UnicodeUsernameValidator()],
            },

        }


class LoginCustomSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def _validate_phone(self, phone_number, password):

        if phone_number and password:

            user = self.authenticate(phone_number=phone_number, password=password)


        else:
            msg = _('Must include "phone" and "password".')
            raise exceptions.ValidationError(msg)
        return user

    def validate(self, attrs):

        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        user = None
        if 'allauth' in base.INSTALLED_APPS:
            from farmster_server import app_settings_custom  # Authentication through email

            if app_settings_custom.AUTHENTICATION_METHOD == app_settings_custom.AuthenticationMethod.PHONE:
                user = self._validate_phone(phone_number, password)

            else:
                msg = _('Invalid credential.')
                raise exceptions.ValidationError(msg)  # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)
        attrs['user'] = user
        return attrs
