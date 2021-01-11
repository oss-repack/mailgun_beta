import unittest
import os
from client import Client


class MessagesTests(unittest.TestCase):
    def setUp(self):
        self.auth = (
            "api",
            os.environ["APIKEY"]
        )
        self.client = Client(auth=self.auth)
        self.domain = os.environ["DOMAIN"]
        self.data = {"from": os.environ["MESSAGES_FROM"],
            "to": os.environ["MESSAGES_TO"],
            "cc":  os.environ["MESSAGES_CC"],
            "subject": "Hello Vasyl Bodaj",
            "text": "Congratulations !!!!!, you just sent an email with Mailgun!  You are truly awesome!",
            "o:tag": "Python test"}

    def test_post_right_message(self):
        req = self.client.messages.create(data=self.data, domain=self.domain)
        self.assertEqual(req.status_code, 200)

    def test_post_wrong_message(self):
        req = self.client.messages.create(data={"from": "sdsdsd"}, domain=self.domain)
        self.assertEqual(req.status_code, 400)


class DomainTests(unittest.TestCase):
    def setUp(self):
        self.auth = (
            "api",
            os.environ["APIKEY"]
        )
        self.client = Client(auth=self.auth)
        self.domain = os.environ["DOMAIN"]
        self.test_domain = "mailgun.wrapper.test"
        self.post_domain_data = {
            "name": self.test_domain,
        }
        self.post_domain_creds = {
            "login": "alice_bob@2048.zeefarmer.com",
            "password": "test_new_creds123"
        }

        self.put_domain_creds = {
            "password": "test_new_creds"
        }

    def test_get_domain_list(self):
        req = self.client.domainlist.get(domain=self.domain)
        self.assertEqual(req.status_code, 200)
        self.assertIn("items", req.json())

    def test_post_domain(self):

        #  ### Problem with smtp_password!!!!
        #
        request = self.client.domains.create(data=self.post_domain_data)
        self.assertEqual(request.status_code, 200)
        self.assertIn("Domain has been created", request.json()["message"])

    def test_delete_domain(self):
        self.client.domains.create(data=self.post_domain_data)
        request = self.client.domains.delete(domain=self.test_domain)
        self.assertEqual(request.json()["message"], "Domain has been deleted")
        self.assertEqual(request.status_code, 200)

    def test_get_smtp_creds(self):
        request = self.client.domains_credentials.get(domain=self.domain)
        print(request.json())
        self.assertEqual(request.status_code, 200)
        self.assertIn("items", request.json())

    def test_post_domain_creds(self):
        request = self.client.domains_credentials.create(domain=self.domain,
                                                         data=self.post_domain_creds)
        self.assertEqual(request.status_code, 200)
        self.assertIn("message", request.json())

    def test_put_domain_creds(self):
        self.client.domains_credentials.create(domain=self.domain,
                                               data=self.post_domain_creds)
        request = self.client.domains_credentials.put(domain=self.domain,
                                                      data=self.put_domain_creds,
                                                      login="alice_bob")

        self.assertEqual(request.status_code, 200)
        self.assertIn("message", request.json())

    def test_delete_domain_creds(self):
        self.client.domains_credentials.create(domain=self.domain,
                                               data=self.post_domain_creds)
        request = self.client.domains_credentials.delete(domain=self.domain,
                                                         login="alice_bob")

        self.assertEqual(request.status_code, 200)


class IpTests(unittest.TestCase):
    def setUp(self):
        self.auth = (
            "api",
            os.environ["APIKEY"]
        )
        self.client = Client(auth=self.auth)
        self.domain = os.environ["DOMAIN"]
        self.ip_data = {
            "ip": os.environ["DOMAINS_DEDICATED_IP"]
        }

    def test_get_ip_from_domain(self):

        req = self.client.ips.get(domain=self.domain, params={"dedicated": "true"})
        self.assertIn("items", req.json())
        self.assertEqual(req.status_code, 200)

    def test_create_ip(self):
        request = self.client.domains_ips.create(domain=self.domain, data=self.ip_data)
        self.assertEqual("success", request.json()["message"])
        self.assertEqual(request.status_code, 200)

    def test_delete_ip(self):
        request = self.client.domains_ips.delete(domain=self.domain, ip=self.ip_data["ip"])
        self.assertEqual("success", request.json()["message"])
        self.assertEqual(request.status_code, 200)


