import os
from mailgun_demo.client import Client

key = os.environ["APIKEY"]
domain = os.environ["DOMAIN"]

client = Client(auth=("api", key))

# Bounces
def get_bounces():
    """
    GET /<domain>/bounces
    :return:
    """
    req = client.bounces.get(domain=domain)
    print(req.json())

def post_bounces():
    """
    POST /<domain>/bounces
    :return:
    """
    data = {
        "address": "test120@gmail.com",
        "code": 550,
        "error": "Test error"
    }
    req = client.bounces.create(data=data, domain=domain)
    print(req.json())

def get_single_bounce():
    """
    GET /<domain>/bounces/<address>
    :return:
    """
    req = client.bounces.get(domain=domain, bounce_address="test120@gmail.com")
    print(req.json())

def add_multiple_bounces():
    """
    POST /<domain>/bounces, Content-Type: application/json
    :return:
    """
    data = [{
        "address": "test121@i.ua",
        "code": "550",
        "error": "Test error2312"
    },
        {
            "address": "test122@gmail.com",
            "code": "550",
            "error": "Test error"
        }]
    req = client.bounces.create(data=data, domain=domain, headers='application/json')
    print(req.json())

def import_bounce_list():
    """
    POST /<domain>/bounces/import, Content-Type: multipart/form-data
    :return:
    """
    files = {"bounce_csv": open("../doc_tests/files/mailgun_bounces_test.csv", "rb")}
    req = client.bounces_import.create(domain=domain, files=files)
    print(req.json())

def delete_single_bounce():
    """
    DELETE /<domain>/bounces/<address>
    :return:
    """
    req = client.bounces.delete(domain=domain, bounce_address="test122@gmail.com")
    print(req.json())

def delete_bounce_list():
    """
    DELETE /<domain>/bounces
    :return:
    """
    req = client.bounces.delete(domain=domain)
    print(req.json())

# Unsubscribes
def get_unsubs():
    """
    GET /<domain>/unsubscribes
    :return:
    """
    req = client.unsubscribes.get(domain=domain)
    print(req.json())

def get_single_unsub():
    """
    GET /<domain>/unsubscribes/<address>
    :return:
    """
    req = client.unsubscribes.get(domain=domain, unsubscribe_address="test1@gmail.com")
    print(req.json())

def create_single_unsub():
    """
    POST /<domain>/unsubscribes
    :return:
    """
    data = {'address':'bob@example.com',
            'tag': '*'}
    req = client.unsubscribes.create(data=data, domain=domain)
    print(req.json())

def create_multiple_unsub():
    """
    POST /<domain>/unsubscribes, Content-Type: application/json
    :return:
    """
    data = [
        {
            "address": "alice@example.com",
            "tags": ["some tag"],
            "created_at": "Thu, 13 Oct 2011 18:02:00 UTC"
        },
        {
            "address": "bob@example.com",
            "tags": ["*"],
        },
        {
            "address": "carol@example.com"
        }
    ]

    req = client.unsubscribes.create(data=data, domain=domain,
                                     headers='application/json')
    print(req.json())

def import_list_unsubs():
    """
    POST /<domain>/unsubscribes/import, Content-Type: multipart/form-data
    :return:
    """
    files = {"unsubscribe2_csv": open("../doc_tests/files/mailgun_unsubscribes.csv", "rb")}
    req = client.unsubscribes_import.create(domain=domain, files=files)
    print(req.json())

def delete_single_unsub():
    """
    DELETE /<domain>/unsubscribes/<address>
    :return:
    """
    req = client.unsubscribes.delete(domain=domain, unsubscribe_address="alice@example.com")
    print(req.json())

def delete_all_unsubs():
    """
    DELETE /<domain>/unsubscribes/
    :return:
    """
    req = client.unsubscribes.delete(domain=domain)
    print(req.json())

# Complaints

def get_complaints():
    """
    GET /<domain>/complaints

    :return:
    """
    req = client.complaints.get(domain=domain)
    print(req.json())

def add_complaints():
    """
    POST /<domain>/complaints
    :return:
    """
    data = {
        "address": "bob@gmail.com",
        "tag": "compl_test_tag"
    }
    req = client.complaints.create(data=data, domain=domain)
    print(req.json())

def add_multiple_complaints():
    """
    POST /<domain>/complaints, Content-Type: application/json
    :return:
    """
    data = [
        {
            "address": "alice1@example.com",
            "tags": ["some tag"],
            "created_at": "Thu, 13 Oct 2011 18:02:00 UTC"
        },
        {
            "address": "carol1@example.com"
        }
    ]

    req = client.complaints.create(data=data, domain=domain, headers='application/json')
    print(req.json())

def import_complaint_list():
    """
    POST /<domain>/complaints/import, Content-Type: multipart/form-data
    :return:
    """
    files = {"complaints_csv": open("../doc_tests/files/mailgun_complaints.csv", "rb")}
    req = client.complaints_import.create(domain=domain, files=files)
    print(req.json())

def delete_single_complaint():
    """
    DELETE /<domain>/complaints/<address>
    :return:
    """
    req = client.complaints.delete(domain=domain, complaint_address="carol1@example.com")
    print(req.json())

def delete_all_complaints():
    """
    DELETE /<domain>/complaints/
    :return:
    """
    req = client.complaints.delete(domain=domain)
    print(req.json())

# Whitelists

def get_whitelists():
    """
    GET /<domain>/whitelists
    :return:
    """
    req = client.whitelists.get(domain=domain)
    print(req.json())

def create_whitelist():
    """
    POST /<domain>/whitelists
    :return:
    """
    data = {
        "address": "bob@gmail.com",
        "tag": "whitel_test"
    }
    req = client.whitelists.create(data=data, domain=domain)
    print(req.json())

def get_single_whitelist():
    """
    GET /<domain>/whitelists/<address or domain>
    :return:
    """
    # You can set domain name or address for whitelist_address option
    req = client.whitelists.get(domain=domain, whitelist_address="bob@gmail.com")
    print(req.json())

def import_list_whitelists():
    """
    POST /<domain>/whitelists/import, Content-Type: multipart/form-data
    :return:
    """
    files = {"whitelist_csv": open("../doc_tests/files/mailgun_whitelists.csv", "rb")}
    req = client.whitelists_import.create(domain=domain, files=files)
    print(req.json())

def delete_single_whitelist():
    """
    DELETE /<domain>/whitelists/<address or domain>
    :return:
    """
    req = client.whitelists.delete(domain=domain, whitelist_address="bob@gmail.com")
    print(req.json())

if __name__ == '__main__':
    delete_single_whitelist()

