from .error_handler import ApiError


def handle_resend_message(_url, _domain, _method, **kwargs):
    """
    Resend message endpoint
    :param _url: Incoming URL dictionary
    :param _domain: Incoming domain
    :param _method: Incoming request method (but it's not used for handle_default)
    :param kwargs: kwargs
    :return: final url for default endpoint
    """
    if "storage_url" in kwargs:
        return kwargs["storage_url"]
    else:
        ApiError("Storage url is required")
