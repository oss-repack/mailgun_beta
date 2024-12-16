import os

from mailgun.client import Client


key = os.environ["APIKEY"]
domain = os.environ["DOMAIN"]

client = Client(auth=("api", key))


def get_routes():
    """
    GET /routes
    :return:
    """
    params = {
        "skip": 1,
        "limit": 1
    }
    req = client.routes.get(domain=domain, filters=params)
    print(req.json())


def get_route_by_id():
    """
    GET /routes/<id>
    :return:
    """
    req = client.routes.get(domain=domain, route_id="6012d994e8d489e24a127e79")
    print(req.json())


def post_routes():
    """
    POST /routes
    :return:
    """
    data = {"priority": 0,
            "description": "Sample route",
            "expression": "match_recipient('.*@{domain_name}')".format(domain_name=domain),
            "action": ["forward('http://myhost.com/messages/')", "stop()"]
            }
    req = client.routes.create(domain=domain, data=data)
    print(req.json())


def put_route():
    """
    PUT /routes/<id>
    :return:
    """
    data = {"priority": 2,
            "description": "Sample route",
            "expression": "match_recipient('.*@{domain_name}')".format(domain_name=domain),
            "action": ["forward('http://myhost.com/messages/')", "stop()"]
            }
    req = client.routes.put(
        domain=domain,
        data=data,
        route_id="60142b357c90c3c9f228e0a6")
    print(req.json())


def delete_route():
    """
    DELETE /routes/<id>
    :return:
    """
    req = client.routes.delete(domain=domain, route_id="60142b357c90c3c9f228e0a6")
    print(req.json())


if __name__ == "__main__":
    delete_route()
