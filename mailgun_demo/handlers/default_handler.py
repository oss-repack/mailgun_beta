"""
DEFAULT HANDLER
"""
from os import path
from .error_handler import ApiError


def handle_default(url, domain, _method, **_):
    """
    Default handler for endpoints with single url pattern
    (events, messages, stats)
    :param url: Incoming URL dictionary
    :param domain: Incoming domain
    :param _method: Incoming request method (but it's not used for handle_default)
    :param kwargs: kwargs
    :return: final url for default endpoint
    """
    if not domain:
        raise ApiError("Domain is missing!")

    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    url = url["base"] + domain + final_keys

    return url
