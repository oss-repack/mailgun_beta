"""SUPPRESSION HANDLER.

Doc: https://documentation.mailgun.com/en/latest/api-suppressions.html
"""

from os import path


def handle_bounces(url, domain, _method, **kwargs):
    """Handle Bounces.

    :param url: Incoming URL dictionary
    :type url: dict
    :param domain: Incoming domain
    :type domain: str
    :param _method: Incoming request method (it's not being used for this handler)
    :type _method: str
    :param kwargs: kwargs
    :return: final url for Bounces endpoint
    """
    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    if "bounce_address" in kwargs:
        url = url["base"] + domain + final_keys + "/" + kwargs["bounce_address"]
    else:
        url = url["base"] + domain + final_keys
    return url


def handle_unsubscribes(url, domain, _method, **kwargs):
    """Handle Unsubscribes.

    :param url: Incoming URL dictionary
    :type url: dict
    :param domain: Incoming domain
    :type domain: str
    :param _method: Incoming request method (it's not being used for this handler)
    :type _method: str
    :param kwargs: kwargs
    :return: final url for Unsubscribes endpoint
    """
    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    if "unsubscribe_address" in kwargs:
        url = url["base"] + domain + final_keys + "/" + kwargs["unsubscribe_address"]
    else:
        url = url["base"] + domain + final_keys
    return url


def handle_complaints(url, domain, _method, **kwargs):
    """Handle Complaints.

    :param url: Incoming URL dictionary
    :type url: dict
    :param domain: Incoming domain
    :type domain: str
    :param _method: Incoming request method (it's not being used for this handler)
    :type _method: str
    :param kwargs: kwargs
    :return: final url for Complaints endpoint
    """
    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    if "complaint_address" in kwargs:
        url = url["base"] + domain + final_keys + "/" + kwargs["complaint_address"]
    else:
        url = url["base"] + domain + final_keys
    return url


def handle_whitelists(url, domain, _method, **kwargs):
    """Handle Whitelists.

    :param url: Incoming URL dictionary
    :type url: dict
    :param domain: Incoming domain
    :type domain: str
    :param _method: Incoming request method (it's not being used for this handler)
    :type _method: str
    :param kwargs: kwargs
    :return: final url for Whitelists endpoint
    """
    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    if "whitelist_address" in kwargs:
        url = url["base"] + domain + final_keys + "/" + kwargs["whitelist_address"]
    else:
        url = url["base"] + domain + final_keys

    return url