class IpPoolsTests(unittest.TestCase):
    def setUp(self):
        self.auth = (
            "api",
            os.environ["APIKEY"]
        )
        self.client = Client(auth=self.auth)
        self.domain = "2048.zeefarmer.com"
        self.data = {
            "name" : "test_pool",
            "description": "Test"
        }
        self.patch_data = {
            "name" : "test_pool1",
            "description": "Test1"
        }
        self.ippool_id = ""

    def test_get_ippools(self):
        req = self.client.ippools.get(domain=self.domain)
        self.assertIn("ip_pools", req.json())
        self.assertEqual(req.status_code, 200)

    def test_post_ippool(self):

        req = self.client.ippools.create(domain=self.domain,
                                         data=self.data)
        self.assertEqual("success", req.json()["message"])
        self.assertEqual(req.status_code, 200)
        self.ippool_id = req.json()["pool_id"]

    def test_patch_ippool(self):
        req_post = self.client.ippools.create(domain=self.domain,
                                         data=self.data)
        self.ippool_id = req_post.json()["pool_id"]

        req = self.client.ippools.patch(domain=self.domain, data=self.patch_data, pool_id=self.ippool_id)
        self.assertEqual("success", req.json()["message"])
        self.assertEqual(req.status_code, 200)

    def test_delete_ippool(self):
        req = self.client.ippools.create(domain=self.domain,
                                         data=self.data)
        self.ippool_id = req.json()["pool_id"]
        req_del = self.client.ippools.delete(domain=self.domain, pool_id=self.ippool_id)
        self.assertEqual("started", req_del.json()["message"])


class EventsTests(unittest.TestCase):
    def setUp(self):
        self.auth = (
            "api",
            os.environ["APIKEY"]
        )
        self.client = Client(auth=self.auth)
        self.domain = "2048.zeefarmer.com"
        self.params = {
            "event" : "rejected"
        }

    def test_events_get(self):
        req = self.client.events.get(domain=self.domain)
        self.assertIn("items", req.json())
        self.assertEqual(req.status_code, 200)

    def test_event_params(self):
        req = self.client.events.get(domain=self.domain,
                                     filters=self.params)

        self.assertIn("items", req.json())
        self.assertEqual(req.status_code, 200)


class StatsTests(unittest.TestCase):
    def setUp(self):
        self.auth = (
            "api",
            os.environ["APIKEY"]
        )
        self.client = Client(auth=self.auth)
        self.domain = "2048.zeefarmer.com"
        self.params = {
            "event" : ["accepted"],
            "duration": "1m"
        }

    def test_stats_total_get(self):
        req = self.client.stats_total.get(filters=self.params,
                                          domain=self.domain)
        self.assertIn("stats", req.json())
        self.assertEqual(req.status_code, 200)


class TagsTests(unittest.TestCase):
    def setUp(self):
        self.auth = (
            "api",
            os.environ["APIKEY"]
        )
        self.client = Client(auth=self.auth)
        self.domain = "2048.zeefarmer.com"
        self.data = {
            "description" : "Tests running"
        }
        self.tag_name = "Python test"

    def test_get_tags(self):
        req = self.client.tags.get(domain=self.domain)
        self.assertIn('items', req.json())
        self.assertEqual(req.status_code, 200)

    def test_tag_get_by_name(self):
        req = self.client.tags.get(domain=self.domain,
                                   tag_name=self.tag_name)
        self.assertIn('tag', req.json())
        self.assertEqual(req.status_code, 200)


