from client import Client

if __name__ == '__main__':
    key = "key-578f9790b7d06fd46a104f8156ed6995"
    domain = "2048.zeefarmer.com"
    client = Client(auth=("api", key))


    req = client.domains_webhooks.get(domain=domain)
    print(req.json())

    data = {
        'id':'clicked',
        'url':[ 'https://facebook.com'
                ]
    }
    #
    req = client.domains_webhooks.create(domain=domain, data=data)
    print(req.json())

    req = client.domains_webhooks_clicked.get(domain=domain)
    print(req.json())
