"""RESEND MESSAGE HANDLER.

Doc: https://documentation.mailgun.com/en/latest/api-sending.html#
"""

from .error_handler import ApiError


def handle_resend_message(_url, _domain, _method, **kwargs):
    """Resend message endpoint.

    :param _url: Incoming URL dictionary (it's not being used for this handler)
    :type _url: dict
    :param _domain: Incoming domain (it's not being used for this handler)
    :type _domain: str
    :param _method: Incoming request method (it's not being used for this handler)
    :type _method: str
    :param kwargs: kwargs
    :return: final url for default endpoint
    """
    if "storage_url" in kwargs:
        return kwargs["storage_url"]
    ApiError("Storage url is required")
    return None
