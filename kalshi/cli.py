import argparse
import logging

from get_market import printMarketOrderBook
from get_positions import getPositions
from place_order import placeOrder
from utils import getHelpMessage, printHelpCommands

logging.basicConfig(filename='logs.log', level=logging.INFO)
logger = logging.getLogger(__name__)

def entryMain():
    parser = argparse.ArgumentParser(prog='kalshi')
    sub_parser = parser.add_subparsers(dest='subparser_name')

    sub_parser.add_parser('help', help=getHelpMessage())

    expirationHelpMessage = "Time in seconds until the order expires. If unspecified order will not expire."
    sellPositionCappedHelpMessage = "Specifies whether the order place count should be capped by the members current position." \
                            "Must be 'y' or 'n' for true or false."

    buy_parser = sub_parser.add_parser('buy', help='Buy Shares')
    buy_parser.add_argument('-amount', help="Amount of shares to buy", type=int, required=True)
    buy_parser.add_argument('-id', help="ID of market choice", type=int, required=True)
    buy_parser.add_argument('-price', help="Price to buy shares at", type=float, required=True)
    buy_parser.add_argument('-side', help="Specify if you are buying yes or no shares. input a 'y' or 'n'", type=str, required=True)
    buy_parser.add_argument('-expiration', help=expirationHelpMessage, type=float, required=False)
    buy_parser.add_argument('-maxCost', help="The most that will be paid for an order.", type=float, required=False)
    buy_parser.add_argument('-sellPositionCapped', help=sellPositionCappedHelpMessage, type=float, required=False)

    sell_parser = sub_parser.add_parser('sell', help='Sell Shares')
    sell_parser.add_argument('-amount', help="Amount of shares to sell", type=int, required=True)
    sell_parser.add_argument('-id', help="ID of market choice", type=int, required=True)
    sell_parser.add_argument('-price', help="Price to buy shares at", type=float, required=True)
    sell_parser.add_argument('-side', help="Specify if you are buying yes or no shares. input a 'y' or 'n'", type=str, required=True)
    sell_parser.add_argument('-expiration', help=expirationHelpMessage, type=float, required=False)
    sell_parser.add_argument('-maxCost', help="The most that will be paid for an order.", type=float, required=False)
    sell_parser.add_argument('-sellPositionCapped', help=sellPositionCappedHelpMessage, type=float, required=False)

    market_parser = sub_parser.add_parser('getMarket', help='Get Market Details')
    market_parser.add_argument('-id', help="Id of the market to retrieve details for", required=True)

    sub_parser.add_parser('positions', help='List open positions')

    args = parser.parse_args()

    if args.subparser_name in ['buy', 'sell']: # todo add common logic here
        parseBuyAndSell(args)

    elif args.subparser_name in ['getMarket']:
        parseGetMarket(args)

    elif args.subparser_name in ['positions']:
        try:
            getPositions()
        except AttributeError as e:
            logger.error(e)
            exit()

    else: # Assumes user either sent the help command or malformed the request
        printHelpCommands()


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
        placeOrder(amount, marketId, price, side, expiration, maxCost, sellPositionCapped)
        # need to implement logic still

    elif args.subparser_name == 'sell':
        placeOrder(amount, marketId, price, side, expiration, maxCost, sellPositionCapped)
        pass
    try:
        pass
    except AttributeError as e:
        logger.error(e)
        exit()


if __name__ == '__main__':
    entryMain()