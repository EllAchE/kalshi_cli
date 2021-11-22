import argparse

from kalshi.get_market import printMarketOrderBook
from kalshi.get_positions import getPositions
from kalshi.place_order import placeOrder
from kalshi.utils import getHelpMessage, printHelpCommands, generateExpirationSeconds
from kalshi.logger import LOG

def createParsers():
    baseParser = argparse.ArgumentParser(prog='kalshi')
    subParser = baseParser.add_subparsers(dest='subparser_name')

    subParser.add_parser('help', help=getHelpMessage())

    buyParser = subParser.add_parser('buy', help='Buy Shares')
    addOrderPlacingArguments(buyParser)
    buyParser.add_argument('-a', help="Amount of shares to buy", type=int, required=True)
    buyParser.add_argument('-p', help="Price to buy shares at", type=float, required=True)
    buyParser.add_argument('-s', help="Specify if you are buying yes or no shares. input a 'y' or 'n'", type=str, required=True)

    sellParser = subParser.add_parser('sell', help='Sell Shares')
    addOrderPlacingArguments(sellParser)
    sellParser.add_argument('-a', help="Amount of shares to sell", type=int, required=True)
    sellParser.add_argument('-p', help="Price to sell shares at", type=float, required=True)
    sellParser.add_argument('-s', help="Specify if you are selling yes or no shares. input a 'y' or 'n'", type=str, required=True)

    mktParser = subParser.add_parser('getMarket', help='Get Market Details')
    mktParser.add_argument('-id', help="Id of the market to retrieve details for", required=True)
    # todo switch this to ticker based

    subParser.add_parser('positions', help='List open positions')

    args = baseParser.parse_args()

    if args.subparser_name in ['buy', 'sell']: # todo add common logic here
        parseBuyAndSell(args)

    elif args.subparser_name == 'getMarket':
        parseGetMarket(args)

    elif args.subparser_name == 'positions':
        try:
            getPositions()
        except AttributeError as e:
            LOG.error(e)
            exit()

    else: # Assumes user either sent the help command or malformed the request
        printHelpCommands()


def addOrderPlacingArguments(parser):
    expirationHelpMessage = "Time in {} until the order expires. If unspecified order will not expire."
    sellPositionCappedHelpMessage = "Specifies whether the order place count should be capped by the members current position." \
                            "Must be 'y' or 'n' for true or false."
    parser.add_argument('-id', help="ID of market choice. Must specify this or ticker", type=str, required=False)
    parser.add_argument('-ti', help="Ticker of market choice. Must specify this or id", type=str, required=False)
    parser.add_argument('-es', help=expirationHelpMessage.format('seconds'), type=float, required=False)
    parser.add_argument('-em', help=expirationHelpMessage.format('minutes'), type=float, required=False)
    parser.add_argument('-eh', help=expirationHelpMessage.format('hours'), type=float, required=False)
    parser.add_argument('-ed', help=expirationHelpMessage.format('days'), type=float, required=False)
    parser.add_argument('-max', help="The most that will be paid for an order.", type=float, required=False)
    parser.add_argument('-sellCap', help=sellPositionCappedHelpMessage, type=float, required=False)


def parseGetMarket(args):
    try:
        marketId = args.id
        printMarketOrderBook(marketId)
    except AttributeError as e:
        LOG.error(e)
        exit()
    except Exception as e:
        LOG.error(e)
        exit()

def parseBuyAndSell(args):
    try:
        exSeconds = args.es
        exMinutes = args.em
        exHours = args.eh
        exDays = args.ed
        expiration = generateExpirationSeconds(seconds=exSeconds, minutes=exMinutes, hours=exHours, days=exDays)

        amount = args.a
        marketId = args.id
        ticker = args.ti
        price = args.p
        side = args.s
        maxCost = args.max
        sellPositionCapped = args.sellPositionCapped

        if (amount < 0 or amount is None):
            LOG.warning("Amount must be greater than 0")
            exit()
        if (side != 'y' and side != 'n' or side is None):
            LOG.warning("Side must be either 'y' or 'n'")
            exit()
        if (price < 0.01 or price > 0.99 or price is None):
            LOG.warning("Price must be in the range 0.01-0.99, inclusive")
            exit()
        if (marketId is None and ticker is None):
            LOG.warning("Either ticker or id must be specified")
            exit()

        if args.subparser_name == 'sell':
            price = 1 - price
            if side == 'y': # convert to opposite for "sell", as you need to buy opposite side
                side = 'n'
            else:
                side = 'y'
        placeOrder(amount, marketId, price, side, expiration, maxCost, sellPositionCapped)

    except AttributeError as e:
        LOG.error(e)
        exit()
    except Exception as e:
        LOG.error(e)
        exit()



if __name__ == '__main__':
    createParsers()