apikey = ''
apisecret = ''

import requests
import math
from datetime import timedelta
import datetime
import sys
import threading
import linecache
from time import sleep

import ccxt

binance	 = ccxt.binance({'apiKey': apikey,   
			'secret': apisecret,
'enableRateLimit': True,
"options":{"defaultMarket":"futures"},
'urls': {'api': {
                         'public': 'https://dapi.binance.com/dapi/v1',
                         'private': 'https://dapi.binance.com/dapi/v1',},}
})

print(dir(binance))
#sleep(10)
SECONDS_IN_DAY	  = 3600 * 24
from cryptofeed import FeedHandler
from cryptofeed import FeedHandler
from cryptofeed.callback import BookCallback, TickerCallback, TradeCallback
from cryptofeed.defines import TICKER_FUTURES, TICKER_OKS, BID, ASK, FUNDING, L2_BOOK, OPEN_INTEREST, TICKER, TRADES
from cryptofeed.exchanges import OKEx, KrakenFutures, HuobiDM, BinanceFutures, FTX
fh = FeedHandler()
fundingwinners = []
from flask import Flask

from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from flask import jsonify

minArb = 0.015
print(minArb)

minArb = minArb * 75
print(minArb)
minArb = minArb * 365 
print(minArb)
premiumwinners = []
@app.route('/json')
def summary():
    global fundingwinners, premiumwinners
    return jsonify({'premiumwinners': premiumwinners, 'fundingwinners': fundingwinners})

def loop_in_thread():
    fh.run()
def loop_in_thread2():
    app.run(host='0.0.0.0', port=8080)

def PrintException():
	exc_type, exc_obj, tb = sys.exc_info()
	f = tb.tb_frame
	lineno = tb.tb_lineno
	filename = f.f_code.co_filename
	linecache.checkcache(filename)
	line = linecache.getline(filename, lineno, f.f_globals)
	string = 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
	if 'Account does not have enough margin for orde' not in string and 'Reduce leverage to place orders' not in string and 'Size too small' not in string and 'Order already closed' not in string:
		print	(string)
#		if 'Account does not have enough margin for order' not in string:
			#sleep(1)
async def ticker(feed, pair, bid, ask, timestamp, ex):
    global mids
    #print(f'Ex?: {ex} Timestamp: {timestamp} Feed: {feed} Pair: {pair} Bid: {bid} Ask: {ask}')
    if 'OKEX' in feed.upper():
        ex = 'ftx'
        if 'USDT' not in pair:
            name = pair.split('-')[0]
            if '-' not in pair:
                return
            dt = pair[-4:]
            if dt == 'SWAP':
                dt = 'PERP'
            #print(pair)
        else:
            return
    elif 'FTX' in feed:
        ex = 'ftx'
        name = pair.split('-')[0]
        if '-' not in pair:
            return
        dt = pair.split('-')[1]
        #print(dt)
    elif 'KRAKEN' in feed:
        if 'PI' in pair:
            p = pair.split('_')[1]
            name = p.replace('USD','').replace('XBT','BTC')
            dt = 'PERP'
        else:
            name = pair.split('_')[1].split('_')[0].replace('USD', '').replace('XBT', 'BTC')
            dt = pair[-4:]
        ex = 'kraken'
    elif 'BINANCE' in feed:
        #ETH-USD_200925
        name = pair.split('-')[0]
        dt = pair[-4:]
        ex = 'binance'
        #print(dt)


   # print(feed + '-' + name + '-' + dt +': ' + str( 0.5 * ( float(bid) + float(ask))))
    mids[ex][name + '-' + dt] = 0.5 * ( float(bid) + float(ask))

