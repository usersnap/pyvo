import requests
import purl

import logging

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    '%(levelname)s [%(asctime)s] -- %(message)s'
))
logger.addHandler(handler)
logger.setLevel(logging.WARN)

def debug(*args):
    msg = ", ".join(map(str, args))
    logger.debug(msg)

PIVOTAL_TRACKER_TOKEN = '2a2c2003c8e45a643ad8af2b066b3e71'

class NullReturnedError(Exception):
    pass

class ResourceNotFound(Exception):
    pass

HTTP_VERBS = ('head', 'options', 'get', 'post', 'put', 'patch', 'delete')

class Request(object):
    """docstring for Request"""
    def __init__(self, method=None, session=None,
            auth_callable=(lambda x: x), base_url=None,
            uriparts=None, sent=False):
        self.method = method
        self.session = session
        self.auth_callable = auth_callable
        self.base_url = base_url
        self.uriparts = uriparts or []
        self.baseparts = self.uriparts
        self.sent = sent

    def augment_request(self, arg, reset=False):
        debug("augment_request", reset, arg, self.uriparts, self.baseparts)
        if reset:
            self.uriparts = self.baseparts
            return Request(
                method=self.method,
                session=self.session,
                auth_callable=self.auth_callable,
                base_url=self.base_url,
                uriparts=self.uriparts,
                sent=False
            )
        else:
            self.uriparts.append(arg)
            return self

    @property
    def resource_key(self):
        def filter_(arg):
            try:
                _ = int(arg)
            except ValueError:
                return arg not in HTTP_VERBS
            else:
                return False

        return [p for p in self.uriparts if filter_(p)][-1]

    def _send(self, method, **kwargs):
        return_json = kwargs.pop('return_json', True)

        url = purl.URL(self.base_url)
        # debug(resource_ids)
        debug("entered send", self.uriparts)
        for p in self.uriparts:
            url = url.add_path_segment(p)

        def hook(r, *args, **kwargs):
            r.resource_key = self.resource_key

        hooks = {"response": hook}

        request = requests.Request(method, url, hooks=hooks, **kwargs)

        if self.session is None:
            self.session = requests.Session()

        prepped = self.auth_callable(self.session.prepare_request(request))
        debug(prepped, prepped.url)

        resp = self.session.send(prepped)
        self.sent = True

        if resp.status_code == 404:
            raise ResourceNotFound(resp.content)

        if return_json:
            return resp.json()
        else:
            return resp

    def __getattr__(self, k):
        try:
            return object.__getattr__(self, k)
        except AttributeError:
            return self.augment_request(k, reset=self.sent)

    def __call__(self, id=None, **kwargs):
        if self.uriparts[-1] in HTTP_VERBS:
            method = self.uriparts.pop()
            if id is not None:
                self.augment_request(id)
            return self._send(method, **kwargs)
        else:
            if id is not None:
                return self.augment_request(id, reset=self.sent)
            else:
                return self


class Client(object):
    def __init__(self, token, base_url):
        self.token = token
        self.base_url = base_url
        self.session = requests.Session()

    def token_auth(self, request):
        request.headers.update({
            'x-trackertoken': self.token
        })
        return request

    def request(self, **kwargs):
        return Request(session=self.session, auth_callable=self.token_auth,
            base_url=self.base_url, **kwargs)

    def __getattr__(self, k):
        try:
            return object.__getattr__(self, k)
        except AttributeError:
            request = self.request(uriparts=[k])
            return request


if __name__ == '__main__':
    # client = Client()
    # # resp = client.get('1138154', 'memberships', return_json=False)
    # resp = client.zod(return_json=False)
    # # resp = client.search('1138154', 'type:release', return_json=False)
    # debug(resp.status_code, resp.request.url, resp.content)
    # debug(list((p['username'], p['id']) for p in (m['person'] for m in resp)))
    client = Client(base_url='https://www.pivotaltracker.com/services/v5/',
        token=PIVOTAL_TRACKER_TOKEN)
    req = client.request()
    # resp = req.projects('1138154').labels(9308508).get()
    # resp = req.projects('1138154').labels.get()
    # resp = client.projects('1138154').get()
    project = client.projects('1138154')
    r1 = project.labels.get(return_json=False)
    r2 = project.labels('9308508').get(return_json=False)
    r3 = project.members.get(return_json=False)
    # resp = req.projects.get()
    debug(r1.content, r1.resource_key)
    debug(r2.content, r2.resource_key)
    debug(r3.content, r3.resource_key)