import argparse
import logging

from api_methods.place_order import placeOrder

logging.basicConfig(filename='logs.log', level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(prog="kalshi")
    sub_parser = parser.add_subparsers(dest='subparser_name')

    buy_parser = sub_parser.add_parser('buy', help='Buy Shares')
    buy_parser.add_argument('-amount', help="Amount of shares to buy", type=int, required=True)
    buy_parser.add_argument('-id', help="ID of market choice", type=int, required=True)
    buy_parser.add_argument('-price', help="Price to buy shares at", type=float, required=True)
    buy_parser.add_argument('-side', help="Specify if you are buying yes or no shares. input a 'y' or 'n'", type=string, required=True)
    buy_parser.add_argument('-expiration', help="Time in seconds until the order expires. If unspecified order will not expire.", type=float, required=False)
    buy_parser.add_argument('-maxCost', help="The most that will be paid for an order.", type=float, required=False)
    buy_parser.add_argument('-sellPositionCapped', help="Specifies whether the order place count should be capped by the members current position. Must be 'y' or 'n' for true or false.", type=float, required=False)

    sell_parser = sub_parser.add_parser('sell', help='Sell Shares')
    sell_parser.add_argument('-amount', help="Amount of shares to sell", type=int, required=True)
    sell_parser.add_argument('-id', help="ID of market choice", type=int, required=True)
    sell_parser.add_argument('-price', help="Price to buy shares at", type=float, required=True)
    sell_parser.add_argument('-side', help="Specify if you are buying yes or no shares. input a 'y' or 'n'", type=string, required=True)
    sell_parser.add_argument('-expiration', help="Time in seconds until the order expires. If unspecified order will not expire.", type=float, required=False)
    sell_parser.add_argument('-maxCost', help="The most that will be paid for an order.", type=float, required=False)
    sell_parser.add_argument('-sellPositionCapped', help="Specifies whether the order place count should be capped by the members current position. Must be 'y' or 'n' for true or false.", type=float, required=False)

    market_parser = sub_parser.add_parser('getMarket', help='Get Market Details')
    market_parser.add_argument('-id', help="Id of the market to retrieve details for", required=True)

    sub_parser.add_parser('positions', help='List open positions')

    args = parser.parse_args()

    if args.subparser_name in ['buy', 'sell']: # todo add common logic here
        try:
            pass
        except AttributeError as e:
            logger.error(e)
            exit()

    elif args.subparser_name in ['getMarket']:
        try:
            id  = args.id
        except AttributeError as e:
            logger.error(e)
            exit()

    if args.subparser_name == 'buy':
        try:
            count = args.count
            marketId = args.marketId
            price = args.price
            side = args.side
            expiration = args.expiration
            maxCost = args.maxCost
            sellPositionCapped = args.sellPositionCapped
        except AttributeError as e:
            logger.error(e)
            exit()

        if(count < 0):
            logger.warning("Count must be greater than 0")
        placeOrder(userId, cookie, count, marketId, price, side, expiration, maxCost, sellPositionCapped)
        # need to implement logic still
        pass

    elif args.subparser_name == 'sell':
        pass

    elif args.subparser_name == 'positions':
        pass
