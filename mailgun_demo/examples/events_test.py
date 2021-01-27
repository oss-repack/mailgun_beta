from client import Client

if __name__ == '__main__':
    key = "key-578f9790b7d06fd46a104f8156ed6995"
    domain = "2048.zeefarmer.com"
    client = Client(auth=("api", key))


    req = client.events.get(domain=domain)
    print(req.json())

    ### Stored messages
    req = client.domains_messages.get(domain=domain, api_storage_url="https://se.api.mailgun.net/v3/domains/2048.zeefarmer.com/messages/AgEFAuH34wUg9HC4jONHUq8meODCJuYfZg==")
    print(req.json())

    # params = {
    #     "begin": "Tue, 24 Nov 2020 09:00:00 -0000",
    #     "ascending": "yes",
    #     "limit": 10,
    #     "pretty": "yes",
    #     "recipient": "diskovodik@gmail.com"
    # }

    params = {
        "event": "rejected OR failed"
    }
    req = client.events.get(domain=domain, filters=params)
    print(req.json())