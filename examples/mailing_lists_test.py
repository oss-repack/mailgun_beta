from client import Client

if __name__ == '__main__':
    key = "key-578f9790b7d06fd46a104f8156ed6995"
    domain = "2048.zeefarmer.com"
    client = Client(auth=("api", key))


    # req = client.lists_pages.get(domain=domain)
    # print(req.json())
    #
    # req = client.lists.get(domain=domain, address="everyone@mailgun.zeefarmer.com")
    # print(req.json())

    data = {
        'address': 'python_sdk@{domain}'.format(domain=domain),
        'description': "Mailgun developers list"}

    req = client.lists.create(domain=domain, data=data)
    print(req.json())

    data = {
        'description': "Mailgun developers list 121212"
    }

    # req = client.lists.put(domain=domain, data=data, address='python_sdk@{domain}'.format(domain=domain))
    # print(req.json())


    # req = client.lists.delete(domain=domain, address='python_sdk@{domain}'.format(domain=domain))
    # print(req.json())

    # req = client.lists.create(domain=domain, address="everyone@mailgun.zeefarmer.com", validate=True)
    # print(req.json())
    #
    # req = client.lists.get(domain=domain, address="everyone@mailgun.zeefarmer.com", validate=True)
    # print(req.json())
    #
    # req = client.lists.delete(domain=domain, address="everyone@mailgun.zeefarmer.com", validate=True)
    # print(req.json())

    req = client.lists_members_pages.get(domain=domain, address="everyone@mailgun.zeefarmer.com")
    print(req.json())
    #
    req = client.lists_members.get(domain=domain, address="everyone@mailgun.zeefarmer.com",
                                   member_address="zerreissen@hotmail.com")
    print(req.json())

    data = {'subscribed': True,
            'address': 'bar@example.com',
            'name': 'Bob Bar',
            'description': 'Developer',
            'vars': '{"age": 26}'}
    req = client.lists_members.create(domain=domain, address="everyone@mailgun.zeefarmer.com", data=data)
    print(req.json())

    data = {'subscribed': True,
            'address': 'bar@example.com',
            'name': 'Bob Bar 2',
            'description': 'Developer',
            'vars': '{"age": 28}'}

    req = client.lists_members.put(domain=domain, address="everyone@mailgun.zeefarmer.com", data=data,
                                   member_address="bar@example.com")
    print(req.json())


    data = {'upsert': True,
            'members': '[{"address": "Alice <alice@example.com>", "vars": {"age": 26}},'
                       '{"name": "Bob", "address": "bob2@example.com", "vars": {"age": 34}}]'}

    req = client.lists_members.create(domain=domain, address="everyone@mailgun.zeefarmer.com", data=data, multiple=True)
    print(req.json())


    req = client.lists_members.delete(domain=domain,
                                      address="everyone@mailgun.zeefarmer.com",
                                      member_address="bob2@example.com")
    print(req.json())