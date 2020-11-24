def set_on_session(request, key: str, val):
    request.session[key] = val


def get_from_session(request, key: str, default_val=''):
    return request.session.get(key, default_val)
