"""IPS HANDLER.

Doc: https://documentation.mailgun.com/en/latest/api-ips.html
"""

from os import path


def handle_ips(url, _domain, _method, **kwargs):
    """Handle IPs.

    :param url: Incoming URL dictionary
    :type url: dict
    :param _domain: Incoming domain (it's not being used for this handler)
    :type _domain: str
    :param _method: Incoming request method (it's not being used for this handler)
    :type _method: str
    :param kwargs: kwargs
    :return: final url for IPs endpoint
    """
    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    if "ip" in kwargs:
        url = url["base"][:-1] + final_keys + "/" + kwargs["ip"]
    else:
        url = url["base"][:-1] + final_keys

    return url