class BouncesTests(unittest.TestCase):
    def setUp(self):
        self.auth = (
            "api",
            os.environ["APIKEY"]
        )
        self.client = Client(auth=self.auth)
        self.domain = "2048.zeefarmer.com"
        self.bounces_data = {
            "address": "test@gmail.com",
            "code": 550,
            "error": "Test error"
            }

        self.bounces_json_data = [{
            "address": "test1@gmail.com",
            "code": "550",
            "error": "Test error2312"
        },
            {
                "address": "test2@gmail.com",
                "code": "550",
                "error": "Test error"
            }]

    def test_bounces_get(self):
        req = self.client.bounces.get(domain=self.domain)
        self.assertEqual(req.status_code, 200)
        self.assertIn('items', req.json())

    def test_bounces_create(self):
        req = self.client.bounces.create(data=self.bounces_data,
                                         domain=self.domain)
        print(req.json())
        self.assertEqual(req.status_code, 200)
        self.assertIn('address', req.json())

    def test_bounces_get_address(self):
        req_post = self.client.bounces.create(data=self.bounces_data,
                                         domain=self.domain)
        req = self.client.bounces.get(domain=self.domain,
                                      bounce_address=self.bounces_data["address"])
        self.assertEqual(req.status_code, 200)
        self.assertIn('address', req.json())

    def test_bounces_create_json(self):
        req = self.client.bounces.create(data=self.bounces_json_data,
                                         domain=self.domain,
                                         headers='application/json')
        self.assertEqual(req.status_code, 200)
        self.assertIn('message', req.json())

    def test_bounces_delete_single(self):
        req_post = self.client.bounces.create(data=self.bounces_data,
                                         domain=self.domain)
        req = self.client.bounces.delete(domain=self.domain,
                                         bounce_address=self.bounces_data["address"])
        self.assertEqual(req.status_code, 200)
        self.assertIn('message', req.json())

    def test_bounces_delete_all(self):
        req = self.client.bounces.delete(domain=self.domain)
        self.assertEqual(req.status_code, 200)
        self.assertIn('message', req.json())


class UnsubscribesTest(unittest.TestCase):
    def setUp(self):
        self.auth = (
            "api",
            os.environ["APIKEY"]
        )
        self.client = Client(auth=self.auth)
        self.domain = "2048.zeefarmer.com"
        self.unsub_data = {
            "address": "test@gmail.com",
            "tag": "unsub_test_tag"
        }

        self.unsub_json_data = [{
            "address": "test1@gmail.com",
            "tags": ["some tag"],
            "error": "Test error2312"
        },
        {
            "address": "test2@gmail.com",
            "code": ["*"],
            "error": "Test error"
        },
            {
                "address": "test3@gmail.com"
            }]

    def test_unsub_create(self):
        req = self.client.unsubscribes.create(data=self.unsub_data,
                                              domain=self.domain)
        self.assertEqual(req.status_code, 200)
        self.assertIn("message", req.json())

    def test_unsub_get(self):
        req = self.client.unsubscribes.get(domain=self.domain)
        self.assertEqual(req.status_code, 200)
        self.assertIn("items", req.json())

    def test_unsub_get_single(self):
        req = self.client.unsubscribes.get(domain=self.domain,
                                           bounce_address=self.unsub_data["address"])
        self.assertEqual(req.status_code, 200)
        self.assertIn("items", req.json())

    def test_unsub_create_multiple(self):
        req = self.client.unsubscribes.create(data=self.unsub_json_data,
                                              domain=self.domain,
                                              headers='application/json')

        self.assertEqual(req.status_code, 200)
        self.assertIn("message", req.json())

    def test_unsub_delete(self):
        req = self.client.bounces.delete(domain=self.domain,
                                         unsubscribe_address=self.unsub_data["address"])

        self.assertEqual(req.status_code, 200)
        self.assertIn("message", req.json())

    def test_unsub_delete_all(self):
        req = self.client.bounces.delete(domain=self.domain)

        self.assertEqual(req.status_code, 200)
        self.assertIn("message", req.json())


