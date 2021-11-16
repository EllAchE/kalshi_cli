# Kalshi CLI tool 

Enables CLI interaction with [Kalshi's](https://kalshi.com/home) trading api.
Supported operations include:
- Retrieve all markets
- Retrieve individual market by ID
- Retrieve user positions
- Place order (with custom expiration, not supported via UI)

![Alt text](./assets/logo.png)

[Kalshi docs](https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html) 
// todo html format README landing page

###Setup
(WIP, repo is functional if you are a power user)

###Usage
    kalshi help - lists usages within CLI
    
######Placing Orders
    kalshi buy -a <amount> -id <marketId> -p <price> -s <side> -e <expiration> -max <maxCost> -sellCap <sellPositionCapped> 
    kalshi sell -a <amount> -id <marketId> -p <price> -s <side> -e <expiration> -max <maxCost> -sellCap <sellPositionCapped> 

There are no "buy" and "sell" orders in kalshi, you can buy shares on one side, or you can buy the opposite 
side to close a position (see the site for more details). The sell command, therefore, attempts to place an order to "close", 
or buy a contract on the opposite side that you offer (all contracts are yes/no binaries)

######Retrieving Markets
    kalshi getMarket -id <id>
    kalshi getMarkets
    

######Retrieving Positions
    kalshi positions

### Notes

This tool is still a WIP. Outstanding items include:
- 

Unfortunately I couldn't see anywhere in the docs that it was

Contributing:
