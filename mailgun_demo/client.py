#!/usr/bin/env python
# coding=utf-8

import json
import requests
from urllib.parse import urljoin

from messages_handler import handle_resend_message
from domains_handler import handle_domains, handle_domainlist
from ips_handler import handle_ips
from ip_pools_handler import handle_ippools
from tags_handler import handle_tags
from suppressions_handler import handle_bounces, handle_whitelists, \
    handle_complaints, handle_unsubscribes
from routes_handler import handle_routes
from mailinglists_handler import handle_lists
from templates_handler import handle_templates
from email_validation_handler import handle_address_validate
from inbox_placement_handler import handle_inbox
from error_handler import ApiError


requests.packages.urllib3.disable_warnings()

HANDLERS = {"resendmessage": handle_resend_message,
            "domains":handle_domains,
            "domainlist": handle_domainlist,
            "dkim_authority": handle_domains,
            "dkim_selector": handle_domains,
            "web_prefix": handle_domains,
            "ips": handle_ips,
            "ip_pools": handle_ippools,
            "tags": handle_tags,
            "bounces": handle_bounces,
            "unsubscribes": handle_unsubscribes,
            "whitelists": handle_whitelists,
            "complaints": handle_complaints,
            "routes": handle_routes,
            "lists": handle_lists,
            "templates": handle_templates,
            "addressvalidate": handle_address_validate,
            "inbox": handle_inbox}


class Config(object):
    DEFAULT_API_URL = 'https://api.mailgun.net/'
    API_REF = 'https://documentation.mailgun.com/en/latest/api_reference.html'
    version = 'v3'
    user_agent = 'mailgun-apiv3-python/v1' #+ get_version()

    def __init__(self, version=None, api_url=None):
        if version is not None:
            self.version = version

        self.ex_handler = True
        self.api_url = api_url or self.DEFAULT_API_URL

    def __getitem__(self, key):
        # Append version to URL.
        # Forward slash is ignored if present in self.version.
        url = urljoin(self.api_url, self.version + '/')
        headers = {'User-agent': self.user_agent}
        modified = False
        #### Domains section
        if key.lower() == 'domainlist':
            url = {"base": urljoin(self.api_url, self.version + "/"),
                   "keys": ["domainlist"]}
            modified = True
        if 'domains' in key.lower():
            splitted = [key.lower()]
            if "_" in key.lower():
                splitted = key.split('_')
            final_keys = splitted
            if "dkimauthority" in splitted:
                final_keys = ["dkim_authority"]
            elif "dkimselector" in splitted:
                final_keys = ["dkim_selector"]
            elif "webprefix" in splitted:
                final_keys = ["web_prefix"]

            url = {"base": urljoin(self.api_url, self.version + "/domains/"),
                   "keys": final_keys}
            modified = True
        #### Messages section
        if key.lower() == "messages":
            url = {"base": urljoin(self.api_url, self.version + "/"),
                   "keys": ["messages"]}
            self.ex_handler = False
        if key.lower() == "mimemessage":
            url = {"base": urljoin(self.api_url, self.version + "/"),
                   "keys": ["messages.mime"]}
            modified = True
            self.ex_handler = False
        if key.lower() == "resendmessage":
            url = {"keys": ["resendmessage"]}
            self.ex_handler = True
            modified = True

        #### IPpools section
        if key.lower() == "ippools":
            url = {"base": urljoin(self.api_url, self.version + "/"),
                   "keys": ["ip_pools"]}
            modified = True

        if "addressvalidate" in key.lower():
            url = {"base": urljoin(self.api_url, "v4" + "/address/validate"),
                   "keys": key.split('_')}
            modified = True

        if not modified:
            url = urljoin(self.api_url, self.version + '/')
            url = {"base": url,
                   "keys": key.split('_')}
            if url["keys"][0] in HANDLERS:
                self.ex_handler = True
            else:
                self.ex_handler = False
        return url, headers, self.ex_handler