class ComplaintsTest(unittest.TestCase):
    def setUp(self):
        self.auth = (
            "api",
            os.environ["APIKEY"]
        )
        self.client = Client(auth=self.auth)
        self.domain = "2048.zeefarmer.com"
        self.compl_data = {
            "address": "test@gmail.com",
            "tag": "compl_test_tag"
        }

        self.compl_json_data = [{
            "address": "test1@gmail.com",
            "tags": ["some tag"],
            "error": "Test error2312"
        },
            {
                "address": "test3@gmail.com"
            }]

    def test_compl_create(self):
        req = self.client.complaints.create(data=self.compl_data,
                                            domain=self.domain)

        self.assertEqual(req.status_code, 200)
        self.assertIn("message", req.json())

    def test_compl_get_all(self):
        req = self.client.complaints.get(domain=self.domain)
        self.assertEqual(req.status_code, 200)
        self.assertIn('items', req.json())

    def test_compl_get_single(self):
        req_post = self.client.complaints.create(data=self.compl_data,
                                            domain=self.domain)
        req = self.client.complaints.get(domain=self.domain,
                                         complaint_address=self.compl_data["address"])
        self.assertEqual(req.status_code, 200)
        self.assertIn('address', req.json())

    def test_compl_create_multiple(self):
        req = self.client.complaints.create(data=self.compl_json_data,
                                            domain=self.domain,
                                            headers='application/json')

        self.assertEqual(req.status_code, 200)
        self.assertIn("message", req.json())

    def test_compl_delete_single(self):
        req = self.client.complaints.delete(domain=self.domain,
                                            unsubscribe_address=self.compl_data["address"])

        self.assertEqual(req.status_code, 200)
        self.assertIn("message", req.json())

    def test_compl_delete_all(self):
        req = self.client.complaints.delete(domain=self.domain)
        self.assertEqual(req.status_code, 200)
        self.assertIn("message", req.json())


class WhiteListTest(unittest.TestCase):
    def setUp(self):
        self.auth = (
            "api",
            os.environ["APIKEY"]
        )
        self.client = Client(auth=self.auth)
        self.domain = "2048.zeefarmer.com"
        self.whitel_data = {
            "address": "test@gmail.com",
            "tag": "whitel_test"
        }

        self.whitl_json_data = [{
            "address": "test1@gmail.com",
            "domain": self.domain
        },
        {
            "address": "test3@gmail.com",
            "domain": self.domain
        }]

    def test_whitel_create(self):
        req = self.client.whitelists.create(data=self.whitel_data,
                                            domain=self.domain)
        self.assertEqual(req.status_code, 200)
        self.assertIn("message", req.json())

    def test_whitel_get_simple(self):
        req_post = self.client.whitelists.create(data=self.whitel_data,
                                                domain=self.domain)

        req = self.client.whitelists.get(domain=self.domain,
                                         whitelist_address=self.whitel_data["address"])

        self.assertEqual(req.status_code, 200)
        self.assertIn("value", req.json())

    def test_whitel_delete_simple(self):
        self.client.whitelists.create(data=self.whitel_data,
                                      domain=self.domain)
        req = self.client.whitelists.delete(domain=self.domain,
                                            whitelist_address=self.whitel_data["address"])

        self.assertEqual(req.status_code, 200)
        self.assertIn("message", req.json())


class RoutesTest(unittest.TestCase):
    def setUp(self):
        self.auth = (
            "api",
            os.environ["APIKEY"]
        )
        self.client = Client(auth=self.auth)
        self.domain = "2048.zeefarmer.com"
        self.routes_data = {
            "priority": 0,
            "description": "Sample route",
            "expression": "match_recipient('.*@{domain_name}')".format(domain_name=self.domain),
            "action": ["forward('http://myhost.com/messages/')", "stop()"]
        }
        self.routes_params = {
            "skip": 1,
            "limit": 1
        }
        self.routes_put_data = {
            "priority": 2
        }

    def test_routes_create(self):
        req = self.client.routes.create(domain=self.domain,
                                        data=self.routes_data)

        self.assertEqual(req.status_code, 200)
        self.assertIn("message", req.json())

    def test_routes_get_all(self):
        req_post = self.client.routes.create(domain=self.domain,
                                        data=self.routes_data)
        req = self.client.routes.get(domain=self.domain,
                                     filters=self.routes_params)

        self.assertEqual(req.status_code, 200)
        self.assertIn("items", req.json())

    def test_get_route_by_id(self):
        req_post = self.client.routes.create(domain=self.domain,
                                  data=self.routes_data)
        self.client.routes.create(domain=self.domain,
                                  data=self.routes_data)
        req = self.client.routes.get(domain=self.domain,
                                     route_id=req_post.json()["route"]["id"])

        self.assertEqual(req.status_code, 200)
        self.assertIn("route", req.json())

    def test_routes_put(self):
        req_post = self.client.routes.create(domain=self.domain,
                                             data=self.routes_data)
        req = self.client.routes.put(domain=self.domain,
                                     data=self.routes_put_data,
                                     route_id=req_post.json()["route"]["id"])

        self.assertEqual(req.status_code, 200)
        self.assertIn("message", req.json())

    def test_routes_delete(self):
        req_post = self.client.routes.create(domain=self.domain,
                                             data=self.routes_data)
        req = self.client.routes.delete(domain=self.domain,
                                        route_id=req_post.json()["route"]["id"])

        self.assertEqual(req.status_code, 200)
        self.assertIn("message", req.json())


