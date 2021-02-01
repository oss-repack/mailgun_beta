"""
IP_POOLS HANDLER
"""
from os import path
from urllib.parse import urljoin
from .error_handler import ApiError


def handle_ippools(url,domain,method,**kwargs):
    """
    Handle IP pools
    :param url: Incoming URL dictionary
    :param domain: Incoming domain
    :param method: Incoming request method
    :param kwargs: kwargs
    :return: final url for IP pools endpoint
    """

    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    if "pool_id" in kwargs:
        url = url["base"][:-1] + final_keys + "/" + kwargs["pool_id"]
    else:
        url = url["base"][:-1] + final_keys

    return url