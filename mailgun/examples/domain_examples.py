import os

from mailgun.client import Client


key = os.environ["APIKEY"]
domain = os.environ["DOMAIN"]

client = Client(auth=("api", key))


def get_domains():
    """
    GET /domains
    :return:
    """
    data = client.domainlist.get(domain=domain)
    print(data.json())


# Get domain


def get_simple_domain():
    """
    GET /domains/<domain>
    :return:
    """
    domain_name = "python.test.domain4"
    data = client.domains.get(domain_name=domain_name)
    print(data.json())


def verify_domain():
    """
    PUT /domains/<domain>/verify
    :return:
    """
    domain_name = "python.test.domain4"
    data = client.domains.put(domain=domain_name, verify=True)
    print(data.json())


def add_domain():
    """
    POST /domains
    :return:
    """
    # Post domain
    data = {
        "name": "python.test.domain5",
        # "smtp_password": "cisco123456"
    }
    # Problem with smtp_password!!!!

    request = client.domains.create(data=data)
    print(request.json())
    print(request.status_code)


def delete_domain():
    """
    DELETE /domains/<domain>
    :return:
    """
    # Delete domain
    request = client.domains.delete(domain="python.test.domain5")
    print(request.text)
    print(request.status_code)


def get_credentials():
    """
    GET /domains/<domain>/credentials
    :return:
    """
    request = client.domains_credentials.get(domain=domain)
    print(request.json())


def post_credentials():
    """
    POST /domains/<domain>/credentials
    :return:
    """
    data = {"login": f"alice_bob@{domain}", "password": "test_new_creds123"}
    request = client.domains_credentials.create(domain=domain, data=data)
    print(request.json())


def put_credentials():
    """
    PUT /domains/<domain>/credentials/<login>
    :return:
    """
    data = {"password": "test_new_creds12356"}
    request = client.domains_credentials.put(
        domain=domain, data=data, login=f"alice_bob@{domain}"
    )
    print(request.json())


def delete_credentials():
    """
    DELETE /domains/<domain>/credentials/<login>
    :return:
    """
    request = client.domains_credentials.delete(
        domain=domain, login=f"alice_bob@{domain}"
    )
    print(request.json())


def get_connections():
    """
    GET /domains/<domain>/connection
    :return:
    """
    request = client.domains_connection.get(domain=domain)
    print(request.json())


def put_connections():
    """
    PUT /domains/<domain>/connection
    :return:
    """
    data = {"require_tls": "true", "skip_verification": "false"}
    request = client.domains_connection.put(domain=domain, data=data)
    print(request.json())


def get_tracking():
    """
    GET /domains/<domain>/tracking
    :return:
    """
    request = client.domains_tracking.get(domain=domain)
    print(request.json())


def put_open_tracking():
    """
    PUT /domains/<domain>/tracking/open
    :return:
    """
    data = {"active": "yes", "skip_verification": "false"}
    request = client.domains_tracking_open.put(domain=domain, data=data)
    print(request.json())


def put_click_tracking():
    """
    PUT /domains/<domain>/tracking/click
    :return:
    """
    data = {
        "active": "yes",
    }
    request = client.domains_tracking_click.put(domain=domain, data=data)
    print(request.json())


def put_unsub_tracking():
    """
    PUT /domains/<domain>/tracking/unsubscribe
    :return:
    """
    # fmt: off
    data = {
        "active": "yes",
        "html_footer": "\n<br>\n<p><a href=\"%unsubscribe_url%\">UnSuBsCrIbE</a></p>\n",
        "text_footer": "\n\nTo unsubscribe here click: <%unsubscribe_url%>\n\n"
    }
    # fmt: on
    request = client.domains_tracking_unsubscribe.put(domain=domain, data=data)
    print(request.json())


def put_dkim_authority():
    """
    PUT /domains/<domain>/dkim_authority
    :return:
    """
    data = {"self": "false"}
    request = client.domains_dkimauthority.put(domain=domain, data=data)
    print(request.json())


def put_dkim_selector():
    """
    PUT /domains/<domain>/dkim_selector
    :return:
    """
    data = {"dkim_selector": "s"}
    request = client.domains_dkimselector.put(domain="python.test.domain4", data=data)
    print(request.json())


def put_web_prefix():
    """
    PUT /domains/<domain>/web_prefix
    :return:
    """
    data = {"web_prefix": "python"}
    request = client.domains_webprefix.put(domain="python.test.domain4", data=data)
    print(request.json())


if __name__ == "__main__":
    put_web_prefix()
