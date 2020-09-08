# FTX_and_four_other_exchange_futures_and_funding_arbitrage_scanner


app.py is futures nonsense, without leverage


app2.py is futures and funding nonsense, at 10x leverage hedge and 10x perp/fut. currently configured for FTX only and a bit buggier with +4 exchanges.


Run python app2.py after pip install whatever we need cryptofeed? requests? ccxt? dunno? 


#todo: replace with dapi.binance.com/, and change all of the ccxt stuff in ccxt/binance.py to dapi.binance.com


Note that app2 now acts on funding opportunities in binance testnet as of this most recent commit.s


Check localhost:8080/json for some output