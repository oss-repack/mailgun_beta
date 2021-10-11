import os
from mailgun_demo.client import Client

key = os.environ["APIKEY"]
domain = os.environ["DOMAIN"]

client = Client(auth=("api", key))

def get_single_validate():
    """
    GET /v4/address/validate
    :return:
    """
    params = {"address": "test@gmail.com",
              "provider_lookup": "false"}
    req = client.addressvalidate.get(domain=domain, filters=params)
    print(req.json())


def post_single_validate():
    """
    POST /v4/address/validate
    :return:
    """
    data = {"address": "diskovodik@gmail.com"}
    params = {"provider_lookup": "false"}
    req = client.addressvalidate.create(domain=domain, data=data, filters=params)
    print(req.json())


def get_bulk_validate():
    """
    GET /v4/address/validate/bulk
    :return:
    """
    params = {"limit": 2}
    req = client.addressvalidate_bulk.get(domain=domain, filters=params)
    print(req.json())


def post_bulk_list_validate():
    """
    POST /v4/address/validate/bulk/<list_id>
    :return:
    """
    files = {'file': open('../doc_tests/files/email_validation.csv', 'rb')}
    req = client.addressvalidate_bulk.create(domain=domain, files=files, list_name="python2_list")
    print(req.json())


def get_bulk_list_validate():
    """
    GET /v4/address/validate/bulk/<list_id>
    :return:
    """
    req = client.addressvalidate_bulk.get(domain=domain, list_name="python2_list")
    print(req.json())

def delete_bulk_list_validate():
    """
    DELETE /v4/address/validate/bulk/<list_id>
    :return:
    """
    req = client.addressvalidate_bulk.delete(domain=domain, list_name="python2_list")
    print(req.json())


def get_preview():
    """
    GET /v4/address/validate/preview
    :return:
    """
    req = client.addressvalidate_preview.get(domain=domain)
    print(req.json())


def post_preview():
    """
    POST /v4/address/validate/preview/<list_id>
    :return:
    """
    files = {'file': open('../doc_tests/files/email_previews.csv', 'rb')}
    req = client.addressvalidate_preview.create(domain=domain,
                                             files=files,
                                             list_name="python_list")
    print(req.json())


def delete_preview():
    """
    DELETE /v4/address/validate/preview/<list_id>
    :return:
    """
    req = client.addressvalidate_preview.delete(domain=domain, list_name="python_list")
    print(req.text)


if __name__ == '__main__':
    delete_preview()
