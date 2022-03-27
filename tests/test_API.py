from unittest import TestCase, mock

from pyshikiapi import API


class TestAPI(TestCase):
    def setUp(self) -> None:
        self.api = API('test', 'test', 'test')

    def test_getattr(self):
        self.assertEqual(self.api.animes._path, 'animes')
        self.assertEqual(self.api.animes.roles._path, 'animes/roles')
        self.assertEqual(self.api.animes(1).roles._path, 'animes/1/roles')
        self.assertEqual(self.api.users(3).friends._path, 'users/3/friends')

    def test_request(self):
        with mock.patch('pyshikiapi.API._send_request') as foo:
            self.api.animes.GET()
            self.assertTrue(foo.called)
