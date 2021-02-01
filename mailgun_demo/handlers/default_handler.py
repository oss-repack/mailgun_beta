"""
DEFAULT HANDLER
"""
from os import path
from urllib.parse import urljoin
from .error_handler import ApiError


def handle_default(url, domain, method, **kwargs):
    if not domain:
        raise ApiError("Domain is missing!")

    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    url = url["base"] + domain + final_keys

    print(url)
    return url