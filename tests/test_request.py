from unittest import TestCase

from pyshikiapi.request import Request


class TestRequest(TestCase):
    def setUp(self):
        self.req = Request(None, '')

    def test__path(self):
        self.assertEqual(self.req._path, '')
        self.assertEqual(self.req.animes._path, '/animes')
        self.assertEqual(self.req.animes.roles._path, '/animes/roles')
        self.assertEqual(self.req.animes(1).roles._path, '/animes/1/roles')
        self.assertEqual(self.req.users(3).friends._path, '/users/3/friends')
        self.assertEqual(self.req().path()._path, self.req.path._path)
