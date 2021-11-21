import json

from kalshi.get_all_markets import getAllMarkets
from kalshi.logger import LOG


def getIdFromTicker(ticker):
    matchingMarket = findTickerInLocalFile(ticker)
    if matchingMarket is not None:
        return matchingMarket['id']
    else:
        LOG.error("no match found for market with ticker {}, fetching latest and reattempting".format(ticker))
        getAllMarkets()
        matchingMarket = findTickerInLocalFile(ticker)
        if matchingMarket is not None:
            return matchingMarket['id']
        else:
            LOG.error("no match found for market with ticker {} after reattempt".format(ticker))
            return None


def findTickerInLocalFile(ticker):
    with open('data/markets.json') as jsonMarketFile:
        marketsJson = json.load(jsonMarketFile)

    return list(filter(lambda a: a['ticker_name'] == ticker, marketsJson))[0]
