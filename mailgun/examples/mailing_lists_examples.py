import os

from mailgun.client import Client


key: str = os.environ["APIKEY"]
domain: str = os.environ["DOMAIN"]

client: Client = Client(auth=("api", key))


def get_pages() -> None:
    """
    GET /lists/pages
    :return:
    """
    req = client.lists_pages.get(domain=domain)
    print(req.json())


def get_lists_address() -> None:
    """
    GET /lists/<address>
    :return:
    """
    req = client.lists.get(domain=domain, address="everyone@mailgun.zeefarmer.com")
    print(req.json())


def post_lists() -> None:
    """
    POST /lists
    :return:
    """
    data = {
        "address": f"python_sdk2@{domain}",
        "description": "Mailgun developers list",
    }

    req = client.lists.create(domain=domain, data=data)
    print(req.json())


def put_lists() -> None:
    """
    PUT /lists/<address>
    :return:
    """
    data = {"description": "Mailgun developers list 121212"}

    req = client.lists.put(domain=domain, data=data, address=f"python_sdk2@{domain}")
    print(req.json())


def post_address_validate() -> None:
    """
    POST /lists/<address>/validate
    :return:
    """
    req = client.lists.create(
        domain=domain, address=f"python_sdk2@{domain}", validate=True
    )
    print(req.json())


def get_validate_address() -> None:
    """
    GET /lists/<address>/validate
    :return:
    """
    req = client.lists.get(
        domain=domain, address=f"python_sdk2@{domain}", validate=True
    )
    print(req.json())


def delete_validate_job() -> None:
    """
    DELETE /lists/<address>/validate
    :return:
    """
    req = client.lists.delete(
        domain=domain, address=f"python_sdk2@{domain}", validate=True
    )
    print(req.json())


def get_lists_members() -> None:
    """
    GET /lists/<address>/members/pages
    :return:
    """
    req = client.lists_members_pages.get(
        domain=domain, address="everyone@mailgun.zeefarmer.com"
    )
    print(req.json())


def get_member_from_list() -> None:
    """
    GET /lists/<address>/members/<member_address>
    :return:
    """
    req = client.lists_members.get(
        domain=domain,
        address="everyone@mailgun.zeefarmer.com",
        member_address="zerreissen@hotmail.com",
    )

    print(req.json())


def post_member_list() -> None:
    """
    POST /lists/<address>/members
    :return:
    """
    data = {
        "subscribed": True,
        "address": "bar2@example.com",
        "name": "Bob Bar",
        "description": "Developer",
        "vars": '{"age": 26}',
    }
    req = client.lists_members.create(
        domain=domain, address="everyone@mailgun.zeefarmer.com", data=data
    )
    print(req.json())


def put_member_list() -> None:
    """
    PUT /lists/<address>/members/<member_address>
    :return:
    """
    data = {
        "subscribed": True,
        "address": "bar2@example.com",
        "name": "Bob Bar 2",
        "description": "Developer",
        "vars": '{"age": 28}',
    }

    req = client.lists_members.put(
        domain=domain,
        address="everyone@mailgun.zeefarmer.com",
        data=data,
        member_address="bar2@example.com",
    )

    print(req.json())


def post_members_json() -> None:
    """
    POST /lists/<address>/members.json
    :return:
    """
    data = {
        "upsert": True,
        "members": '[{"address": "Alice <alice@example.com>", "vars": {"age": 26}},'
        '{"name": "Bob", "address": "bob2@example.com", "vars": {"age": 34}}]',
    }

    req = client.lists_members.create(
        domain=domain,
        address="everyone@mailgun.zeefarmer.com",
        data=data,
        multiple=True,
    )
    print(req.json())


def delete_members_list() -> None:
    """
    DELETE /lists/<address>/members/<member_address>
    :return:
    """
    req = client.lists_members.delete(
        domain=domain,
        address="everyone@mailgun.zeefarmer.com",
        member_address="bob2@example.com",
    )
    print(req.json())


def delete_lists_address() -> None:
    """
    DELETE /lists/<address>
    :return:
    """
    req = client.lists.delete(domain=domain, address=f"python_sdk@{domain}")
    print(req.json())


if __name__ == "__main__":
    delete_lists_address()
