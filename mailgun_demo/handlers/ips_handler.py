"""
IPS HANDLER
"""
from os import path
from urllib.parse import urljoin
from .error_handler import ApiError


def handle_ips(url,domain,method,**kwargs):
    """
    Handle IPs
    :param url: Incoming URL dictionary
    :param domain: Incoming domain
    :param method: Incoming request method
    :param kwargs: kwargs
    :return: final url for IPs endpoint
    """
    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    if "ip" in kwargs:
        url = url["base"][:-1] + final_keys + "/" + kwargs["ip"]
    else:
        url = url["base"][:-1] + final_keys

    return url