class Endpoint(object):

    def __init__(self, url, headers, auth, ex_handler, action=None):
        self._url = url
        self.headers = headers
        self._auth = auth
        self.ex_handler = ex_handler
        self.action = action

    def __doc__(self):
        return self._doc

    def get(self, params=None, domain=None, action_id=None, id=None, **kwargs):
        return api_call(self._auth, 'get', self._url, domain=domain,
                        headers=self.headers, action=self.action,
                        action_id=action_id, params=params,
                        resource_id=id, ex_handler=self.ex_handler, **kwargs)

    def create(self, data=None, filters=None, id=None, domain=None,
               headers=None, action_id=None, files=None, **kwargs):
        if "Content-type" in self.headers:
            if self.headers['Content-type'] == 'application/json':
                data = json.dumps(data)
        elif headers:
            if headers == 'application/json':
                data = json.dumps(data)
                self.headers['Content-type'] = 'application/json'
            elif headers == 'multipart/form-data':
                self.headers['Content-type'] = 'multipart/form-data'
        return api_call(self._auth, 'post', self._url, files=files,
                        domain=domain, headers=self.headers, resource_id=id,
                        data=data, action=self.action, action_id=action_id,
                        filters=filters, ex_handler=self.ex_handler, **kwargs)

    def put(self, data=None, filters=None, action_id=None, **kwargs):

        return api_call(self._auth, 'put', self._url, headers=self.headers,
                        data=data, action=self.action, action_id=action_id,
                        filters=filters, ex_handler=self.ex_handler, **kwargs)

    def patch(self, data=None, filters=None, action_id=None, **kwargs):

        return api_call(self._auth, 'patch', self._url, headers=self.headers,
                        data=data, action=self.action, action_id=action_id,
                        filters=filters, ex_handler=self.ex_handler, **kwargs)

    def update(self, id, data, filters=None, action_id=None, **kwargs):
        if self.headers['Content-type'] == 'application/json':
            data = json.dumps(data)
        return api_call(self._auth, 'put', self._url, resource_id=id, headers=self.headers,
                        data=data, action=self.action, action_id=action_id,
                        filters=filters, ex_handler=self.ex_handler, **kwargs)

    def delete(self, domain=None, **kwargs):
        return api_call(self._auth, 'delete', self._url, action=self.action,
                        headers=self.headers, domain=domain, ex_handler=self.ex_handler, **kwargs)


class Client(object):

    def __init__(self, auth=None, **kwargs):
        self.auth = auth
        version = kwargs.get('version', None)
        api_url = kwargs.get('api_url', None)
        self.config = Config(version=version, api_url=api_url)

    def __getattr__(self, name):
        split = name.split('_')
        #identify the resource
        fname = split[0]
        action = None
        if (len(split) > 1):
            #identify the sub resource (action)
            action = split[1]
            if action == 'csvdata':
                action = 'csvdata/text:plain'
            if action == 'csverror':
                action = 'csverror/text:csv'
        url, headers, ex_handler = self.config[name]
        return type(fname, (Endpoint,), {})(url=url, headers=headers,
                                            action=action, auth=self.auth, ex_handler=ex_handler)


def api_call(auth, method, url, headers, ex_handler, data=None, filters=None,
             params=None, resource_id=None, timeout=60, debug=False,
             action=None, files=None, action_id=None, domain=None, **kwargs):

    url = build_url(url, ex_handler, domain=domain, method=method, **kwargs)
    req_method = getattr(requests, method)

    try:
        response = req_method(url, data=data, params=filters, headers=headers, auth=auth,
                              timeout=timeout, files=files, verify=True, stream=False)

        return response

    except requests.exceptions.Timeout:
        raise TimeoutError
    except requests.RequestException as e:
        raise ApiError(e)
    except Exception as e:
        raise e


def convert_keys(keys):

    final_keys = ""
    if len(keys) == 1:
        final_keys = "/" + keys[0]
    else:
        for k in keys:
            final_keys += "/" + k

    return final_keys


def build_url(url, ex_handler, domain=None, method=None, **kwargs):
    if ex_handler:
        url = HANDLERS[url["keys"][0]](url, domain, method, **kwargs)
    else:
        if not domain:
            raise ApiError("Domain is missing!")

        final_keys = convert_keys(url["keys"])
        url = url["base"] + domain + final_keys

    return url