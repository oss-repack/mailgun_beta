from client import Client

if __name__ == '__main__':
    key = "key-578f9790b7d06fd46a104f8156ed6995"
    domain = "2048.zeefarmer.com"
    client = Client(auth=("api", key))

    req = client.ippools.get(domain=domain)
    print(req.json())
    # pool_id_list = req.json()["ip_pools"]
    # # # #
    # data = {
    #     "name" : "test_pool",
    #     "description": "Test",
    #     "ips": ["166.78.68.186"]
    # }
    # req = client.ippools.create(domain=domain, data=data)
    # print(req.json())
    #
    # data = {
    #     "name" : "test_pool3",
    #     "description": "Test3",
    #     "add_ip":"127.0.0.1"
    # }
    # req = client.ippools.patch(domain=domain, data=data, pool_id='5fc56d8e1d75fe44715416d8')
    # print(req.json())

    # for ip_pool in pool_id_list:
    #     req = client.ippools.delete(domain=domain, pool_id=ip_pool["pool_id"])
    #     print(req.json())

    data = {
        "pool_id": "5fc4af6f27733e78df9a0fbb"
    }
    req = client.domains_ips.create(domain=domain, data=data)
    print(req.json())