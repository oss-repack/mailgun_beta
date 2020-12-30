#!/usr/bin/env python
# coding=utf-8

import json
import logging

import requests
from requests.compat import urljoin
import urllib.parse
# from .utils.version import get_version

requests.packages.urllib3.disable_warnings()


class Config(object):
    DEFAULT_API_URL = 'https://api.mailgun.net/'
    API_REF = 'http://dev.mailjet.com/email-api/v3/'
    version = 'v3'
    user_agent = 'mailjet-apiv3-python/v1' #+ get_version()

    def __init__(self, version=None, api_url=None):
        if version is not None:
            self.version = version
        # if domain is None:
        #     raise ApiError("Domain is missing!")
        # else:
        #     self.domain = domain
        self.api_url = api_url or self.DEFAULT_API_URL

    def __getitem__(self, key):
        # Append version to URL.
        # Forward slash is ignored if present in self.version.
        url = urljoin(self.api_url, self.version + '/')
        # print(key)
        headers = {'User-agent': self.user_agent}
        modified = False
        #### Domains section
        if key.lower() == 'domainlist':
            url = {"base": urljoin(self.api_url, self.version + "/"),
                   "keys": "domainlist"}
            modified = True
        if key.lower() == 'createdomain':
            url = {"base": urljoin(self.api_url, self.version + '/domains/'),
                   "keys": "createdomain"}
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
        if key.lower() == "mimemessage":
            url = {"base": urljoin(self.api_url, self.version + "/"),
                   "keys": ["messages.mime"]}
            modified = True
        if key.lower() == "resendmessage":
            url = {"base": "https://sw.api.mailgun.net/v3/",
                   "keys": ["messages"]}
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
            # url = url + key.split('_')[0].lower()
        return url, headers


class Endpoint(object):

    def __init__(self, url, headers, auth, action=None):
        self._url, self.headers, self._auth, self.action = url, headers, auth, action

    def __doc__(self):
        return self._doc

    def get(self, params=None, domain=None, action_id=None, id=None, **kwargs):
        return api_call(self._auth, 'get', self._url, domain=domain, headers=self.headers, action=self.action, action_id=action_id, params=params, resource_id=id, **kwargs)

    # def get_many(self, params=None, action_id=None, **kwargs):
    #     return self._get(params=params, action_id=action_id **kwargs)

    # def get(self, id=None, params=None, domain=None, action_id=None, **kwargs):
    #     return self._get(id=id, params=params, domain=domain, action_id=action_id, **kwargs)

    def create(self, data=None, filters=None, id=None, domain=None, headers=None, action_id=None, files=None, **kwargs):
        if "Content-type" in self.headers:
            if self.headers['Content-type'] == 'application/json':
                data = json.dumps(data)
        elif headers:
            if headers == 'application/json':
                data = json.dumps(data)
                print(data)
                self.headers['Content-type'] = 'application/json'
            elif headers == 'multipart/form-data':
                self.headers['Content-type'] = 'multipart/form-data'
        return api_call(self._auth, 'post', self._url, files=files, domain=domain, headers=self.headers, resource_id=id, data=data, action=self.action, action_id=action_id, filters=filters, **kwargs)

    def put(self, data=None, filters=None, action_id=None, **kwargs):
        # if self.headers['Content-type'] == 'application/json':
        #     data = json.dumps(data)
        return api_call(self._auth, 'put', self._url, headers=self.headers, data=data, action=self.action, action_id=action_id, filters=filters, **kwargs)

    def patch(self, data=None, filters=None, action_id=None, **kwargs):
        # if self.headers['Content-type'] == 'application/json':
        #     data = json.dumps(data)
        return api_call(self._auth, 'patch', self._url, headers=self.headers, data=data, action=self.action, action_id=action_id, filters=filters, **kwargs)

    def update(self, id, data, filters=None, action_id=None, **kwargs):
        if self.headers['Content-type'] == 'application/json':
            data = json.dumps(data)
        return api_call(self._auth, 'put', self._url, resource_id=id, headers=self.headers, data=data, action=self.action, action_id=action_id, filters=filters, **kwargs)

    def delete(self, domain=None, **kwargs):
        return api_call(self._auth, 'delete', self._url, action=self.action, headers=self.headers, domain=domain, **kwargs)


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
        url, headers = self.config[name]
        return type(fname, (Endpoint,), {})(url=url, headers=headers, action=action, auth=self.auth)


