import unittest

from kalshi.ticker_to_id import getIdFromTicker


class TestApiCalls(unittest.TestCase):
    def testShouldGetIdGivenTicker(self):
        testId = getIdFromTicker('CPI-0001')
        self.assertEqual(testId, 'ee1cec6a-c439-44a2-9233-684685476d2a')

    def testShouldReturnNoneForInvalidTicker(self):
        testId = getIdFromTicker('Fake Ticker')
        self.assertEqual(testId, None)
