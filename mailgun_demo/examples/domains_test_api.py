from client import Client

if __name__ == '__main__':
    key = "key-578f9790b7d06fd46a104f8156ed6995"
    domain = "2048.zeefarmer.com"
    client = Client(auth=("api", key))
    ##### Get domainlist
    # data = client.domainlist.get(domain=domain)
    # print(data)
    #### Get domain


    #### Post domain
    data = {
        "name": "python.test.domain4",
        # "smtp_password": "cisco123456"
    }
    #  ### Problem with smtp_password!!!!
    #
    request = client.domains.create(data=data)
    print(request.text)
    print(request.status_code)


    #### Delete domain
    # request = client.domains.delete(domain="python.test.domain4")
    # print(request.text)
    # print(request.status_code)

    ### Get smtp credentials
    # request = client.domains_credentials.get(domain=domain)
    # print(request)

    ### Post creds
    # data = {
        # "login": "alice_bob@2048.zeefarmer.com",
        # "password": "test_new_creds123"
    # }
    # request = client.domains_credentials.delete(domain=domain, data=data, login="alice_bob")
    # print(request)

    #### Connection
    # data = {
    #     "require_tls": "false",
    #     "skip_verification": "false"
    # }
    # request = client.domains_connection.put(domain=domain, data=data)
    # print(request)

    ##### Tracking
    # data = {
    #     "active": "yes",
    #     "skip_verification": "false"
    # }
    # request = client.domains_tracking_open.put(domain=domain, data=data)
    # print(request)

    # data = {
    #     "active": "yes",
        # "skip_verification": "false"
    # }
    # request = client.domains_tracking_click.put(domain=domain, data=data)
    # print(request)

    # data = {
    #     "active": "yes",
    #     "html_footer": "\n<br>\n<p><a href=\"%unsubscribe_url%\">UnSuBsCrIbE</a></p>\n",
    #     "text_footer": "\n\nTo unsubscribe here click: <%unsubscribe_url%>\n\n"
        # "skip_verification": "false"
    # }
    # request = client.domains_tracking_unsubscribe.put(domain=domain, data=data)
    # print(request)

    ##### Dkim authority
    data = {
        "self": "false"
    }
    request = client.domains_dkimauthority.put(domain="python.test.domain4", data=data)
    print(request)

    #### Dkim selector
    data = {
        "dkim_selector": "s"
    }
    request = client.domains_dkimselector.put(domain="python.test.domain4", data=data)
    print(request)

    ##### Web Prefix
    data = {
        "web_prefix": "python"
    }
    request = client.domains_webprefix.put(domain="python.test.domain4", data=data)
    print(request)