def api_call(auth, method, url, headers, data=None, filters=None, params=None, resource_id=None,
             timeout=60, debug=False, action=None, files=None, action_id=None, domain=None, **kwargs):

    url = build_url(url, domain=domain, method=method, **kwargs)
    req_method = getattr(requests, method)

    try:
        filters_str = None
        if filters:
            filters_str = "&".join("%s=%s" % (k, v) for k, v in filters.items())

        print(url)
        # print(data)
        # print(headers)
        # print(auth)
        # print(method)
        # print(params)
        response = req_method(url, data=data, params=filters, headers=headers, auth=auth,
                              timeout=timeout, files=files, verify=True, stream=False)
        print(response.url)
        # print(response.text)
        # print(response.content)
        # print(response.status_code)
        return response

    except requests.exceptions.Timeout:
        raise TimeoutError
    except requests.RequestException as e:
        raise ApiError(e)
    except Exception as e:
        raise


# def build_headers(resource, action=None, extra_headers=None):
#     headers = {'Content-type': 'application/json'}
#
#     if resource.lower() == 'contactslist' and action.lower() == 'csvdata':
#         headers = {'Content-type': 'text/plain'}
#     elif resource.lower() == 'batchjob' and action.lower() == 'csverror':
#         headers = {'Content-type': 'text/csv'}
#
#     if extra_headers:
#         headers.update(extra_headers)
#
#     return headers

def convert_keys(keys):
    print(len(keys))

    final_keys = ""
    if len(keys) == 1:
        final_keys = "/" + keys[0]
    else:
        for k in keys:
            final_keys += "/" + k

    return final_keys


