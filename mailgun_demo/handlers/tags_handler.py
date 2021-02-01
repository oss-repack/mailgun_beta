"""
TAGS HANDLER
"""
from os import path
from urllib.parse import urljoin, quote
from .error_handler import ApiError


def handle_tags(url,domain,method,**kwargs):
    """
    Handle Tags
    :param url: Incoming URL dictionary
    :param domain: Incoming domain
    :param method: Incoming request method
    :param kwargs: kwargs
    :return: final url for Tags endpoint
    """

    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    base = url["base"] + domain + "/"
    keys_without_tags = url["keys"][1:]
    url = url["base"] + domain + final_keys
    if "tag_name" in kwargs:
        if "stats" in final_keys:
            final_keys = path.join("/", *keys_without_tags) if keys_without_tags else ""
            url = base + "tags" + "/" + quote(kwargs["tag_name"]) + final_keys
        else:
            url = url + "/" + quote(kwargs["tag_name"])

    return url