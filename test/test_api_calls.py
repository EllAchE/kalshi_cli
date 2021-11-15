import unittest

from api_methods.get_market import printMarketOrderBook
from api_methods.get_positions import getPositions
from api_methods.place_order import placeOrder
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

    def testGetSingleMarket(self):
        testMarketId = 'ee1cec6a-c439-44a2-9233-684685476d2a'
        # this is title: 'Will the Consumer Price Index (CPI) increase more than 0.6%?', category: 'Economics'
        printMarketOrderBook(testMarketId)

    def testGetPositions(self):
        positions = getPositions()
        print(positions)

    def testPlaceOrder(self):
        testMarketId = ''
        amount = 1
        price = 0.01
        side = 'yes'
        maxCost = 0.02 # optional argument
        sellPositionCapped = None # optional argument
        expiration = 1 # order lasts for one second if set this way

        testOrder = placeOrder(amount, testMarketId, price, side, expiration, maxCost, sellPositionCapped)