class WebhooksTest(unittest.TestCase):
    def setUp(self):
        self.auth = (
            "api",
            os.environ["APIKEY"]
        )
        self.client = Client(auth=self.auth)
        self.domain = "2048.zeefarmer.com"
        self.webhooks_data = {
            'id': 'clicked',
            'url': ['https://i.ua']
        }

        self.webhooks_data_put = {
            'url': 'https://twitter.com'
        }

    def test_webhooks_create(self):
        req = self.client.domains_webhooks.create(domain=self.domain,
                                                  data=self.webhooks_data)

        self.assertEqual(req.status_code, 200)
        self.assertIn("message", req.json())
        self.client.domains_webhooks_clicked.delete(domain=self.domain)

    def test_webhooks_get(self):
        req = self.client.domains_webhooks.get(domain=self.domain)
        self.assertEqual(req.status_code, 200)
        self.assertIn("webhooks", req.json())

    def test_webhook_put(self):
        self.client.domains_webhooks.create(domain=self.domain,
                                            data=self.webhooks_data)
        req = self.client.domains_webhooks_clicked.put(domain=self.domain,
                                                       data=self.webhooks_data_put)
        self.assertEqual(req.status_code, 200)
        self.assertIn("message", req.json())
        self.client.domains_webhooks_clicked.delete(domain=self.domain)

    def test_webhook_get_simple(self):
        self.client.domains_webhooks.create(domain=self.domain,
                                            data=self.webhooks_data)
        req = self.client.domains_webhooks_clicked.get(domain=self.domain)
        self.assertEqual(req.status_code, 200)
        self.assertIn("webhook", req.json())
        self.client.domains_webhooks_clicked.delete(domain=self.domain)

    def test_webhook_delete(self):
        self.client.domains_webhooks.create(domain=self.domain,
                                            data=self.webhooks_data)
        req = self.client.domains_webhooks_clicked.delete(domain=self.domain)
        self.assertEqual(req.status_code, 200)
        self.assertIn("message", req.json())


