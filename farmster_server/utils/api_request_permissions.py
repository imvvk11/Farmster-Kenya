from rest_framework.permissions import BasePermission

# from rfkeeper_server.queries import api_key as api_key_queries
from farmster_server.models.api_key import ApiKey


class IsSuperUser(BasePermission):
    """
    Allows access only to super users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_active and request.user.is_superuser


class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_active and request.user.is_superuser_or_admin


class EveryoneCanViewOnlySuperUserCanChange(BasePermission):
    """
    Allows access only to super users.
    """

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user and request.user.is_active
        return request.user and request.user.is_active and request.user.is_superuser


class EveryoneCanViewOnlyAdminUserCanChange(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user and request.user.is_active
        return request.user and request.user.is_active and request.user.is_superuser_or_admin


class HasApiKey(BasePermission):
    def has_permission(self, request, view):
        api_key = request.META.get('HTTP_API_KEY', '')
        if api_key:
            return ApiKey.objects.filter(key=api_key).exists()
        return False


class HasApiKeyOrAuthenticated(BasePermission):
    def has_permission(self, request, view):
        api_key = request.META.get('HTTP_API_KEY', '')
        if api_key:
            has_api_key = ApiKey.objects.filter(key=api_key).exists()
        else:
            has_api_key = False

        is_authenticated = bool(request.user and request.user.is_authenticated)

        return has_api_key | is_authenticated


