from client import Client

if __name__ == '__main__':
    key = "key-578f9790b7d06fd46a104f8156ed6995"
    domain = "2048.zeefarmer.com"
    client = Client(auth=("api", key))

    params = {
        "skip": 1,
        "limit": 1
    }
    req = client.routes.get(domain=domain, filters=params)
    print(req.json())
    #
    data={"priority": 0,
          "description": "Sample route",
          "expression": "match_recipient('.*@{domain_name}')".format(domain_name=domain),
          "action": ["forward('http://myhost.com/messages/')", "stop()"]
          }
    req = client.routes.create(domain=domain, data=data)
    print(req.json())

    data={"priority": 2
          }
    req = client.routes.put(domain=domain, data=data, rout_id="5eebb7d7939f249719a0c53c")
    print(req.json())

    req = client.routes.get(domain=domain, rout_id="5eebb7d7939f249719a0c53c")
    print(req.json())

    req = client.routes.delete(domain=domain, rout_id="5eebb7d7939f249719a0c53c")
    print(req.json())