def build_url(url, domain=None, method=None, **kwargs):

    #### Kwargs parser
    if "storage_url" in kwargs:
        if not domain:
            raise ApiError("Domain is missing!")

        url = url["base"] + domain + "/" + url["keys"] + "/" + kwargs["storage_url"]

    #### Domain parser
    elif url["keys"] == "domainlist" or url["keys"] == "createdomain":
        url = url["base"] + "domains"

    elif "domains" in url["keys"]:
        domains_index = url["keys"].index("domains")
        url["keys"].pop(domains_index)
        if url["keys"]:
            final_keys = convert_keys(url["keys"])
            if not domain:
                raise ApiError("Domain is missing!")
            if "login" in kwargs:
                url = url["base"] + domain + final_keys + "/" + kwargs["login"]
            elif "ip" in kwargs:
                url = url["base"] + domain + final_keys + "/" + kwargs["ip"]
            elif "api_storage_url" in kwargs:
                url = kwargs["api_storage_url"]
            else:
                url = url["base"] + domain + final_keys
        else:
            if method in ["get", "post", "delete"]:
                if method == "delete":
                    url = url["base"] + domain
                else:
                    url = url["base"][:-1]
            else:
                url = url["base"] + domain
    elif "ips" in url["keys"]:
        final_keys = convert_keys(url["keys"])
        if "ip" in kwargs:
            url = url["base"][:-1] + final_keys + "/" + kwargs["ip"]
        else:
            url = url["base"][:-1] + final_keys
    elif "ip_pools" in url["keys"]:
        final_keys = convert_keys(url["keys"])
        url = url["base"][:-1] + final_keys
        if "pool_id" in kwargs:

            url = url + "/" + kwargs["pool_id"]
    elif "tags" in url["keys"]:
        final_keys = convert_keys(url["keys"])
        base = url["base"] + domain + "/"
        keys_without_tags = url["keys"][1:]
        url = url["base"] + domain + final_keys
        if "tag_name" in kwargs:
            if "stats" in final_keys:
                final_keys = convert_keys(keys_without_tags)
                url = base + "tags" + "/" + urllib.parse.quote(kwargs["tag_name"]) + final_keys
            else:
                url = url + "/" + urllib.parse.quote(kwargs["tag_name"])
    elif "bounces" in url["keys"]:
        final_keys = convert_keys(url["keys"])
        if "bounce_address" in kwargs:
            url = url["base"] + domain + final_keys + "/" + kwargs["bounce_address"]
        else:
            url = url["base"] + domain + final_keys
    elif "unsubscribes" in url["keys"]:
        final_keys = convert_keys(url["keys"])
        if "unsubscribe_address" in kwargs:
            url = url["base"] + domain + final_keys + "/" + kwargs["unsubscribe_address"]
        else:
            url = url["base"] + domain + final_keys
    elif "complaints" in url["keys"]:
        final_keys = convert_keys(url["keys"])
        if "complaint_address" in kwargs:
            url = url["base"] + domain + final_keys + "/" + kwargs["complaint_address"]
        else:
            url = url["base"] + domain + final_keys
    elif "whitelists" in url["keys"]:
        final_keys = convert_keys(url["keys"])
        if "whitelist_address" in kwargs:
            url = url["base"] + domain + final_keys + "/" + kwargs["whitelist_address"]
        else:
            url = url["base"] + domain + final_keys
    elif "routes" in url["keys"]:
        final_keys = convert_keys(url["keys"])
        if "rout_id" in kwargs:
            url = url["base"][:-1] + final_keys + "/" + kwargs["rout_id"]
        else:
            url = url["base"][:-1] + final_keys
    elif "lists" in url["keys"]:
        final_keys = convert_keys(url["keys"])
        if "validate" in kwargs:
            url = url["base"][:-1] + final_keys + "/" + kwargs["address"] + "/" + "validate"
        elif "multiple" in kwargs and "address" in kwargs:
            if kwargs["multiple"]:
                url = url["base"][:-1] + "/lists/" + kwargs["address"] + "/members.json"
        elif "members" in final_keys and "address" in kwargs:
            members_keys = convert_keys(url["keys"][1:])
            if "member_address" in kwargs:
                url = url["base"][:-1] + "/lists/" + kwargs["address"] + members_keys + \
                      "/" + kwargs["member_address"]
            else:
                url = url["base"][:-1] + "/lists/" + kwargs["address"] + members_keys
        elif "address" in kwargs and not "validate" in kwargs:
            url = url["base"][:-1] + final_keys + "/" + kwargs["address"]

        else:
            url = url["base"][:-1] + final_keys
    elif "templates" in url["keys"]:
        final_keys = convert_keys(url["keys"])
        if "template_name" in kwargs:
            if "versions" in kwargs:
                if kwargs["versions"]:
                    if "tag" in kwargs:
                        url = url["base"] + domain + final_keys + "/" + \
                              kwargs["template_name"] + "/versions/" + kwargs["tag"]
                    else:
                        url = url["base"] + domain + final_keys + "/" + kwargs["template_name"] + "/versions"
                else:
                    raise ApiError("Versions should be True or absent")
            else:
                url = url["base"] + domain + final_keys + "/" + kwargs["template_name"]
        else:
            url = url["base"] + domain + final_keys
    elif "addressvalidate" in url["keys"]:
        final_keys = convert_keys(url["keys"][1:])
        if "list_name" in kwargs:
            url = url["base"] + final_keys + "/" + kwargs["list_name"]
        else:
            url = url["base"] + final_keys
    else:
        if not domain:
            raise ApiError("Domain is missing!")

        final_keys = convert_keys(url["keys"])
        url = url["base"] + domain + final_keys

    return url


def parse_response(response, debug=False):
    data = response.json()

    if debug:
        logging.debug('REQUEST: %s' % response.request.url)
        logging.debug('REQUEST_HEADERS: %s' % response.request.headers)
        logging.debug('REQUEST_CONTENT: %s' % response.request.body)

        logging.debug('RESPONSE: %s' % response.content)
        logging.debug('RESP_HEADERS: %s' % response.headers)
        logging.debug('RESP_CODE: %s' % response.status_code)

    return data


class ApiError(Exception):
    pass


class AuthorizationError(ApiError):
    pass


class ActionDeniedError(ApiError):
    pass


class CriticalApiError(ApiError):
    pass


class ApiRateLimitError(ApiError):
    pass


class TimeoutError(ApiError):
    pass


class DoesNotExistError(ApiError):
    pass


class ValidationError(ApiError):
    pass