async def book(feed, pair, book, timestamp, receipt_timestamp):
    global mids
    hb = 0
    la = 99999999999999
    for bid in book[BID]:
        if bid > hb:
            hb = bid
    for ask in book[ASK]:
        if ask < la:
            la = ask
    #print(pair)
    dt = pair[-4:]
    name = pair.split('20'+dt)[0]
    #print(name)
  #  if 'BTC' in name and lastex != feed and lastbtc != 0.5 * ( float(bid) + float(ask)):
    #    lastex = feed
   #     lastbtc = 0.5 * ( float(bid) + float(ask))
        #print(feed + '-' + name + '-' + dt +': ' + str( 0.5 * ( float(bid) + float(ask))))
    #print(pair)
    mids['huobi'][name + '-' + dt] = 0.5 * ( float(la) + float(hb))
    #print(mids)
    
    #print(f'Timestamp: {timestamp} Feed: {feed} Pair: {pair} Book Bid Size is {len(book[BID])} Ask Size is {len(book[ASK])}')
def cancelall():
    try:
        binance.dapiPrivateDeleteAllopenorders()
    except Exception as e:
        print(e)
        sleep(10)
        cancelall()
def get_bbo( contract ): # Get best b/o excluding own orders
    try:
        
        ob	  = binance.fetchOrderBook( contract)
        bids	= ob[ 'bids' ]
        asks	= ob[ 'asks' ]
   
        try:
            best_bid	= bids[0][0]
            best_ask	= asks[0][0]
        except:
            PrintException()
        
        return { 'bid': best_bid, 'ask': best_ask }
    except: 
        PrintException()
def doCalc():
    global premiumwinners
    dts = []
    coins = []
    tempmids = mids
    for ex in tempmids:
        for coin in tempmids[ex]:
            #print(coin)
            if coin.split('-')[1] not in dts:
                dts.append(coin.split('-')[1])
            if coin.split('-')[0] not in coins:
                coins.append(coin.split('-')[0])
    arbs = {}
    exes = {}
    #print(expis)
    for coin in coins:
        arbs[coin] = {}
        exes[coin] = {}
        for ex in tempmids:
            for dt in expis:
                arbs[coin][dt] = []
                exes[coin][dt] = {}
    for coin in coins:
        for ex in tempmids:
            for dt in tempmids[ex]:
                try:
                    
                    exes[coin][dt.split('-')[1]][tempmids[ex][dt]] = ex
                except:
                    abc=123
             #       PrintException()
               # print(dt)
                if coin in dt:
                    
                    try:
                        
                        if 'e' not in str(tempmids[ex][dt]):
                        
                            arbs[coin][dt.split('-')[1]].append(tempmids[ex][dt])
                            
                    except:
                        abc=123
    
    
    perps = {}
    lalaexes = {}
    for coin in coins:
        for ex in tempmids:
            for dt in tempmids[ex]:
               # print(dt)
                if coin in dt and 'PERP' in dt:
                    perps[coin] = tempmids[ex][dt]
                    lalaexes[coin] = ex
                    
    for coin in arbs:
        for dt in arbs[coin]:
            try:
                if 'e' not in str(perps[coin]):
                    arbs[coin][dt].append(perps[coin])
                    exes[coin][dt][perps[coin]] = lalaexes[coin]
            except:
                if 'BTC' in coin:
                    PrintException()
    print(exes)
    print(arbs)
    print(expis)
    thearbs = []
    for coin in arbs:
        for dt in expis:
            if dt != 'PERP':
                try:
                    #print(len(arbs[coin][dt]))
                    if len(arbs[coin][dt]) > 0:
                        minimum = min(arbs[coin][dt])
                        
                        maximum = max(arbs[coin][dt])
             #           if coin == 'BTC':
             ##               print(arbs[coin][dt])
              #              print(maximum / minimum)
                        thearb = (((maximum / minimum)-1)*100)*365 #1.1/1.05 = 
                        #print(thearb)
                        #print(expis[dt])
                        #print('thearb of ' + coin + ' at ' + dt + ' in total ' + str(thearb)) 
                        thearb = thearb / expis[dt]
                        #print(thearb)
                        #print( ' ' )
                        if thearb > 3.65 and coin != 'USDT':
                           # print(exes[coin][dt])
                            thearbs.append({'exlong': exes[coin][dt][minimum], 'exshort': exes[coin][dt][maximum], 'coin': coin, 'thearb': thearb, 'dt': dt, 'arbscoindt': arbs[coin][dt]})
                            print({'exlong': exes[coin][dt][minimum], 'exshort': exes[coin][dt][maximum], 'coin': coin, 'thearb': thearb, 'dt': dt, 'arbscoindt': arbs[coin][dt]})
                      #  print('and after figuring out daily arb it\'s ' +  str(thearb))
                    
                except:
                    PrintException()
    # todo remove
    """
    for coin in coins:
        try:
            array = [mids['ftx'][coin + '-PERP'], mids['ftx'][coin + '-0925']]
            minimum = min(array)
                                
            maximum = max(array)
        #           if coin == 'BTC':
        ##               print(arbs[coin][dt])
        #              print(maximum / minimum)
            thearb = (((maximum / minimum)-1)*100)*365 * 10  #1.1/1.05 = 
            #print(thearb)
            #print(expis[dt])
            #print('thearb of ' + coin + ' at ' + dt + ' in total ' + str(thearb)) 
            thearb = thearb / expis['0925']
            #print(thearb)
            #print( ' ' )
            if thearb > 5 and coin != 'USDT':
               # print(exes[coin][dt])
                thearbs.append({'coin': coin, 'thearb': thearb})
                print({'coin': coin, 'thearb': thearb})
          #  print('and after figuring out daily arb it\'s ' +  str(thearb))
        except:
            abc=123#PrintException()
    """
    premiumwinners = []
    for arb in thearbs:
        if arb['coin'] != 'USDT':
           # print(arb)
            premiumwinners.append(arb)
