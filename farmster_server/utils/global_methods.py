import typing
import random
import requests
from django.core.files.temp import NamedTemporaryFile


def save_list_on_entity(entity: typing.T, list: [any]):
    if len(list) is 0:
        list.set([])

    for item in list:
        list.add(item)

    entity.save()


def download_from_url_to_temp_file(url):
    success = False
    lf = NamedTemporaryFile(delete=True)
    request = requests.get(url, stream=True)
    if request.status_code == requests.codes.ok:
        for block in request.iter_content(1024 * 8):
            if not block:
                break
            lf.write(block)
        success = True
    return success, lf


def generate_code():
    code = ''.join(random.choice('0123456789') for _ in range(6))
    return code
