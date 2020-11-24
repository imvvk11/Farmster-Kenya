from threading import current_thread
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class DefaultAuth(JSONWebTokenAuthentication):
    def authenticate(self, request):
        auth_result = super(DefaultAuth, self).authenticate(request)
        if auth_result:
            user, jwt_value = auth_result
            current_thread().user = user
            return user, jwt_value
        return None


def get_current_user():
    t = current_thread()
    if hasattr(t, 'user'):
        return current_thread().user
    return None
