from client import Client

if __name__ == '__main__':
    key = "key-578f9790b7d06fd46a104f8156ed6995"
    domain = "2048.zeefarmer.com"
    client = Client(auth=("api", key))

    params = {"address": "spidlisn@i.ua",
              "provider_lookup": "false"}
    req = client.addressvalidate.get(domain=domain, filters=params)
    print(req.json())


    data = {"address": "diskovodik@gmail.com"}
    params = {"provider_lookup": "false"}
    req = client.addressvalidate.create(domain=domain, data=data, filters=params)
    print(req.json())

    # params = {"limit": 1}
    req = client.addressvalidate_bulk.get(domain=domain, filters=params)
    print(req.json())

    # files = {'file': open('doc_tests/files/email_validation.csv', 'rb')}
    # req = client.addressvalidate_bulk.create(domain=domain, files=files, list_name="python_list")
    # print(req.json())

    # req = client.addressvalidate_bulk.get(domain=domain, list_name="python_list")
    # print(req.json())

    # req = client.addressvalidate_bulk.delete(domain=domain, list_name="python_list")
    # print(req.json())

    req = client.addressvalidate_preview.get(domain=domain)
    print(req.json())

    files = {'file': open('../doc_tests/files/email_previews.csv', 'rb')}
    req = client.addressvalidate_preview.put(domain=domain, files=files, list_name="python_list")
    print(req.json())

    # files = {'file': open('doc_tests/files/email_previews.csv', 'rb')}
    # req = client.addressvalidate_preview.delete(domain=domain, list_name="python_list")
    # print(req.status_code)