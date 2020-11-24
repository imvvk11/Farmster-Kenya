from django.contrib.auth import get_user_model
from rest_framework import views, status
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebToken
from farmster_server.utils import jwt_helper, error_response_handler
from farmster_server.services import user as user_service
from django.utils.translation import gettext_lazy as _

user_model = get_user_model()


class Login(ObtainJSONWebToken):

    def post(self, request, *args, **kwargs):
        if 'code' not in request.data:
            raise exceptions.AuthenticationFailed(_("'code' field is required"))

        request.data['password'] = request.data['code']
        del request.data['code']
        response = super().post(request, *args, **kwargs)

        phone_number = request.data['phone_number']
        code = request.data['password']

        if not user_service.is_login_code_valid(phone_number, code):
            raise exceptions.AuthenticationFailed(_('The code is invalid or has expired'))

        if status.is_success(response.status_code):
            phone_number = phone_number
            user_service.set_user_valid(phone_number, True)
            user_service.reset_one_time_code(phone_number)
            user_service.update_last_login(phone_number)
        else:
            response = error_response_handler.handle_error_response(response)

        return response


class Logout(views.APIView):
    def post(self, request, *args, **kwargs):
        return Response('logged out')


login = Login.as_view()
logout = Logout.as_view()
