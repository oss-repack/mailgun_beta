from error_handler import ApiError


def handle_resend_message(url,domain,method,**kwargs):
    if "storage_url" in kwargs:
        return kwargs["storage_url"]
    else:
        ApiError("Storage url is required")