import argparse
import logging

logging.basicConfig(filename='logs.log', level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(prog="kalshi")
    sub_parser = parser.add_subparsers(dest='subparser_name')

    buy_parser = sub_parser.add_parser('buy', help='Buy Shares')
    buy_parser.add_argument('-a', help="Amount of shares to buy", type=float, required=True)
    buy_parser.add_argument('-o', help="Index of outcome choice", type=int, required=True)
    buy_parser.add_argument('-n', help="Minimum number of shares expected (slippage)", type=float, required=True)

    sell_parser = sub_parser.add_parser('sell', help='Sell Shares')
    sell_parser.add_argument('-m', help="Market Maker Address", required=True)
    sell_parser.add_argument('-a', help="Amount to recover (USDC)", type=float, required=True)
    sell_parser.add_argument('-i', help="Index of outcome choice", type=int, required=True)
    sell_parser.add_argument('-n', help="Maximum number of shares expected (slippage)", type=float, required=True)

    redeem_parser = sub_parser.add_parser('market', help='Redeem Shares')
    redeem_parser.add_argument('-id', help='ID of market to retrieve', required=True)

    sub_parser.add_parser('positions', help='List Open Positions')

    args = parser.parse_args()

    if args.subparser_name in ['buy', 'sell']:
        try:
            market = args.m
            amount = args.a
            index = args.i
            slip_shares = args.n
        except AttributeError as e:
            logger.error(e)
            exit()

    elif args.subparser_name in ['redeem', 'split', 'merge']:
        try:
            condition_id = args.c
            num_outcomes = args.n
            amount = getattr(args, 'a', None)
        except AttributeError as e:
            logger.error(e)
            exit()

    elif args.subparser_name in ['sell_shares']:
        try:
            market_slug = args.s
            outcome = args.o
            num_shares = args.n
            slippage = args.l
        except AttributeError as e:
            logger.error(e)
            exit()

    gas_price = getattr(args, 'g', None)
    w3 = initialize_identity(gas_price)

    trx_hash = None
    if args.subparser_name == 'buy':
        trx_hash = buy(w3, market, amount, index, slip_shares)

    elif args.subparser_name == 'sell':
        trx_hash = sell(w3, market, amount, index, slip_shares)

    elif args.subparser_name == 'redeem':
        trx_hash = redeem(w3, condition_id, num_outcomes)

    elif args.subparser_name == 'split':
        trx_hash = split(w3, condition_id, num_outcomes, amount)

    elif args.subparser_name == 'merge':
        trx_hash = merge(w3, condition_id, num_outcomes, amount)

    elif args.subparser_name == "sell_shares":
        trx_hash = sell_shares(w3, market_slug, outcome, num_shares, slippage)

    elif args.subparser_name == 'positions':
        list_positions(w3, w3.eth.default_account)
        trx_hash = None

    if trx_hash:
        print(Web3.toHex(trx_hash))
