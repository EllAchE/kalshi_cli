import argparse
import logging

from kalshi.get_market import printMarketOrderBook
from kalshi.get_positions import getPositions
from kalshi.place_order import placeLimitOrder
from kalshi.utils import getHelpMessage, printHelpCommands

logging.basicConfig(filename='logs.log', level=logging.INFO)
logger = logging.getLogger(__name__)

def entryMain():
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
            logger.error(e)
            exit()

    else: # Assumes user either sent the help command or malformed the request
        printHelpCommands()


def addOrderPlacingArguments(parser):
    expirationHelpMessage = "Time in {} until the order expires. If unspecified order will not expire."
    sellPositionCappedHelpMessage = "Specifies whether the order place count should be capped by the members current position." \
                            "Must be 'y' or 'n' for true or false."
    parser.add_argument('-id', help="ID of market choice", type=int, required=True)
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
        logger.error(e)
        exit()
    except Exception as e:
        logger.error(e)
        exit()

def parseBuyAndSell(args):
    try:
        amount = args.amount
        marketId = args.id
        price = args.price
        side = args.side
        expiration = args.expiration
        maxCost = args.maxCost
        sellPositionCapped = args.sellPositionCapped
    except AttributeError as e:
        logger.error(e)
        exit()
    if (amount < 0 or amount is None):
        logger.warning("Amount must be greater than 0")
        exit()
    if (side != 'y' and side != 'n' or side is None):
        logger.warning("Side must be either 'y' or 'n'")
        exit()
    if (price < 0.01 or price > 0.99 or price is None):
        logger.warning("Price must be in the range 0.01-0.99, inclusive")
        exit()
    if (marketId is None):
        logger.warning("Market ID must be defined")
        exit()
    if args.subparser_name == 'buy':
        placeLimitOrder(amount, marketId, price, side, expiration, maxCost, sellPositionCapped)
        # need to implement logic still

    elif args.subparser_name == 'sell':
        placeLimitOrder(amount, marketId, price, side, expiration, maxCost, sellPositionCapped)
    try:
        pass
    except AttributeError as e:
        logger.error(e)
        exit()


if __name__ == '__main__':
    entryMain()