import os

from mailgun.client import Client


key: str = os.environ["APIKEY"]
domain: str = os.environ["DOMAIN"]

client: Client = Client(auth=("api", key))

# Bounces


def get_bounces() -> None:
    """
    GET /<domain>/bounces
    :return:
    """
    req = client.bounces.get(domain=domain)
    print(req.json())


def post_bounces() -> None:
    """
    POST /<domain>/bounces
    :return:
    """
    data = {"address": "test120@gmail.com", "code": 550, "error": "Test error"}
    req = client.bounces.create(data=data, domain=domain)
    print(req.json())


def get_single_bounce() -> None:
    """
    GET /<domain>/bounces/<address>
    :return:
    """
    req = client.bounces.get(domain=domain, bounce_address="test120@gmail.com")
    print(req.json())


def add_multiple_bounces() -> None:
    """
    POST /<domain>/bounces, Content-Type: application/json
    :return:
    """
    data = [
        {"address": "test121@i.ua", "code": "550", "error": "Test error2312"},
        {"address": "test122@gmail.com", "code": "550", "error": "Test error"},
    ]
    req = client.bounces.create(data=data, domain=domain, headers="application/json")
    print(req.json())


def import_bounce_list() -> None:
    """
    POST /<domain>/bounces/import, Content-Type: multipart/form-data
    :return:
    """
    # TODO: Refactor this by using with context manager or pathlib.Path
    files = {"bounce_csv": open("../doc_tests/files/mailgun_bounces_test.csv", "rb")}
    req = client.bounces_import.create(domain=domain, files=files)
    print(req.json())


def delete_single_bounce() -> None:
    """
    DELETE /<domain>/bounces/<address>
    :return:
    """
    req = client.bounces.delete(domain=domain, bounce_address="test122@gmail.com")
    print(req.json())


def delete_bounce_list() -> None:
    """
    DELETE /<domain>/bounces
    :return:
    """
    req = client.bounces.delete(domain=domain)
    print(req.json())


# Unsubscribes


def get_unsubs() -> None:
    """
    GET /<domain>/unsubscribes
    :return:
    """
    req = client.unsubscribes.get(domain=domain)
    print(req.json())


def get_single_unsub() -> None:
    """
    GET /<domain>/unsubscribes/<address>
    :return:
    """
    req = client.unsubscribes.get(domain=domain, unsubscribe_address="test1@gmail.com")
    print(req.json())


def create_single_unsub() -> None:
    """
    POST /<domain>/unsubscribes
    :return:
    """
    data = {"address": "bob@example.com", "tag": "*"}
    req = client.unsubscribes.create(data=data, domain=domain)
    print(req.json())


def create_multiple_unsub() -> None:
    """
    POST /<domain>/unsubscribes, Content-Type: application/json
    :return:
    """
    data = [
        {
            "address": "alice@example.com",
            "tags": ["some tag"],
            "created_at": "Thu, 13 Oct 2011 18:02:00 UTC",
        },
        {
            "address": "bob@example.com",
            "tags": ["*"],
        },
        {"address": "carol@example.com"},
    ]

    req = client.unsubscribes.create(
        data=data, domain=domain, headers="application/json"
    )
    print(req.json())


def import_list_unsubs() -> None:
    """
    POST /<domain>/unsubscribes/import, Content-Type: multipart/form-data
    :return:
    """
    # TODO: Refactor this by using with context manager or pathlib.Path
    files = {
        "unsubscribe2_csv": open("../doc_tests/files/mailgun_unsubscribes.csv", "rb")
    }
    req = client.unsubscribes_import.create(domain=domain, files=files)
    print(req.json())


def delete_single_unsub() -> None:
    """
    DELETE /<domain>/unsubscribes/<address>
    :return:
    """
    req = client.unsubscribes.delete(
        domain=domain, unsubscribe_address="alice@example.com"
    )
    print(req.json())


def delete_all_unsubs() -> None:
    """
    DELETE /<domain>/unsubscribes/
    :return:
    """
    req = client.unsubscribes.delete(domain=domain)
    print(req.json())


# Complaints


def get_complaints() -> None:
    """
    GET /<domain>/complaints

    :return:
    """
    req = client.complaints.get(domain=domain)
    print(req.json())


def add_complaints() -> None:
    """
    POST /<domain>/complaints
    :return:
    """
    data = {"address": "bob@gmail.com", "tag": "compl_test_tag"}
    req = client.complaints.create(data=data, domain=domain)
    print(req.json())


def add_multiple_complaints() -> None:
    """
    POST /<domain>/complaints, Content-Type: application/json
    :return:
    """
    data = [
        {
            "address": "alice1@example.com",
            "tags": ["some tag"],
            "created_at": "Thu, 13 Oct 2011 18:02:00 UTC",
        },
        {"address": "carol1@example.com"},
    ]

    req = client.complaints.create(data=data, domain=domain, headers="application/json")
    print(req.json())


def import_complaint_list() -> None:
    """
    POST /<domain>/complaints/import, Content-Type: multipart/form-data
    :return:
    """
    # TODO: Refactor this by using with context manager or pathlib.Path
    files = {"complaints_csv": open("../doc_tests/files/mailgun_complaints.csv", "rb")}
    req = client.complaints_import.create(domain=domain, files=files)
    print(req.json())


def delete_single_complaint() -> None:
    """
    DELETE /<domain>/complaints/<address>
    :return:
    """
    req = client.complaints.delete(
        domain=domain, complaint_address="carol1@example.com"
    )
    print(req.json())


def delete_all_complaints() -> None:
    """
    DELETE /<domain>/complaints/
    :return:
    """
    req = client.complaints.delete(domain=domain)
    print(req.json())


# Whitelists


def get_whitelists() -> None:
    """
    GET /<domain>/whitelists
    :return:
    """
    req = client.whitelists.get(domain=domain)
    print(req.json())


def create_whitelist() -> None:
    """
    POST /<domain>/whitelists
    :return:
    """
    data = {"address": "bob@gmail.com", "tag": "whitel_test"}
    req = client.whitelists.create(data=data, domain=domain)
    print(req.json())


def get_single_whitelist() -> None:
    """
    GET /<domain>/whitelists/<address or domain>
    :return:
    """
    # You can set domain name or address for whitelist_address option
    req = client.whitelists.get(domain=domain, whitelist_address="bob@gmail.com")
    print(req.json())


def import_list_whitelists() -> None:
    """
    POST /<domain>/whitelists/import, Content-Type: multipart/form-data
    :return:
    """
    # TODO: Refactor this by using with context manager or pathlib.Path
    files = {"whitelist_csv": open("../doc_tests/files/mailgun_whitelists.csv", "rb")}
    req = client.whitelists_import.create(domain=domain, files=files)
    print(req.json())


def delete_single_whitelist() -> None:
    """
    DELETE /<domain>/whitelists/<address or domain>
    :return:
    """
    req = client.whitelists.delete(domain=domain, whitelist_address="bob@gmail.com")
    print(req.json())


if __name__ == "__main__":
    delete_single_whitelist()
