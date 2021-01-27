"""
DOMAINS HANDLER
"""
from urllib.parse import urljoin
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


def handle_domainlist(url,domain,method,**kwargs):
    """

    :param url: Incoming URL dictionary
    :param domain: Incoming domain
    :param method: Incoming request method
    :param kwargs: kwargs
    :return: final url for domainlist endpoint
    """
    return url["base"] + "domains"


def handle_domains(url,domain,method,**kwargs):
    """

    :param url: Incoming URL dictionary
    :param domain: Incoming domain
    :param method: Incoming request method
    :param kwargs: kwargs
    :return: final url for domain endpoint
    """
    if "domains" in url["keys"]:
        domains_index = url["keys"].index("domains")
        url["keys"].pop(domains_index)
    if url["keys"]:
        final_keys = convert_keys(url["keys"])
        if not domain:
            raise ApiError("Domain is missing!")
        if "login" in kwargs:
            url = urljoin(url["base"], domain + final_keys + "/" + kwargs["login"])
        elif "ip" in kwargs:
            url = urljoin(url["base"], domain + final_keys + "/" + kwargs["ip"])
        elif "unlink_pool" in kwargs:
            url = urljoin(url["base"], domain + final_keys + "/ip_pool")
        elif "api_storage_url" in kwargs:
            url = kwargs["api_storage_url"]
        else:
            url = urljoin(url["base"], domain + final_keys)
    else:
        if method in ["get", "post", "delete"]:
            if method == "delete":
                url = urljoin(url["base"], domain)
            else:
                url = url["base"][:-1]
        else:
            url = urljoin(url["base"], domain)
    return url