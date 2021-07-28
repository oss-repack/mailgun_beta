"""
EMAIL VALIDATION HANDLER
"""
from os import path


def handle_address_validate(url, _domain, _method, **kwargs):
    """
    Handle email validation
    :param url: Incoming URL dictionary
    :param _domain: Incoming domain
    :param _method: Incoming request method
    :param kwargs: kwargs
    :return: final url for email validation endpoint
    """
    final_keys = path.join("/", *url["keys"][1:]) if url["keys"][1:] else ""
    if "list_name" in kwargs:
        url = url["base"] + final_keys + "/" + kwargs["list_name"]
    else:
        url = url["base"] + final_keys

    return url
