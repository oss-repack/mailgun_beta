from client import Client

if __name__ == '__main__':
    key = "key-578f9790b7d06fd46a104f8156ed6995"
    domain = "2048.zeefarmer.com"
    client = Client(auth=("api", key))

    data={'name': 'template.name1',
          'description': 'template description',
          'template': '{{fname}} {{lname}}',
          'engine': 'handlebars',
          'comment': 'version comment'}
    #
    req = client.templates.create(data=data, domain=domain)
    print(req.json())

    # params = {"active": "yes"}
    req = client.templates.get(domain=domain, filters=params, template_name='template.name1')
    print(req.json())

    # data={'description': 'new template description'}

    req = client.templates.put(data=data,
                                  domain=domain,
                                  template_name='template.name1')
    # print(req.json())

    # req = client.templates.get(domain=domain)
    # print(req.json())

    req = client.templates.delete(domain=domain)
    print(req.json())

    # data={'tag': 'v1',
    #       'template': '{{fname}} {{lname}}',
    #       'engine': 'handlebars',
    #       'active': 'yes'
    #       }
    #
    req = client.templates.create(data=data, domain=domain,
                                  template_name='template.name1', versions=True)
    print(req.json())
    #
    # req = client.templates.get(domain=domain,
    #                            template_name='template.name1',
    #                            versions=True,
    #                            tag='v1')
    # print(req.json())

    req = client.templates.get(domain=domain,
                               template_name='template.name1',
                               versions=True)
    print(req.json())

    # data = {
    #     'template': '{{fname}} {{lname}}',
    #     'comment': 'Updated version comment'
    # }

    req = client.templates.put(domain=domain,
                               data=data,
                               template_name='template.name1',
                               versions=True,
                               tag='v0')
    print(req.json())

    req = client.templates.delete(domain=domain,
                               template_name='template.name1',
                               versions=True,
                               tag='v0')
    print(req.json())