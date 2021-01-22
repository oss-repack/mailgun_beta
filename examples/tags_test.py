from client import Client

if __name__ == '__main__':
    key = "key-578f9790b7d06fd46a104f8156ed6995"
    domain = "2048.zeefarmer.com"
    client = Client(auth=("api", key))


    # req = client.tags.get(domain=domain)
    # print(req.json())

    # req = client.tags.get(domain=domain, tag_name="Python test")
    # print(req.json())

    # data = {
    #     "description": "Python testtt"
    # }
    #
    # req = client.tags.put(domain=domain, tag_name="Python test", data=data)
    # print(req.json())

    # params = {
    #     "event": "accepted"
    # }
    # req = client.tags_stats.get(domain=domain, filters=params, tag_name="Python test")
    # print(req.json())

    params = {
        "event": "accepted"
    }
    req = client.tags_stats_aggregates_devices.get(domain=domain, filters=params, tag_name="Python test")
    print(req.json())
