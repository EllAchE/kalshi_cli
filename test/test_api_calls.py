import unittest

# Requires auth in order to run unit tests, even on getMarkets which should be unauthed
from kalshi.auth_methods import getValidUserIdAndCookie
from kalshi.get_all_markets import getAllMarkets
from kalshi.get_market import printMarketOrderBook, getMarketByTicker
from kalshi.get_positions import getPositions
from kalshi.place_order import placeOrder


class TestApiCalls(unittest.TestCase):
    def testGetAllMarkets(self):
        response = getAllMarkets()
        self.assertEqual("markets", list(response.keys())[0])

    def testGetSingleMarketByTicker(self):
        response = getMarketByTicker("VAXX-006")
        self.assertEqual(response['market']['title'], 'Will over 225 million Americans be vaccinated for COVID-19 by November 1?')

    def testLogin(self):
        user_id, cookie = getValidUserIdAndCookie()
        self.assertNotEqual(user_id, None)
        self.assertNotEqual(cookie, None)

    def testGetSingleMarket(self):
        testMarketId = 'ee1cec6a-c439-44a2-9233-684685476d2a'
        # this is title: 'Will the Consumer Price Index (CPI) increase more than 0.6%?', category: 'Economics'
        noInterest, yesInterest = printMarketOrderBook(testMarketId)
        self.assertEqual(noInterest, None)
        self.assertEqual(yesInterest, None)

    def testGetPositions(self):
        positions = getPositions()
        self.assertEqual(list(positions.keys())[0], 'market_positions')

    # def testPlaceOrder(self):
    #     testMarketTicker = ''
    #     amount = 1
    #     price = 0.01
    #     side = 'yes'
    #     maxCost = 0.02 # optional argument
    #     sellPositionCapped = None # optional argument
    #     expiration = 1 # order lasts for one second if set this way
    #
    #     # no asserts
    #     testOrder = placeOrder(amount, testMarketId, price, side, expiration, maxCost, sellPositionCapped)
    #     self.assertEqual(testOrder['code'], 'invalid_content_type')
