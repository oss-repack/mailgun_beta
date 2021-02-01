"""
ROUTES HANDLER
"""
from os import path
from urllib.parse import urljoin, quote
from .error_handler import ApiError


def handle_routes(url,domain,method,**kwargs):
    """
    Handle Routes
    :param url: Incoming URL dictionary
    :param domain: Incoming domain
    :param method: Incoming request method
    :param kwargs: kwargs
    :return: final url for Routes endpoint
    """
    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    if "route_id" in kwargs:
        url = url["base"][:-1] + final_keys + "/" + kwargs["route_id"]
    else:
        url = url["base"][:-1] + final_keys

    return url