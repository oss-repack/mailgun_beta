"""
DOMAINS HANDLER
"""
from os import path
from urllib.parse import urljoin
from .error_handler import ApiError


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
        final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
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
            if "domain_name" in kwargs:
                url = urljoin(url["base"], kwargs["domain_name"])
            elif method == "delete":
                url = urljoin(url["base"], domain)
            else:
                url = url["base"][:-1]
        else:
            if "verify" in kwargs:
                if kwargs["verify"] is not True:
                    raise ApiError("Verify option should be True or absent")
                url = url["base"] + domain + "/verify"
            else:
                url = urljoin(url["base"], domain)

    return url