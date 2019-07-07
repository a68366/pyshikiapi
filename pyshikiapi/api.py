import re

from requests_oauthlib import OAuth2Session

from pyshikiapi.request import Request


class API:
    AUTHORIZATION_URL = 'https://shikimori.one/oauth/authorize'
    TOKEN_URL = 'https://shikimori.one/oauth/token'
    API_V1_URL = 'https://shikimori.one/api'
    API_V2_URL = 'https://shikimori.one/api/v2'

    def __init__(self, app_name, client_id, client_secret,
                 token=None, token_update_callback=None,
                 redirect_uri='urn:ietf:wg:oauth:2.0:oob'):
        """
        :param app_name: Your application name. Create one here: https://shikimori.one/oauth/applications
        :param client_id: ID of your application. Find it on your application page.
        :param client_secret: Secret of your application. Find it on your application page.
        :param token: Oauth access token.
        :param token_update_callback: A function that accepts 1 argument (dict-like token object).
        It is called when token changes, e.g. when fetch_token() is called or when token auto-refresh happens.
        :param redirect_uri: Where to redirect authenticated user.
        You can point at your webserver to receive user auth code.
        """

        self.app_name = app_name
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_update_callback = token_update_callback
        self.redirect_uri = redirect_uri

        self._headers = {'User-Agent': app_name}
        self._refresh_args = {'client_id': self.client_id,
                              'client_secret': self.client_secret}
        self._session = self._make_session(token)

    @property
    def token(self):
        return self._session.token

    @property
    def authorization_url(self):
        return self._session.authorization_url(self.AUTHORIZATION_URL)[0]

    def fetch_token(self, code):
        """
        :param code: Authentication code, obtained from user
        """

        self._session.fetch_token(self.TOKEN_URL, code=code,
                                  client_secret=self.client_secret,
                                  headers=self._headers)
        if self.token_update_callback:
            self.token_update_callback(self.token)

    def _make_session(self, token=None):
        session = OAuth2Session(client_id=self.client_id,
                                redirect_uri=self.redirect_uri,
                                auto_refresh_url=self.TOKEN_URL,
                                auto_refresh_kwargs=self._refresh_args,
                                token_updater=self.token_update_callback,
                                token=token)
        session.headers.update(self._headers)
        return session

    def _send_request(self, method, path, **kwargs):
        if is_v2(path):
            url = self.API_V2_URL + '/' + path
        else:
            url = self.API_V1_URL + '/' + path
        if method == 'GET':
            response = self._session.request(method, url, params=kwargs)
        else:
            response = self._session.request(method, url, json=kwargs)

        if response.ok and 'application/json' in response.headers.get('Content-Type', ''):
            return response.json()
        else:
            response.raise_for_status()

    def __getattr__(self, name):
        return Request(self, name)

    def __repr__(self):
        return '<pyshikiapi-API app_name={0}, token={1}>'.format(self.app_name, self.token)


def is_v2(path):
    """
    Some methods of the api are implemented in api version 2.
    More info here: https://shikimori.one/api/doc/2.0

    :param path: request path
    :return: True if path belongs to version 2 of the api, False otherwise
    """

    patterns = [r'users/signup', r'abuse_requests.*', r'users/\d+/ignore',
                r'topics/\d+/ignore', r'user_rates(/\d+.*)?',
                r'episode_notifications']
    return any(re.fullmatch(r, path) for r in patterns)