class MailingListsTest(unittest.TestCase):
    def setUp(self):
        self.auth = (
            "api",
            os.environ["APIKEY"]
        )
        self.client = Client(auth=self.auth)
        self.domain = os.environ["DOMAIN"]
        self.maillist_address = os.environ["MAILLIST_ADDRESS"]
        self.mailing_lists_data = {
            'address': 'python_sdk@{domain}'.format(domain=self.domain),
            'description': "Mailgun developers list"
        }

        self.mailing_lists_data_update = {
            'description': "Mailgun developers list 121212"
        }

        self.mailing_lists_members_data = {
            'subscribed': True,
            'address': 'bar@example.com',
            'name': 'Bob Bar',
            'description': 'Developer',
            'vars': '{"age": 26}'
        }

        self.mailing_lists_members_put_data = {
            'subscribed': True,
            'address': 'bar@example.com',
            'name': 'Bob Bar',
            'description': 'Developer',
            'vars': '{"age": 28}'
        }

        self.mailing_lists_members_data_mult = {'upsert': True,
                                                'members': '[{"address": "Alice <alice@example.com>", "vars": {"age": 26}},'
                                                '{"name": "Bob", "address": "bob2@example.com", "vars": {"age": 34}}]'}



    def test_maillist_pages_get(self):
        req = self.client.lists_pages.get(domain=self.domain)
        self.assertEqual(req.status_code, 200)
        self.assertIn("items", req.json())

    def test_maillist_lists_get(self):
        req = self.client.lists.get(domain=self.domain,
                                    address=self.maillist_address)
        self.assertEqual(req.status_code, 200)
        self.assertIn("list", req.json())

    def test_maillist_lists_create(self):
        self.client.lists.delete(domain=self.domain,
                                 address='python_sdk@{domain}'.format(domain=self.domain))
        req = self.client.lists.create(domain=self.domain,
                                       data=self.mailing_lists_data)
        # print(req.json())
        self.assertEqual(req.status_code, 200)
        self.assertIn("list", req.json())

    def test_maillists_lists_put(self):
        self.client.lists.create(domain=self.domain,
                                 data=self.mailing_lists_data)
        req = self.client.lists.put(domain=self.domain,
                                    data=self.mailing_lists_data_update,
                                    address='python_sdk@{domain}'.format(domain=self.domain))
        self.assertEqual(req.status_code, 200)
        self.assertIn("list", req.json())

    def test_maillists_lists_delete(self):
        self.client.lists.create(domain=self.domain,
                                 data=self.mailing_lists_data)
        req = self.client.lists.delete(domain=self.domain,
                                       address='python_sdk@{domain}'.format(domain=self.domain))
        self.assertEqual(req.status_code, 200)

    def test_maillists_lists_validate_create(self):
        req = self.client.lists.create(domain=self.domain,
                                       address=self.maillist_address,
                                       validate=True)

        self.assertEqual(req.status_code, 202)
        self.assertIn("message", req.json())

    def test_maillists_lists_validate_get(self):
        req = self.client.lists.get(domain=self.domain,
                                    address=self.maillist_address,
                                    validate=True)

        self.assertEqual(req.status_code, 200)
        self.assertIn("id", req.json())

    def test_maillists_lists_validate_delete(self):
        self.client.lists.create(domain=self.domain,
                                 address=self.maillist_address,
                                 validate=True)
        req = self.client.lists.get(domain=self.domain,
                                    address=self.maillist_address,
                                    validate=True)

        self.assertEqual(req.status_code, 200)

    def test_maillists_lists_members_pages_get(self):
        req = self.client.lists_members_pages.get(domain=self.domain,
                                                  address=self.maillist_address)
        self.assertEqual(req.status_code, 200)
        self.assertIn("items", req.json())

    def test_maillists_lists_members_create(self):
        self.client.lists_members.delete(domain=self.domain,
                                         address=self.maillist_address,
                                         member_address=self.mailing_lists_members_data["address"])
        req = self.client.lists_members.create(domain=self.domain,
                                               address=self.maillist_address,
                                               data=self.mailing_lists_members_data)

        self.assertEqual(req.status_code, 200)
        self.assertIn("member", req.json())

    def test_maillists_lists_members_update(self):
        self.client.lists_members.create(domain=self.domain,
                                         address=self.maillist_address,
                                         data=self.mailing_lists_members_data)

        req = self.client.lists_members.put(domain=self.domain,
                                            address=self.maillist_address,
                                            data=self.mailing_lists_members_put_data,
                                            member_address=self.mailing_lists_members_data["address"])

        self.assertEqual(req.status_code, 200)
        self.assertIn("member", req.json())

    def test_maillists_lists_members_delete(self):
        self.client.lists_members.create(domain=self.domain,
                                         address=self.maillist_address,
                                         data=self.mailing_lists_members_data)

        req = self.client.lists_members.delete(domain=self.domain,
                                          address=self.maillist_address,
                                          member_address=self.mailing_lists_members_data["address"])
        self.assertEqual(req.status_code, 200)

    def test_maillists_lists_members_create_mult(self):
        req = self.client.lists_members.create(domain=self.domain,
                                               address=self.maillist_address,
                                               data=self.mailing_lists_members_data_mult,
                                               multiple=True)

        self.assertEqual(req.status_code, 200)
        self.assertIn("message", req.json())


if __name__ == '__main__':
    unittest.main()
