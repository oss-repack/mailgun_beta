"""
TEMPLATES HANDLER
"""
from urllib.parse import urljoin, quote
from .error_handler import ApiError


def convert_keys(keys):
    """
    Generate path base on incoming keys
    :param keys: url keys
    :return: part of url path
    """
    final_keys = ""
    if len(keys) == 1:
        final_keys = "/" + keys[0]
    else:
        for k in keys:
            final_keys += "/" + k

    return final_keys


def handle_inbox(url,domain,method,**kwargs):
    final_keys = convert_keys(url["keys"])
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