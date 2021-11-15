import unittest

from api_methods.get_all_markets import getAllMarkets

# Requires auth in order to run unit tests, even on getMarkets which should be unauthed
class TestUnauthedApiCalls(unittest.TestCase):
    def testGetAllMarkets(self):
        response = getAllMarkets()
        self.assertEqual("abc", response)