ftx	 = ccxt.ftx({
'enableRateLimit': True,
'rateLimit': 36

})
markets = binance.fetchMarkets()
futs = '200925'
for m in markets:
    #print(m['id'])
    try:
        binance.dapiPrivatePostLeverage({'symbol': m['id'], 'leverage': 75})
    except:
        abc=123
huobi = ccxt.huobipro({"urls": {'api':{'public': 'https://api.hbdm.com/swap-api',
'private': 'https://api.hbdm.com/swap-api'}}})
insts			   = binance.fetchMarkets()
#print(insts[0])

bin_futures_all	=	insts
funding = {}
exchanges = ['binance', 'kraken', 'ftx', 'huobi', 'okex']
mids = {}
for ex in exchanges:
    funding[ex] = {}
    mids[ex] = {}
expis = {}
futureends = ["_CW", "_NW", "_CQ", "_NQ"]
precisions = {}
ticksizes = {}
rates = {}
for ex in exchanges:
    rates[ex] = {}
"""
huobi = requests.get("https://api.hbdm.com/api/v1/contract_contract_info").json()['data']
huobis = []
dts = []
for market in huobi:
    #stri = str(huobi[market])
        #if 'usd' in market['quoteId']:
    if market['symbol'] not in huobis:
        huobis.append(market['symbol'])
    dt = market['delivery_date']
    expiry  = datetime.datetime.strptime( 
                                           dt, 
                                            '%Y%m%d' )
            
    #print(dt)
    dt = dt[-4:]
    if dt not in dts:
        dts.append(dt)			
    now	 = datetime.datetime.utcnow()

    days	= ( expiry - now ).total_seconds() / SECONDS_IN_DAY
    #print(days)
    expis[dt] = days
    #print(expis)

    #print(huobi[market])
\
"""
bcontracts = []

pairs = requests.get('https://dapi.binance.com/dapi/v1/exchangeInfo').json()
for symbol in pairs['symbols']:
    split = len(symbol['baseAsset'])
    #if 'BTC' in symbol['symbol']:
        #print(symbol['symbol'])
    normalized = symbol['symbol'][:split] + '-' + symbol['symbol'][split:]
    bcontracts.append(normalized)
