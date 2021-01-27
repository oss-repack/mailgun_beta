"""
IPS HANDLER
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


def handle_tags(url,domain,method,**kwargs):

    final_keys = convert_keys(url["keys"])
    base = url["base"] + domain + "/"
    keys_without_tags = url["keys"][1:]
    url = url["base"] + domain + final_keys
    if "tag_name" in kwargs:
        if "stats" in final_keys:
            final_keys = convert_keys(keys_without_tags)
            url = base + "tags" + "/" + quote(kwargs["tag_name"]) + final_keys
        else:
            url = url + "/" + quote(kwargs["tag_name"])

    return url