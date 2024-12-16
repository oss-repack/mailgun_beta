"""IP_POOLS HANDLER.

Doc: https://documentation.mailgun.com/en/latest/api-ip-pools.html
"""
from os import path


def handle_ippools(url, _domain, _method, **kwargs):
    """Handle IP pools.

    :param url: Incoming URL dictionary
    :type url: dict
    :param _domain: Incoming domain (it's not being used for this handler)
    :type _domain: str
    :param _method: Incoming request method (it's not being used for this handler)
    :type _method: str
    :param kwargs: kwargs
    :return: final url for IP pools endpoint
    """
    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    if "pool_id" in kwargs:
        url = url["base"][:-1] + final_keys + "/" + kwargs["pool_id"]
    else:
        url = url["base"][:-1] + final_keys

    return url
