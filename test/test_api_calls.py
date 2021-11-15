import unittest

from auth.auth_methods import getValidUserIdAndCookie
from api_methods.get_all_markets import getAllMarkets

# Requires auth in order to run unit tests, even on getMarkets which should be unauthed
class TestUnauthedApiCalls(unittest.TestCase):
    def testGetAllMarkets(self):
        response = getAllMarkets()
        self.assertEqual("abc", response)

    def testLogin(self):
        user_id, cookie = getValidUserIdAndCookie()
        self.assertNotEqual(user_id, None)
        self.assertNotEqual(cookie, None)
