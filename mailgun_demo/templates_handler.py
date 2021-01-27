"""
TEMPLATES HANDLER
"""
from urllib.parse import urljoin, quote
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


def handle_templates(url,domain,method,**kwargs):
    final_keys = convert_keys(url["keys"])
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