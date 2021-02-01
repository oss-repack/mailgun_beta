"""
EMAIL VALIDATION HANDLER
"""
from os import path
from urllib.parse import urljoin, quote
from .error_handler import ApiError


def handle_address_validate(url,domain,method,**kwargs):
    """
    Handle email validation
    :param url: Incoming URL dictionary
    :param domain: Incoming domain
    :param method: Incoming request method
    :param kwargs: kwargs
    :return: final url for email validation endpoint
    """
    final_keys = path.join("/", *url["keys"][1:]) if url["keys"][1:] else ""
    if "list_name" in kwargs:
        url = url["base"] + final_keys + "/" + kwargs["list_name"]
    else:
        url = url["base"] + final_keys

    return url