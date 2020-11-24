from rest_framework import status
from rest_framework.renderers import JSONRenderer

from farmster_server.settings.version import VERSION


class JsonResponseRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if status.is_client_error(renderer_context['response'].status_code) or \
                status.is_server_error(renderer_context['response'].status_code):
            if isinstance(data, dict) and 'detail' in data:
                response_data = {'success': False, 'data': None, 'error': data['detail']}
            elif isinstance(data, dict):
                response_data = {'success': False, 'data': None, 'error': data}
            else:
                response_data = {'success': False, 'data': None, 'error': str(data)}
        else:
            response_data = {'success': True, 'data': data, 'error': None}
        response_data['version'] = VERSION
        return super(JsonResponseRenderer, self).render(response_data, accepted_media_type, renderer_context)
