import json
from urllib.parse import urljoin

import requests

from mailgun.handlers.default_handler import handle_default
from mailgun.handlers.domains_handler import handle_domainlist
from mailgun.handlers.domains_handler import handle_domains
from mailgun.handlers.email_validation_handler import handle_address_validate
from mailgun.handlers.error_handler import ApiError
from mailgun.handlers.inbox_placement_handler import handle_inbox
from mailgun.handlers.ip_pools_handler import handle_ippools
from mailgun.handlers.ips_handler import handle_ips
from mailgun.handlers.mailinglists_handler import handle_lists
from mailgun.handlers.messages_handler import handle_resend_message
from mailgun.handlers.routes_handler import handle_routes
from mailgun.handlers.suppressions_handler import handle_bounces
from mailgun.handlers.suppressions_handler import handle_complaints
from mailgun.handlers.suppressions_handler import handle_unsubscribes
from mailgun.handlers.suppressions_handler import handle_whitelists
from mailgun.handlers.tags_handler import handle_tags
from mailgun.handlers.templates_handler import handle_templates


# requests.packages.urllib3.disable_warnings()

HANDLERS = {"resendmessage": handle_resend_message,
            "domains": handle_domains,
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
            "inbox": handle_inbox,
            "messages": handle_default,
            "messages.mime": handle_default,
            "events": handle_default,
            "stats": handle_default}


class Config:
    """
    Config class. Configure client with basic (urls, version, headers)
    """
    DEFAULT_API_URL = "https://api.mailgun.net/"
    API_REF = "https://documentation.mailgun.com/en/latest/api_reference.html"
    version = "v3"
    user_agent = "mailgun-api-python/"

    def __init__(self, version=None, api_url=None):
        """
        Set version and api_url
        :param version: API version (default: v3)
        :type version: str
        :param api_url: API base url
        :type api_url: str
        """
        if version is not None:
            self.version = version

        self.ex_handler = True
        self.api_url = api_url or self.DEFAULT_API_URL

    def __getitem__(self, key):
        """
        Parse incoming splitted attr name, check it and prepare endpoint url.
        Most urls generated here can't be generated dynamically as we are doing this
        in build_url() method under Endpoint class.
        :param key: incoming attr name
        :type key: str
        :return: url, headers
        """
        # Append version to URL.
        # Forward slash is ignored if present in self.version.
        url = urljoin(self.api_url, self.version + "/")
        headers = {"User-agent": self.user_agent}
        modified = False
        # Domains section
        if key.lower() == "domainlist":
            url = {"base": urljoin(self.api_url, self.version + "/"),
                   "keys": ["domainlist"]}
            modified = True
        if "domains" in key.lower():
            splitted = [key.lower()]
            if "_" in key.lower():
                splitted = key.split("_")
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
        # Messages section
        if key.lower() == "messages":
            url = {"base": urljoin(self.api_url, self.version + "/"),
                   "keys": ["messages"]}
        if key.lower() == "mimemessage":
            url = {"base": urljoin(self.api_url, self.version + "/"),
                   "keys": ["messages.mime"]}
            modified = True
        if key.lower() == "resendmessage":
            url = {"keys": ["resendmessage"]}
            modified = True

        # IPpools section
        if key.lower() == "ippools":
            url = {"base": urljoin(self.api_url, self.version + "/"),
                   "keys": ["ip_pools"]}
            modified = True
        # Email Validation section
        if "addressvalidate" in key.lower():
            url = {"base": urljoin(self.api_url, "v4" + "/address/validate"),
                   "keys": key.split("_")}
            modified = True

        if not modified:
            url = urljoin(self.api_url, self.version + "/")
            url = {"base": url,
                   "keys": key.split("_")}
        return url, headers


