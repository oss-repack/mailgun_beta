"""
DEFAULT HANDLER
"""
from os import path
from urllib.parse import urljoin
from .error_handler import ApiError


def handle_default(url, domain, method, **kwargs):
    """
    Default handler for endpoints with single url pattern
    (events, messages, stats)
     :param url: Incoming URL dictionary
    :param domain: Incoming domain
    :param method: Incoming request method
    :param kwargs: kwargs
    :return: final url for default endpoint
    """
    if not domain:
        raise ApiError("Domain is missing!")

    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    url = url["base"] + domain + final_keys

    return url