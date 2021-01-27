"""
IPS HANDLER
"""
from urllib.parse import urljoin
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


def handle_ips(url,domain,method,**kwargs):
    final_keys = convert_keys(url["keys"])
    if "ip" in kwargs:
        url = url["base"][:-1] + final_keys + "/" + kwargs["ip"]
    else:
        url = url["base"][:-1] + final_keys

    return url