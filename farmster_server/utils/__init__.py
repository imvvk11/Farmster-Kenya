import logging

from django.core.exceptions import PermissionDenied
from django.http import Http404, JsonResponse
from django.utils import six
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions, status
from rest_framework.response import Response
from rest_framework.views import set_rollback

logger = logging.getLogger(__name__.split('.')[0])


class ObjectFormDict(object):
    def __init__(self, d):
        self.__dict__ = d


def exception_handler(exc, context):
    logger.exception(msg="An Error Has Occurred", exc_info=exc)

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait
        if isinstance(exc.detail, (list, dict)):
            data = exc.detail
        else:
            data = {'detail': exc.detail}

        set_rollback()
        return Response(data, status=exc.status_code, headers=headers)

    elif isinstance(exc, Http404):
        msg = _('Not found.')
        data = {'detail': six.text_type(msg)}

        set_rollback()
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    elif isinstance(exc, PermissionDenied):
        msg = _('Permission denied.')
        data = {'detail': six.text_type(msg)}

        set_rollback()
        return Response(data, status=status.HTTP_403_FORBIDDEN)

    return Response({'detail': six.text_type(str(exc))}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def custom404(request, exception):
    return JsonResponse({'success': False, 'data': None, 'error': 'The resource was not found'},
                        status=status.HTTP_404_NOT_FOUND)


def custom500(request):
    return JsonResponse({'success': False, 'data': None, 'error': 'Internal server error'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