config = {TICKER: bcontracts}
fh.add_feed(BinanceFutures(config=config, callbacks={TICKER: TickerCallback(ticker)}))
"""
ofuts = []
oswaps = []
swaps = requests.get('https://www.okex.com/api/swap/v3/instruments').json()

futures = requests.get('https://www.okex.com/api/futures/v3/instruments').json()
for s in swaps:
    oswaps.append(s['instrument_id'])
for f in futures:
    ofuts.append(f['instrument_id'])
config = {TICKER_OKS: oswaps
,TICKER_FUTURES: ofuts}
fh.add_feed(OKEx(config=config, callbacks={TICKER_FUTURES: TickerCallback(ticker), TICKER_OKS: TickerCallback(ticker)}))

#print(expis)
takens = []
dts.sort()
#print(dts)
times = {"_CW": dts[0], "_NW": dts[1], "_CQ": dts[2], "_NQ": dts[3]}
for fut in bin_futures_all:
    try:
        split = (fut['info']['symbol']).split('_')[1][-4:]
        
        expi = datetime.datetime.fromtimestamp(fut['info']['deliveryDate'] / 1000)

        now	 = datetime.datetime.utcnow()
        days	= ( expi - now ).total_seconds() / SECONDS_IN_DAY
        #print(days)
        #print(days)
        expis[split] = days
        precisions[fut['info']['symbol']] = 1
        ticksizes[fut['info']['symbol']] = 1
        for precision in range(0, fut['info']['pricePrecision']):
            precisions[fut['info']['symbol']] = precisions[fut['info']['symbol']] / 10
            ticksizes[fut['info']['symbol']]= ticksizes[fut['info']['symbol']] / 10
        #print(fut['info']['symbol'])
        #print(ticksizes_binance[fut['info']['symbol']])
        #print(precisions_binance[fut['info']['symbol']])
    except:
        PrintException()

ftx = requests.get("https://ftx.com/api/funding_rates").json()['result']
doneFtx = {}
for rate in ftx:
    doneFtx[rate['future'].replace('-PERP', '')] = False
for rate in ftx:
    if rate['future'].replace('-PERP', '') != 'BTC' and rate['future'].replace('-PERP', '') != 'ETH':
        if doneFtx[rate['future'].replace('-PERP', '')] == False:
            doneFtx[rate['future'].replace('-PERP', '')] = True
            rates['ftx'][rate['future'].replace('-PERP', '')] = rate['rate'] * 24

allfuts = []
expiries = {}
hcontracts = []

for contract in huobis:
    for futureend in futureends:
        hcontracts.append(contract + futureend)

config = {L2_BOOK: hcontracts}
fh.add_feed(HuobiDM(config=config, callbacks={L2_BOOK: BookCallback(book)}))
kcontracts = []
binance = requests.get("https://dapi.binance.com/dapi/v1/premiumIndex").json()
#binance_f = requests.get("https://fapi.binance.com/fapi/v1/premiumIndex").json()
kraken = requests.get("https://futures.kraken.com/derivatives/api/v3/tickers").json()

for market in kraken['tickers']:
    if 'tag' in market:
        kcontracts.append(market['symbol'].upper())
#print(kcontracts)
config = {TICKER: kcontracts}
fh.add_feed(KrakenFutures(config=config, callbacks={TICKER: TickerCallback(ticker)}))

fcontracts = []
ftxmarkets = requests.get("https://ftx.com/api/futures").json()['result']
for market in ftxmarkets:
    if 'MOVE' not in market['name'] and 'HASH' not in market['name']:
        fcontracts.append(market['name'])
config = {TICKER: fcontracts}
fh.add_feed(FTX(config=config, callbacks={TICKER: TickerCallback(ticker)}))
#loop = asyncio.get_event_loop()
"""
t = threading.Thread(target=loop_in_thread, args=())
t.start()
t = threading.Thread(target=loop_in_thread2, args=())
t.start()
print(expis)

import random, string
import requests
import math

funding = {}
exchanges = ['binance']#['binance', 'kraken', 'ftx', 'phemex', 'okex']
for ex in exchanges:
    funding[ex] = {}
