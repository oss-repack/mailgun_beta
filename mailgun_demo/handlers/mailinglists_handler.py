"""
MAILING LISTS HANDLER
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


def handle_lists(url,domain,method,**kwargs):
    final_keys = convert_keys(url["keys"])
    if "validate" in kwargs:
        url = url["base"][:-1] + final_keys + "/" + kwargs["address"] + "/" + "validate"
    elif "multiple" in kwargs and "address" in kwargs:
        if kwargs["multiple"]:
            url = url["base"][:-1] + "/lists/" + kwargs["address"] + "/members.json"
    elif "members" in final_keys and "address" in kwargs:
        members_keys = convert_keys(url["keys"][1:])
        if "member_address" in kwargs:
            url = url["base"][:-1] + "/lists/" + kwargs["address"] + members_keys + \
                  "/" + kwargs["member_address"]
        else:
            url = url["base"][:-1] + "/lists/" + kwargs["address"] + members_keys
    elif "address" in kwargs and not "validate" in kwargs:
        url = url["base"][:-1] + final_keys + "/" + kwargs["address"]

    else:
        url = url["base"][:-1] + final_keys

    return url