class Endpoint:
    """
    Generate request and return response
    """

    def __init__(self, url, headers, auth):
        """
        :param url: URL dict with pairs {"base": "keys"}
        :type url: dict
        :param headers: Headers dict
        :type headers: dict
        :param auth: requests auth tuple
        :type auth: tuple
        """
        self._url = url
        self.headers = headers
        self._auth = auth

    def api_call(self, auth, method, url, headers, data=None, filters=None, timeout=60,
                 files=None, domain=None, **kwargs):
        """
        Build URL and make a request
        :param auth: auth data
        :type auth: tuple
        :param method: request method
        :type method: str
        :param url: incoming url (base+keys)
        :type url: dict
        :param headers: incoming headers
        :type headers: dict
        :param data: incoming post/put data
        :type data: dict
        :param filters: incoming params
        :type filters: dict
        :param timeout: requested timeout (60-default)
        :type timeout: int
        :param files: incoming files
        :type files: dict
        :param domain: incoming domain
        :type domain: str
        :param kwargs: kwargs
        :return: server response from API
        """
        url = self.build_url(url, domain=domain, method=method, **kwargs)
        req_method = getattr(requests, method)

        try:
            return req_method(
                url,
                data=data,
                params=filters,
                headers=headers,
                auth=auth,
                timeout=timeout,
                files=files,
                verify=True,
                stream=False)

        except requests.exceptions.Timeout:
            raise TimeoutError
        except requests.RequestException as e:
            raise ApiError(e)
        except Exception as e:
            raise e

    @staticmethod
    def build_url(url, domain=None, method=None, **kwargs):
        """
        Build final request url using predefined handlers.
        Note: Some urls are being built in Config class, as they can't be generated dynamically.
        :param url: incoming url (base+keys)
        :type url: dict
        :param domain: incoming domain
        :type domain: str
        :param method: requested method
        :type method: str
        :param kwargs: kwargs
        :return: builded URL
        """

        return HANDLERS[url["keys"][0]](url, domain, method, **kwargs)

    def get(self, filters=None, domain=None, **kwargs):
        """
        GET method for API calls
        :param filters: incoming params
        :type filters: dict
        :param domain: incoming domain
        :type domain: str
        :param kwargs: kwargs
        :return: api_call GET request
        """
        return self.api_call(self._auth, "get", self._url,
                             domain=domain, headers=self.headers,
                             filters=filters, **kwargs)

    def create(self, data=None, filters=None, domain=None,
               headers=None, files=None, **kwargs):
        """
        POST method for API calls
        :param data: incoming post data
        :type data: dict
        :param filters: incoming params
        :type filters: dict
        :param domain: incoming domain
        :type domain: str
        :param headers: incoming headers
        :type headers: dict
        :param files: incoming files
        :type files: file
        :param kwargs: kwargs
        :return: api_call POST request
        """
        if "Content-type" in self.headers:
            if self.headers["Content-type"] == "application/json":
                data = json.dumps(data)
        elif headers:
            if headers == "application/json":
                data = json.dumps(data)
                self.headers["Content-type"] = "application/json"
            elif headers == "multipart/form-data":
                self.headers["Content-type"] = "multipart/form-data"

        return self.api_call(self._auth, "post", self._url, files=files,
                             domain=domain, headers=self.headers,
                             data=data, filters=filters, **kwargs)

    def put(self, data=None, filters=None, **kwargs):
        """
        PUT method for API calls
        :param data: incoming data
        :type data: dict
        :param filters: incoming params
        :type filters: dict
        :param kwargs: kwargs
        :return: api_call POST request
        """
        return self.api_call(self._auth, "put", self._url, headers=self.headers,
                             data=data, filters=filters, **kwargs)

    def patch(self, data=None, filters=None, **kwargs):
        """
        PATCH method for API calls
        :param data: incoming data
        :type data: dict
        :param filters: incoming params
        :type filters: dict
        :param kwargs: kwargs
        :return: api_call PATCH request
        """
        return self.api_call(self._auth, "patch", self._url, headers=self.headers,
                             data=data, filters=filters, **kwargs)

    def update(self, data, filters=None, **kwargs):
        """
        PUT method for API calls
        :param data: incoming data
        :type data: dict
        :param filters: incoming params
        :type filters: dict
        :param kwargs: kwargs
        :return: api_call PUT request
        """
        if self.headers["Content-type"] == "application/json":
            data = json.dumps(data)
        return self.api_call(self._auth, "put", self._url, headers=self.headers,
                             data=data, filters=filters, **kwargs)

    def delete(self, domain=None, **kwargs):
        """
        DELETE method for API calls
        :param domain: incoming domain
        :type domain: str
        :param kwargs: kwargs
        :return: api_call DELETE request
        """
        return self.api_call(self._auth, "delete", self._url,
                             headers=self.headers, domain=domain, **kwargs)


class Client:
    """
    Client class
    """

    def __init__(self, auth=None, **kwargs):
        """
        :param auth: auth set ("username", "APIKEY")
        :type auth: set
        :param kwargs: kwargs
        """
        self.auth = auth
        version = kwargs.get("version", None)
        api_url = kwargs.get("api_url", None)
        self.config = Config(version=version, api_url=api_url)

    def __getattr__(self, name):
        """
        Get named attribute of an object, split it and execute
        :param name: attribute name (Example: client.domains_ips. names: ["domains", "ips"])
        :type name: str
        :return: type object (executes existing handler)
        """
        split = name.split("_")
        # identify the resource
        fname = split[0]
        url, headers = self.config[name]
        return type(fname, (Endpoint,), {})(url=url, headers=headers, auth=self.auth)
