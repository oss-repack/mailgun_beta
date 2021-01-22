from client import Client

if __name__ == '__main__':
    key = "key-578f9790b7d06fd46a104f8156ed6995"
    domain = "2048.zeefarmer.com"

    client = Client(auth=("api", key))

    # req = client.ips.get(domain=domain, params={"dedicated": "true"})
    # print(req.json())
    #
    # req = client.ips.get(domain=domain, ip="161.38.194.10")
    # print(req.json())

    request = client.domains_ips.get(domain=domain)
    print(request.json())

    ip_data = {
        "ip": "161.38.194.10"
    }
    request = client.domains_ips.create(domain=domain, data=ip_data)
    print(request.json())
    print(request.status_code)

    request = client.domains_ips.delete(domain=domain, ip="161.38.194.10")
    print(request.json())
    print(request.status_code)