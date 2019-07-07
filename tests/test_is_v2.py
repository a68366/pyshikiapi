from unittest import TestCase

from pyshikiapi.api import is_v2


class TestIsV2(TestCase):
    def test_v2(self):
        """These api methods use api v2 and is_v2 must return True for them"""

        self.assertTrue(is_v2('topics/123/ignore'))
        self.assertTrue(is_v2('users/123/ignore'))
        self.assertTrue(is_v2('abuse_requests/offtopic'))
        self.assertTrue(is_v2('abuse_requests/summary'))
        self.assertTrue(is_v2('abuse_requests/abuse'))
        self.assertTrue(is_v2('abuse_requests/spoiler'))
        self.assertTrue(is_v2('episode_notifications'))
        self.assertTrue(is_v2('users/signup'))
        self.assertTrue(is_v2('user_rates'))
        self.assertTrue(is_v2('user_rates/123'))
        self.assertTrue(is_v2('user_rates/123/increment'))

    def test_v1(self):
        """These api methods use api v1"""

        self.assertFalse(is_v2('users'))
        self.assertFalse(is_v2('users/123'))
        self.assertFalse(is_v2('users/123/friends'))
        self.assertFalse(is_v2('topics'))
        self.assertFalse(is_v2('topics/updates'))
        self.assertFalse(is_v2('topics/123'))
        self.assertFalse(is_v2('user_rates/type/cleanup'))
        self.assertFalse(is_v2('user_rates/type/reset'))
