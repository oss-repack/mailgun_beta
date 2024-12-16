import os

from mailgun.client import Client


key = os.environ["APIKEY"]
domain = os.environ["DOMAIN"]

client = Client(auth=("api", key))


def get_webhooks():
    """
    GET /domains/<domain>/webhooks
    :return:
    """
    req = client.domains_webhooks.get(domain=domain)
    print(req.json())


def create_webhook():
    """
    POST /domains/<domain>/webhooks
    :return:
    """
    data = {"id": "clicked", "url": ["https://facebook.com"]}
    #
    req = client.domains_webhooks.create(domain=domain, data=data)
    print(req.json())


def put_webhook():
    """
    PUT /domains/<domain>/webhooks/<webhookname>
    :return:
    """
    data = {"id": "clicked", "url": ["https://facebook.com", "https://google.com"]}

    req = client.domains_webhooks_clicked.put(domain=domain, data=data)
    print(req.json())


def delete_webhook():
    """
    DELETE /domains/<domain>/webhooks/<webhookname>
    :return:
    """
    req = client.domains_webhooks_clicked.delete(domain=domain)
    print(req.json())


if __name__ == "__main__":
    delete_webhook()
