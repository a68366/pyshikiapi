from functools import partial


class Request:
    HTTP_METHODS = ['DELETE', 'GET', 'PATCH', 'POST', 'PUT']

    def __init__(self, api, method_name, parent=None):
        self._api = api
        self._method_name = method_name
        self._parent = parent

    @property
    def _path(self):
        url = []
        current = self
        while current:
            url.append(current._method_name)
            current = current._parent
        return '/'.join(url[::-1])

    def __call__(self, path=None):
        if path:
            self._method_name += '/' + str(path)
        return self

    def __getattr__(self, name):
        if name in self.HTTP_METHODS:
            return partial(self._api._send_request, name, self._path)
        return Request(self._api, name, parent=self)

    def __repr__(self):
        return '<pyshikiapi-Request path={0}>'.format(self._path)
