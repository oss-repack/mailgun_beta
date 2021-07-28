"""
IPS HANDLER
"""
from os import path


def handle_ips(url, _domain, _method, **kwargs):
    """
    Handle IPs
    :param url: Incoming URL dictionary
    :param _domain: Incoming domain
    :param _method: Incoming request method
    :param kwargs: kwargs
    :return: final url for IPs endpoint
    """
    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    if "ip" in kwargs:
        url = url["base"][:-1] + final_keys + "/" + kwargs["ip"]
    else:
        url = url["base"][:-1] + final_keys

    return url
