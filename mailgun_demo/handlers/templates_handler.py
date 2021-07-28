"""
TEMPLATES HANDLER
"""
from os import path
from .error_handler import ApiError


def handle_templates(url, domain, _method, **kwargs):
    """
    Handle Templates
    :param url: Incoming URL dictionary
    :param domain: Incoming domain
    :param _method: Incoming request method (but not used here)
    :param kwargs: kwargs
    :return: final url for Templates endpoint
    """
    final_keys = path.join("/", *url["keys"]) if url["keys"] else ""
    if "template_name" in kwargs:
        if "versions" in kwargs:
            if kwargs["versions"]:
                if "tag" in kwargs:
                    url = url["base"] + domain + final_keys + "/" + \
                          kwargs["template_name"] + "/versions/" + kwargs["tag"]
                else:
                    url = url["base"] + domain + final_keys + "/" + kwargs["template_name"] + "/versions"
            else:
                raise ApiError("Versions should be True or absent")
        else:
            url = url["base"] + domain + final_keys + "/" + kwargs["template_name"]
    else:
        url = url["base"] + domain + final_keys

    return url
