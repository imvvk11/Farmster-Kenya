from farmster_server.utils.error_codes import ERROR_CODES


def handle_error_response(response):
    if hasattr(response, 'data') and 'non_field_errors' in response.data:
        error_text = ', '.join(str(error) for error in response.data['non_field_errors'])
        response.data['message'] = error_text
        response.data['error_code'] = ERROR_CODES.WRONG_CREDENTIALS
    return response
