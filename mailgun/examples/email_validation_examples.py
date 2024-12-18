import os

from mailgun.client import Client


key: str = os.environ["APIKEY"]
domain: str = os.environ["DOMAIN"]

client: Client = Client(auth=("api", key))


def get_single_validate() -> None:
    """
    GET /v4/address/validate
    :return:
    """
    params = {"address": "test@gmail.com", "provider_lookup": "false"}
    req = client.addressvalidate.get(domain=domain, filters=params)
    print(req.json())


def post_single_validate() -> None:
    """
    POST /v4/address/validate
    :return:
    """
    data = {"address": "diskovodik@gmail.com"}
    params = {"provider_lookup": "false"}
    req = client.addressvalidate.create(domain=domain, data=data, filters=params)
    print(req.json())


def get_bulk_validate() -> None:
    """
    GET /v4/address/validate/bulk
    :return:
    """
    params = {"limit": 2}
    req = client.addressvalidate_bulk.get(domain=domain, filters=params)
    print(req.json())


def post_bulk_list_validate() -> None:
    """
    POST /v4/address/validate/bulk/<list_id>
    :return:
    """
    # TODO: Refactor this by using with context manager or pathlib.Path
    files = {"file": open("../doc_tests/files/email_validation.csv", "rb")}
    req = client.addressvalidate_bulk.create(
        domain=domain, files=files, list_name="python2_list"
    )
    print(req.json())


def get_bulk_list_validate() -> None:
    """
    GET /v4/address/validate/bulk/<list_id>
    :return:
    """
    req = client.addressvalidate_bulk.get(domain=domain, list_name="python2_list")
    print(req.json())


def delete_bulk_list_validate() -> None:
    """
    DELETE /v4/address/validate/bulk/<list_id>
    :return:
    """
    req = client.addressvalidate_bulk.delete(domain=domain, list_name="python2_list")
    print(req.json())


def get_preview() -> None:
    """
    GET /v4/address/validate/preview
    :return:
    """
    req = client.addressvalidate_preview.get(domain=domain)
    print(req.json())


def post_preview() -> None:
    """
    POST /v4/address/validate/preview/<list_id>
    :return:
    """
    # TODO: Refactor this by using with context manager or pathlib.Path
    files = {"file": open("../doc_tests/files/email_previews.csv", "rb")}
    req = client.addressvalidate_preview.create(
        domain=domain, files=files, list_name="python_list"
    )
    print(req.json())


def delete_preview() -> None:
    """
    DELETE /v4/address/validate/preview/<list_id>
    :return:
    """
    req = client.addressvalidate_preview.delete(domain=domain, list_name="python_list")
    print(req.text)


if __name__ == "__main__":
    delete_preview()
