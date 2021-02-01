"""
MAILING LISTS HANDLER
"""
from os import path
from urllib.parse import urljoin, quote
from .error_handler import ApiError


def handle_lists(url,domain,method,**kwargs):
    """
    Handle Mailing List
    :param url: Incoming URL dictionary
    :param domain: Incoming domain
    :param method: Incoming request method
    :param kwargs: kwargs
    :return: final url for mailinglist endpoint
    """
    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    if "validate" in kwargs:
        url = url["base"][:-1] + final_keys + "/" + kwargs["address"] + "/" + "validate"
    elif "multiple" in kwargs and "address" in kwargs:
        if kwargs["multiple"]:
            url = url["base"][:-1] + "/lists/" + kwargs["address"] + "/members.json"
    elif "members" in final_keys and "address" in kwargs:
        members_keys = path.join("/", *url["keys"][1:]) if url["keys"][1:] else ""
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