import os
from client import Client

key = os.environ["APIKEY"]
domain = os.environ["DOMAIN"]

client = Client(auth=("api", key))

def post_template():
    """
    POST /<domain>/templates
    :return:
    """
    data={'name': 'template.name1',
          'description': 'template description',
          'template': '{{fname}} {{lname}}',
          'engine': 'handlebars',
          'comment': 'version comment'}

    req = client.templates.create(data=data, domain=domain)
    print(req.json())


def get_template():
    """
    GET /<domain>/templates/<name>
    :return:
    """
    params = {"active": "yes"}
    req = client.templates.get(domain=domain, filters=params, template_name='template.name1')
    print(req.json())


def update_template():
    """
    PUT /<domain>/templates/<name>
    :return:
    """
    data={'description': 'new template description'}

    req = client.templates.put(data=data,
                                  domain=domain,
                                  template_name='template.name1')
    print(req.json())


def delete_template():
    """
    DELETE /<domain>/templates/<name>
    :return:
    """
    req = client.templates.delete(domain=domain, template_name='template.name1')
    print(req.json())

def get_domain_templates():
    """
    GET /<domain>/templates
    :return:
    """
    params = {
        "limit": 1
    }
    req = client.templates.get(domain=domain, filters=params)
    print(req.json())

def delete_templates():
    """
    DELETE /<domain>/templates
    :return:
    """
    req = client.templates.delete(domain=domain)
    print(req.json())


def create_new_template_version():
    """
    POST /<domain>/templates/<template>/versions
    :return:
    """
    data={'tag': 'v1',
          'template': '{{fname}} {{lname}}',
          'engine': 'handlebars',
          'active': 'yes'
          }

    req = client.templates.create(data=data, domain=domain,
                                  template_name='template.name1', versions=True)
    print(req.json())


def get_template_version():
    """
    GET /<domain>/templates/<name>/versions/<tag>
    :return:
    """
    req = client.templates.get(domain=domain,
                               template_name='template.name1',
                               versions=True,
                               tag='v1')
    print(req.json())


def update_template_version():
    """
    PUT /<domain>/templates/<name>/versions/<tag>
    :return:
    """
    data = {
        'template': '{{fname}} {{lname}}',
        'comment': 'Updated version comment'
    }

    req = client.templates.put(domain=domain,
                               data=data,
                               template_name='template.name1',
                               versions=True,
                               tag='v1')
    print(req.json())

def delete_template_version():
    """
    DELETE /<domain>/templates/<template>/versions/<version>
    :return:
    """
    req = client.templates.delete(domain=domain,
                               template_name='template.name1',
                               versions=True,
                               tag='initial')
    print(req.json())


def get_all_versions():
    """
    GET /<domain>/templates/<template>/versions
    :return:
    """
    req = client.templates.get(domain=domain,
                               template_name='template.name1',
                               versions=True)
    print(req.json())

if __name__ == '__main__':
    get_all_versions()