def randomword(length):
	   letters = string.ascii_lowercase
	   return ''.join(random.choice(letters) for i in range(length))
def doupdates():
    global fundingwinners
    #todo: replace with dapi.binance.com/, and change all of the ccxt stuff in ccxt/binance.py to dapi.binance.com
    binance2 = requests.get('https://dapi.binance.com/dapi/v1/premiumIndex').json()
    for obj in binance2:
        try:
            funding['binance'][obj['symbol'].replace('USDT', '')] = float(obj['lastFundingRate']) * 3
        except:
            abc=123
    """
    kraken = requests.get('https://futures.kraken.com/derivatives/api/v3/tickers').json()['tickers']
    for obj in kraken:
        if 'tag' in obj:
            if obj['tag'] == 'perpetual':
                funding['kraken'][obj['pair'].replace('XBT','BTC').replace(':USD', '')] = float(obj['fundingRate']) * 3
           
    ftx = requests.get('https://ftx.com/api/funding_rates').json()['result']
    takenftx = []
    for obj in ftx:
        if obj['future'].replace('-PERP','') not in takenftx:
            takenftx.append(obj['future'].replace('-PERP',''))
            funding['ftx'][obj['future'].replace('-PERP','')] = float(obj['rate']) * 24
    
    phemproducts = requests.get('https://api.phemex.com/exchange/public/cfg/v2/products').json()['data']['products']
    phemperps = []
    for obj in phemproducts:
        if obj['type'] == 'Perpetual':
            phemperps.append(obj['symbol'])
    for perp in phemperps:
        phemex = requests.get('https://api.phemex.com/md/ticker/24hr?symbol=' + perp).json()['result']
        funding['phemex'][perp.replace('USD', '')] = float(phemex['fundingRate'])/100000000*3
        
    
    swaps = requests.get('https://www.okex.com/api/swap/v3/instruments').json()
    for s in swaps:
        okex = requests.get('https://www.okex.com/api/swap/v3/instruments/' + s['instrument_id'] + '/funding_time').json()
        funding['okex'][okex['instrument_id'].replace('-USDT-SWAP', '').replace('-USD-SWAP', '')] = float(okex['funding_rate']) * 3
    """
    rates = {}
    for ex in funding:
        rates[ex] = {}
        for coin in funding[ex]:
            rates[ex][coin] = []
    for ex in funding:
        for coin in funding[ex]:
            rates[ex][coin].append(float(funding[ex][coin]))
    APRS = {}
    longshorts = {}
    for ex in rates:
        APRS[ex] = {}
        for coin in rates[ex]:
                
            maximum = max(rates[ex][coin])
            minimum = min(rates[ex][coin])
      #      print(coin)
      #      print(math.fabs(maximum) * 100)
      #      print(math.fabs(minimum) * 100)     
      #      print(str(0.015*3))
      #      print(' ')
            if math.fabs(maximum) > math.fabs(minimum):
                if (math.fabs(maximum) * 365 * 100 * 75 / 2) - minArb > 0:
                    if maximum < 0:
                        longshorts[coin] = 'long'
                    else:
                        longshorts[coin] = 'short'
                    APRS[ex][coin] = (math.fabs(maximum) * 365 * 100 * 75 / 2) - minArb
            else:
                if  (math.fabs(minimum) * 365 * 100 * 75 / 2) - minArb > 0:
                    if minimum < 0:
                        longshorts[coin] = 'long'
                    else:
                        longshorts[coin] = 'short'
                    APRS[ex][coin] = (math.fabs(minimum) * 365 * 100 * 75 / 2) - minArb

    
    fundingwinners = []
    t = 0
    c = 0
    for ex in APRS:
        maximum = 0

        winner = ""
        for coin in APRS[ex]:
            if APRS[ex][coin] > 0 and 'LINK' in coin or 'BTC' in coin or 'ETH' in coin or 'ADA' in coin:
                t = t + APRS[ex][coin]
                c = c + 1
                
                fundingwinners.append({'ex': ex, 'coin': coin, 'arb': APRS[ex][coin]})
     #           print({'ex': ex, 'coin': coin, 'arb': APRS[ex][coin]})
       #print('The Maximum funding opportunity on ' + ex + ' now is ' + winner + ' with ' + str(maximum) + '%!')
    percs = {}
    tobuy = {}
    for ex in APRS:
        maximum = 0

        winner = ""
        for coin in APRS[ex]:
            if APRS[ex][coin] > 0 and 'LINK' in coin or 'BTC' in coin or 'ETH' in coin or 'ADA' in coin:
                    percs[coin] = APRS[ex][coin] / t
                                   #((1000000 * 0.66) * 75 /2) / 10
                    tobuy[coin] = ((balance * percs[coin]) * 75 / 2) / 10
                    if 'BTC' in coin:
                        tobuy[coin] = tobuy[coin] / 10 
                    tobuy[coin.replace('PERP', futs)] = tobuy[coin] * -1
    #print(percs)        
    for coin in longshorts:
        if longshorts[coin] == 'short':
            try:
                tobuy[coin] = tobuy[coin] * -1
                tobuy[coin.replace('PERP', futs)] = tobuy[coin.replace('PERP', futs)] * -1
            except:
                abc=123
    cancelall()
    for coin in tobuy:
        #-100 btc
        #-800 
        #100
        #800
        try:
            if math.fabs(tobuy[coin] / (balance * 75)) > 0.05: 
                tobuy[coin] = tobuy[coin] - pos[coin] / 10
                if 'BTC' in coin:
                    tobuy[coin] = tobuy[coin] / 10
                #print(tobuy)
                direction = 'BUY'
                if tobuy[coin] < 0:
                    direction = 'SELL'
                    tobuy[coin] = tobuy[coin] * -1
                if tobuy[coin] != 0:
                    #print(tobuy[coin])
                    bbo = get_bbo(coin)
                    if direction == 'SELL':
                        
                        binance.dapiPrivatePostOrder(  {'symbol': coin, 'side': direction, 'type': 'LIMIT', 'price': bbo['best_bid'], 'quantity': int(tobuy[coin] / 100),"newClientOrderId": "x-v0tiKJjj-" + randomword(15)})
                    else:
                        binance.dapiPrivatePostOrder(  {'symbol': coin, 'side': direction, 'type': 'LIMIT', 'price': bbo['best_ask'], 'quantity': int(tobuy[coin] / 100),"newClientOrderId": "x-v0tiKJjj-" + randomword(15)})
        except:
            PrintException()
    print(tobuy)
