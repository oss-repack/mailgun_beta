import os
from mailgun_demo.client import Client

key = os.environ["APIKEY"]
domain = os.environ["DOMAIN"]

client = Client(auth=("api", key))

def get_pages():
    """
    GET /lists/pages
    :return:
    """
    req = client.lists_pages.get(domain=domain)
    print(req.json())

def get_lists_address():
    """
    GET /lists/<address>
    :return:
    """
    req = client.lists.get(domain=domain, address="everyone@mailgun.zeefarmer.com")
    print(req.json())

def post_lists():
    """
    POST /lists
    :return:
    """
    data = {
        'address': 'python_sdk2@{domain}'.format(domain=domain),
        'description': "Mailgun developers list"}

    req = client.lists.create(domain=domain, data=data)
    print(req.json())

def put_lists():
    """
    PUT /lists/<address>
    :return:
    """
    data = {
        'description': "Mailgun developers list 121212"
    }

    req = client.lists.put(domain=domain, data=data, address='python_sdk2@{domain}'.format(domain=domain))
    print(req.json())


def post_address_validate():
    """
    POST /lists/<address>/validate
    :return:
    """
    req = client.lists.create(domain=domain,
                              address="python_sdk2@{domain}".format(domain=domain),
                              validate=True)
    print(req.json())

def get_validate_address():
    """
    GET /lists/<address>/validate
    :return:
    """
    req = client.lists.get(domain=domain,
                           address="python_sdk2@{domain}".format(domain=domain),
                           validate=True)
    print(req.json())


def delete_validate_job():
    """
    DELETE /lists/<address>/validate
    :return:
    """
    req = client.lists.delete(domain=domain,
                              address="python_sdk2@{domain}".format(domain=domain),
                              validate=True)
    print(req.json())


def get_lists_members():
    """
    GET /lists/<address>/members/pages
    :return:
    """
    req = client.lists_members_pages.get(domain=domain,
                                         address="everyone@mailgun.zeefarmer.com")
    print(req.json())


def get_member_from_list():
    """
    GET /lists/<address>/members/<member_address>
    :return:
    """
    req = client.lists_members.get(domain=domain, address="everyone@mailgun.zeefarmer.com",
                                   member_address="zerreissen@hotmail.com")

    print(req.json())


def post_member_list():
    """
    POST /lists/<address>/members
    :return:
    """
    data = {'subscribed': True,
            'address': 'bar2@example.com',
            'name': 'Bob Bar',
            'description': 'Developer',
            'vars': '{"age": 26}'}
    req = client.lists_members.create(domain=domain, address="everyone@mailgun.zeefarmer.com", data=data)
    print(req.json())

def put_member_list():
    """
    PUT /lists/<address>/members/<member_address>
    :return:
    """
    data = {'subscribed': True,
            'address': 'bar2@example.com',
            'name': 'Bob Bar 2',
            'description': 'Developer',
            'vars': '{"age": 28}'}

    req = client.lists_members.put(domain=domain, address="everyone@mailgun.zeefarmer.com", data=data,
                                   member_address="bar2@example.com")


    print(req.json())

def post_members_json():
    """
    POST /lists/<address>/members.json
    :return:
    """
    data = {'upsert': True,
            'members': '[{"address": "Alice <alice@example.com>", "vars": {"age": 26}},'
                       '{"name": "Bob", "address": "bob2@example.com", "vars": {"age": 34}}]'}

    req = client.lists_members.create(domain=domain, address="everyone@mailgun.zeefarmer.com", data=data, multiple=True)
    print(req.json())

def delete_members_list():
    """
    DELETE /lists/<address>/members/<member_address>
    :return:
    """
    req = client.lists_members.delete(domain=domain,
                                      address="everyone@mailgun.zeefarmer.com",
                                      member_address="bob2@example.com")
    print(req.json())


def delete_lists_address():
    """
    DELETE /lists/<address>
    :return:
    """
    req = client.lists.delete(domain=domain, address='python_sdk@{domain}'.format(domain=domain))
    print(req.json())



if __name__ == '__main__':
    delete_lists_address()

