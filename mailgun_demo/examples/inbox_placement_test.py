from client import Client

if __name__ == '__main__':
    key = "key-578f9790b7d06fd46a104f8156ed6995"
    domain = "2048.zeefarmer.com"
    client = Client(auth=("api", key))


    data = {
        'domain': 'domain.com',
        'from': 'user@sending_domain.com',
        'subject': 'testSubject',
        'html': '<html>HTML version of the body</html>' }

    req = client.inbox_tests.create(domain=domain, data=data)
    print(req.json())

    req = client.inbox_tests.get(domain=domain)
    print(req.json())

    req = client.inbox_tests.get(domain=domain, test_id="5fec3dc06339a2223bb46a48")
    print(req.json())

    req = client.inbox_tests.delete(domain=domain, test_id="5fec3dc06339a2223bb46a48")
    print(req.json())

    req = client.inbox_tests.get(domain=domain, test_id="5fec3dc06339a2223bb46a48", counters=True)
    print(req.json())

    req = client.inbox_tests.get(domain=domain, test_id="5fec3dc06339a2223bb46a48", checks=True)
    print(req.json())

    req = client.inbox_tests.get(domain=domain,
                                 test_id="5fec3dc06339a2223bb46a48",
                                 checks=True,
                                 address="zamoraburl@yahoo.com")
    print(req.json())

