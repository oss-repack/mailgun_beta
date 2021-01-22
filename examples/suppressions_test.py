from client import Client

if __name__ == '__main__':
    key = "key-578f9790b7d06fd46a104f8156ed6995"
    domain = "2048.zeefarmer.com"
    client = Client(auth=("api", key))


    req = client.bounces.get(domain=domain)
    print(req.json())


    data = {
        "address": "spidlisn@gmail.com",
        "code": 550,
        "error": "Test error"
    }
    req = client.bounces.create(data=data, domain=domain)


    # req = client.bounces.get(domain=domain, bounce_address="spidlisn@i.ua")
    # print(req.json())

    data = [{
        "address": "spidlisn@i.ua",
        "code": "550",
        "error": "Test error2312"
    },
        {
            "address": "diskovodik@gmail.com",
            "code": "550",
            "error": "Test error"
        }]
    req = client.bounces.create(data=data, domain=domain, headers='application/json')
    print(req.json())
    #
    # req = client.bounces.get(domain=domain, bounce_address="spidlisn@gmail.com")
    # print(req.json())
    files = {"bounce_csv": open("../doc_tests/files/mailgun_bounces_test.csv", "rb")}
    req = client.bounces_import.create(domain=domain, files=files)
    print(req.json())

    req = client.bounces.delete(domain=domain, bounce_address="spidlisn@i.ua")
    print(req.json())

    req = client.bounces.delete(domain=domain)
    print(req.json())

    #### Unsubscribes


    req = client.unsubscribes.get(domain=domain)
    print(req.json())


    data = {
        "address": "spidlisn@gmail.com",
        "tag": "unsub_test_tag"
    }
    req = client.unsubscribes.create(data=data, domain=domain)
    print(req.json())

    # req = client.bounces.get(domain=domain, bounce_address="spidlisn@i.ua")
    # print(req.json())

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
    #
    req = client.unsubscribes.create(data=data, domain=domain, headers='application/json')
    print(req.json())
    #
    req = client.unsubscribes.get(domain=domain, unsubscribe_address="1@test.com")
    print(req.json())

    files = {"unsubscribe_csv": open("../doc_tests/files/mailgun_unsubscribes.csv", "rb")}
    req = client.bounces_import.create(domain=domain, files=files)
    print(req.json())

    req = client.bounces.delete(domain=domain, unsubscribe_address="spidlisn@gmail.com")
    print(req.json())

    # req = client.unsubscribes.delete(domain=domain)
    # print(req.json())


    ### Complaints
    #
    req = client.complaints.get(domain=domain)
    print(req.json())


    data = {
        "address": "bob@gmail.com",
        "tag": "compl_test_tag"
    }
    req = client.complaints.create(data=data, domain=domain)
    print(req.json())

    req = client.complaints.get(domain=domain, complaint_address="bob@gmail.com")
    print(req.json())

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
    #
    # req = client.unsubscribes.get(domain=domain, unsubscribe_address="1@test.com")
    # print(req.json())

    files = {"complaints_csv": open("../doc_tests/files/mailgun_complaints.csv", "rb")}
    req = client.complaints_import.create(domain=domain, files=files)
    print(req.json())

    req = client.complaints.delete(domain=domain, unsubscribe_address="carol1@example.com")
    print(req.json())

    # req = client.complaints.delete(domain=domain)
    # print(req.json())

    ### Whitelists

    req = client.whitelists.get(domain=domain)
    print(req.json())


    data = {
        "address": "bob@gmail.com",
        "tag": "whitel_test"
    }
    req = client.whitelists.create(data=data, domain=domain)
    print(req.json())

    req = client.whitelists.get(domain=domain, whitelist_address="bob@gmail.com")
    print(req.json())

    data = [
        {
            "address": "alice2@example.com",
            "domain": "2048.zeefarmer.com"
        },
        {
            "address": "carol1@example.com",
            "domain": "2048.zeefarmer.com"
        }
    ]

    req = client.whitelists.create(data=data, domain=domain, headers='application/json')
    print(req.json())
    #

    files = {"whitelist_csv": open("../doc_tests/files/mailgun_whitelists.csv", "rb")}
    req = client.whitelists_import.create(domain=domain, files=files)
    print(req.json())
    #
    req = client.whitelists.delete(domain=domain, whitelist_address="bob@gmail.com")
    print(req.json())

    req = client.whitelists.delete(domain=domain)
    print(req.json())

