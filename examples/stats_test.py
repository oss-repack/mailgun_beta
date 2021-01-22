from client import Client

if __name__ == '__main__':
    key = "key-578f9790b7d06fd46a104f8156ed6995"
    domain = "2048.zeefarmer.com"
    client = Client(auth=("api", key))

    params = {"event": ["accepted", "delivered", "failed"],
              "duration": "1m"}

    req = client.stats_total.get(filters=params, domain=domain)
    print(req.json())