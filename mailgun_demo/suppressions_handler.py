"""
IPS HANDLER
"""
from urllib.parse import urljoin, quote
from error_handler import ApiError


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


def handle_bounces(url,domain,method,**kwargs):
    final_keys = convert_keys(url["keys"])
    if "bounce_address" in kwargs:
        url = url["base"] + domain + final_keys + "/" + kwargs["bounce_address"]
    else:
        url = url["base"] + domain + final_keys

    return url


def handle_unsubscribes(url,domain,method,**kwargs):
    final_keys = convert_keys(url["keys"])
    if "unsubscribe_address" in kwargs:
        url = url["base"] + domain + final_keys + "/" + kwargs["unsubscribe_address"]
    else:
        url = url["base"] + domain + final_keys
    return url


def handle_complaints(url,domain,method,**kwargs):
    final_keys = convert_keys(url["keys"])
    if "complaint_address" in kwargs:
        url = url["base"] + domain + final_keys + "/" + kwargs["complaint_address"]
    else:
        url = url["base"] + domain + final_keys

    return url


def handle_whitelists(url,domain,method,**kwargs):
    final_keys = convert_keys(url["keys"])
    if "whitelist_address" in kwargs:
        url = url["base"] + domain + final_keys + "/" + kwargs["whitelist_address"]
    else:
        url = url["base"] + domain + final_keys

    return url