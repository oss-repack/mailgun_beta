"""
INBOX PLACEMENT HANDLER
"""
from os import path
from urllib.parse import urljoin, quote
from .error_handler import ApiError


def handle_inbox(url,domain,method,**kwargs):
    """
    Handle inbox placement
    :param url: Incoming URL dictionary
    :param domain: Incoming domain
    :param method: Incoming request method
    :param kwargs: kwargs
    :return: final url for inbox placement endpoint
    """
    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    if "test_id" in kwargs:
        if "counters" in kwargs:
            if kwargs["counters"]:
                url = url["base"][:-1] + final_keys + "/" + kwargs["test_id"] + "/counters"
            else:
                raise ApiError("Counters option should be True or absent")
        elif "checks" in kwargs:
            if kwargs["checks"]:
                if "address" in kwargs:
                    url = url["base"][:-1] + final_keys + "/" + \
                          kwargs["test_id"] + "/checks/" + kwargs["address"]
                else:
                    url = url["base"][:-1] + final_keys + "/" + kwargs["test_id"] + "/checks"
            else:
                raise ApiError("Checks option should be True or absent")
        else:
            url = url["base"][:-1] + final_keys + "/" + kwargs["test_id"]
    else:
        url = url["base"][:-1] + final_keys

    return url