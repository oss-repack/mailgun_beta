"""
SUPPRESSION HANDLER
"""
from os import path
from urllib.parse import urljoin, quote
from .error_handler import ApiError


def handle_bounces(url,domain,method,**kwargs):
    """
    Handle Bounces
    :param url: Incoming URL dictionary
    :param domain: Incoming domain
    :param method: Incoming request method
    :param kwargs: kwargs
    :return: final url for Bounces endpoint
    """
    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    if "bounce_address" in kwargs:
        url = url["base"] + domain + final_keys + "/" + kwargs["bounce_address"]
    else:
        url = url["base"] + domain + final_keys
    return url


def handle_unsubscribes(url,domain,method,**kwargs):
    """
    Handle Unsubscribes
    :param url: Incoming URL dictionary
    :param domain: Incoming domain
    :param method: Incoming request method
    :param kwargs: kwargs
    :return: final url for Unsubscribes endpoint
    """
    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    if "unsubscribe_address" in kwargs:
        url = url["base"] + domain + final_keys + "/" + kwargs["unsubscribe_address"]
    else:
        url = url["base"] + domain + final_keys
    return url


def handle_complaints(url,domain,method,**kwargs):
    """
    Handle Complaints
    :param url: Incoming URL dictionary
    :param domain: Incoming domain
    :param method: Incoming request method
    :param kwargs: kwargs
    :return: final url for Complaints endpoint
    """
    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    if "complaint_address" in kwargs:
        url = url["base"] + domain + final_keys + "/" + kwargs["complaint_address"]
    else:
        url = url["base"] + domain + final_keys
    return url


def handle_whitelists(url,domain,method,**kwargs):
    """
    Handle Whitelists
    :param url: Incoming URL dictionary
    :param domain: Incoming domain
    :param method: Incoming request method
    :param kwargs: kwargs
    :return: final url for Whitelists endpoint
    """
    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    if "whitelist_address" in kwargs:
        url = url["base"] + domain + final_keys + "/" + kwargs["whitelist_address"]
    else:
        url = url["base"] + domain + final_keys

    return url