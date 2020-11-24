from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from farmster_server.serializers import user as user_serializers
from farmster_server.serializers.contact import ContactSerializer
from farmster_server.serializers.deal import DealFullSerializer
from farmster_server.services import user as user_service
from farmster_server.utils.custom_generation import generate_token_custom
from farmster_server.utils.serializer_mixins import UpdateModelWithFullResultMixin
from farmster_server.models.user import User, OTPStorage
from farmster_server.serializers.user import UserSerializer, SendOTPSerializer, OTPVerificationSerializer, \
    RegisterUserSerializer, ForgotPasswordSerializer, UserpasswordResetSerializer
from rest_framework import viewsets
from django.utils import timezone
from datetime import timedelta
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UsersCreateApi(generics.GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer_class = user_serializers.UserCreateSerializer(data=self.request.data)
        if serializer_class.is_valid(raise_exception=True):
            user = user_service.get_or_create_new_user(**serializer_class.validated_data)
            return Response(data=user_serializers.UserFullSerializer(user).data, status=status.HTTP_201_CREATED)


class UserMeApi(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK, data=user_serializers.UserFullSerializer(request.user).data)


class UserRetrieveUpdateAPI(UpdateModelWithFullResultMixin, generics.RetrieveUpdateAPIView):
    queryset = user_service.get_all_users()
    write_serializer_class = user_serializers.UserUpdateSerializer
    read_serializer_class = user_serializers.UserRetrieveSerializer


class UserResendCodeApi(generics.GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        user_id = kwargs["pk"]
        user_service.resend_code(user_id)
        return Response(status=status.HTTP_200_OK)


class UserRetrieveDealsApi(generics.ListAPIView):
    serializer_class = DealFullSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        queryset = user_service.get_user_deals(user_id)
        return queryset


class UserRetrieveContactsApi(generics.ListAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = user_service.get_user_contacts(user_id)
        return queryset


user_create = UsersCreateApi.as_view()
user_me = UserMeApi.as_view()
user_retrieve_update = UserRetrieveUpdateAPI.as_view()
user_resend_code = UserResendCodeApi.as_view()
user_retrieve_deals = UserRetrieveDealsApi.as_view()
user_retrieve_contacts = UserRetrieveContactsApi.as_view()


def otp_phone(phone):
    """
    This method generates the OTP for email verification, sends the email to the respective email ids,
    and then checks if the OTP's are present in the OTPStorage model,fi not create a new one.
    :param phone:
    :return:
    """
    phone = phone
    generated_token = generate_token_custom()
    print("Generated token for phone is: ", generated_token, phone)
    message = '{} {} {}'.format('Please find the otp generated for your registered phone number. ',
                                generated_token, 'Please enter the correct otp to complete your'
                                                 'verification')
    try:
        x = OTPStorage.objects.filter(phone_id=phone)

        obj = OTPStorage.objects.get(phone_id=phone)
        obj.otp = generated_token
        obj.otp_start = timezone.now()
        obj.otp_end = obj.otp_start + timedelta(minutes=10)
        obj.phone_id = phone

        obj.save()

    except Exception:
        obj = OTPStorage()
        obj.otp = generated_token
        obj.otp_start = timezone.now()
        obj.otp_end = obj.otp_start + timedelta(minutes=10)
        obj.phone_id = phone
        obj.save()
    if obj:
        return obj.otp
    else:
        return None


class RegisterUserSendOTPView(viewsets.ModelViewSet):
    serializer_class = SendOTPSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):

        obj = otp_phone(request.data['phone_number'])
        if obj is not None:
            return Response({'message': 'OTP Sent', "Otp": obj}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Something went wrong please register again. Please check the '
                                        ' number you have entered'},
                            status=status.HTTP_400_BAD_REQUEST)


class OTPVerification(viewsets.ModelViewSet):
    serializer_class = OTPVerificationSerializer
    queryset = OTPStorage.objects.none()
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        phone = request.data['phone_id']
        print(phone)
        obj = OTPStorage.objects.filter(phone_id=phone).values_list('otp', flat=True).last()
        print(obj)
        obj1 = [obj for obj in OTPStorage.objects.filter(phone_id=phone) if obj.is_expired]
        x = request.data['otp']

        if str(obj) == str(x):
            a = OTPStorage.objects.get(phone_id=phone)
            if a not in obj1:
                a.verified = True
                a.delete()
                return Response({'data': 'otp verified'}, status=status.HTTP_200_OK)
            else:
                a.expired = True
                a.delete()
                return Response({'data': 'otp expired. Please register again'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'data': 'Wrong Parameters entered'}, status=status.HTTP_412_PRECONDITION_FAILED)


class RegisterUserVerifyView(viewsets.ModelViewSet):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_object(self):
        return User.objects.get(pk=self.kwargs.get('pk'))

    def partial_update(self, request, *args, **kwargs):
        contact_object = self.get_object()
        x = User.objects.filter(id=self.kwargs.get('pk')).values_list('users__id', flat=True).last()

        serializer = RegisterUserSerializer(contact_object, data=request.data,
                                            partial=True)

        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)

            serializer.save()

            return Response({'data': [serializer.data]}, status=status.HTTP_200_OK)

        return Response({'message': 'Wrong Parameters'}, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        if self.action == 'retrieve':
         return [AllowAny(), ]
        return super(RegisterUserVerifyView, self).get_permissions()


class ForgotPasswordSendOTPView(viewsets.ModelViewSet):
    serializer_class = ForgotPasswordSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):

        x = User.objects.filter(phone_number=request.data['phone_number'])
        if x.count() > 0:
            obj = otp_phone(request.data['phone_number'])
            if obj is not None:
                return Response({'message': 'OTP Sent', "Otp": obj}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Something went wrong please try again. Please check the '
                                            ' number you have entered'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Please enter the registered mobile number. This is not the registered'
                                        ' mobile number'},
                            status=status.HTTP_400_BAD_REQUEST)


class PasswordResetModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = UserpasswordResetSerializer
    queryset = User.objects.none()
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        x = request.data['otp']
        updating_password = request.data['password']
        validating_password = request.data['confirm_password']
        c = OTPStorage.objects.filter(otp=x)
        if not c:
            return Response({"otp": ["Wrong otp entered."]}, status=status.HTTP_400_BAD_REQUEST)
        else:
            a = OTPStorage.objects.filter(otp=x).values_list('phone_id', flat=True).last()
            object = User.objects.get(phone_number=a)
            ob = OTPStorage.objects.get(otp=x)
            print(ob.otp_end)
            print(timezone.now())
            if timezone.now() > ob.otp_end:
                ob.delete()
                raise serializers.ValidationError("Otp is expired!", code=400)

            if updating_password != validating_password:
                raise serializers.ValidationError("Please enter the same password!", code=400)
            else:
                object.password = make_password(updating_password)
                object.save()
                ob = OTPStorage.objects.get(otp=x)
                ob.delete()

            return Response({"otp": ["Your password has been changed"], 'status': "200"},
                            status=status.HTTP_200_OK)