balance = 0
pos = {}
def updatePositions():
    global positions
    positions	   = binance.dapiPrivateGetPositionRisk()
    for p in positions:
        pos[p['symbol']] = float(p['positionAmt']) * 10
        if 'BTC' in p['symbol']:
            pos[p['symbol']] = pos[p['symbol']] * 10
    print(pos)
def updateBalance():
    global balance
    bal2 = binance.fetchBalance()
    newbal = 0
    #print(bal2)
    ##print(bal2)
    ##print(bal2)
    for coin in bal2['info']['assets']:
        #print(coin)
        newbal = newbal + float(coin['marginBalance'])

        im = float(coin['initialMargin'])
        if newbal != 0:
            im = im / newbal
    balance = newbal
    print(balance)
while True:
    updatePositions()
    updateBalance()
    for ex in mids:
        for dt in mids[ex]:
            if dt.split('-')[1] not in expis:
                try:
                
                    if 'PERP' in dt:
                        expis[dt.split('-')[1]] = 30000
                    else:
                        now	 = datetime.datetime.utcnow()
                        expiry  = datetime.datetime.strptime( 
                                                   '2021' + dt.split('-')[1], 
                                                    '%Y%m%d' )
                        days	= ( expiry - now ).total_seconds() / SECONDS_IN_DAY
                        print(days)
                        print(dt.split('-')[1])
                        expis[dt.split('-')[1]] = days
                except:
                    abc=123
    #doCalc()
    doupdates()
    sleep(60)