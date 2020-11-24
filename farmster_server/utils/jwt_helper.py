from rest_framework_jwt import utils


def set_key_on_token(token: dict, key: str, value: str):
    token_data = utils.jwt_decode_handler(token)
    token_data[key] = value
    new_token = utils.jwt_encode_handler(token_data)
    return new_token


def get_token_value_by_key(token: dict, key: str):
    try:
        token_data = utils.jwt_decode_handler(token)
    except KeyError:
        return None
    return token_data[key]
