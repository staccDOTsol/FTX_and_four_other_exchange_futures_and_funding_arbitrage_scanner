apikey = ''
apisecret = ''
divisor=100

import requests
import math
from datetime import timedelta
import datetime
import sys
import threading
import linecache
from time import sleep
expis = {}
import ccxt
fundingwinners = []
from flask import jsonify
import asyncio
import requests



minArb = 0.015
print(minArb)

minArb = minArb * 75
print(minArb)
minArb = minArb * 365 
print(minArb)
premiumwinners = []
import json
def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    string = 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
    if 'Account does not have enough margin for orde' not in string and 'Reduce leverage to place orders' not in string and 'Size too small' not in string and 'Order already closed' not in string:
        print   (string)
#       if 'Account does not have enough margin for order' not in string:
            #sleep(1)

ftx  = ccxt.ftx({
'enableRateLimit': True,
'rateLimit': 36

})

markets = requests.get("https://ftx.com/api/markets").json()['result']
expfuts = requests.get("https://ftx.com/api/expired_futures").json()['result']
futs = '200925'
ohlcvs = {}
ohlcvs2 = {}
import datetime
import random
import dateutil.parser
import time
futures = []
yearago = dateutil.parser.parse("2020-08-08T08:00:00")
for m in expfuts:
    nogo = True
    for m2 in markets:
        if m2['name'] == m['name']:
            nogo = False
    if nogo == True:
        if dateutil.parser.parse(m['expiry'][:-7]) > yearago:
            futures.append(m)
futuresOpps = {}
futuresOpps['ftx'] = {}
todo = ["BTC", "ETH", "BNB", "ADA", "XRP", "DOT","UNI","SOL"]
import threading
mdones = []
toms = []
for m in markets:
    if True:# m['name'] == 'BTC-PERP':
        #print(m)
        if m['type'] == 'future':
            m['id'] = m['name']
            
            if m['id'].split('-')[0] in todo and 'MOVE' not in m['id']:
                mdones.append(m['id'])
                toms.append(m['id'])

for m2 in futures:

                        if 'expiry' in m2 and 'MOVE' not in m2['name'] and 'HASH' not in m2['name']:
                            if dateutil.parser.parse(m2['expiry'][:-7]) > yearago:
                                m2['id'] = m2['name']
                                if m2['id'] not in mdones and m2['id'].split('-')[0] in todo and 'MOVE' not in m2['id']:
                                    mdones.append(m2['id'])
                                    toms.append(m2['id'])

async def doStuff(urls):
                                
                global ohlcvs, toms
                dodo = True
                mosts = {}
                leasts = {}
                tss = {}

                if urls == None:
                    urls = []
                    
                    for m in toms:
                        try:
                            with open(m + '-trades.json', 'r') as f:
                                ohlcvs[m] = json.loads(f.read())
                                leasts[m] = dateutil.parser.parse(ohlcvs[m][-200]['time'][:-13])
                                dodo = False

                                mosts[m] = dateutil.parser.parse(ohlcvs[m][-1]['time'][:-13])
                                tss[m] = time.mktime(leasts[m].timetuple())
                            ohlcvs[m] = []
                        except Exception as e:
                            print(e)
                            ohlcvs[m] = []
                        urls.append("https://ftx.com/api/markets/" + m + "/trades")
                ran = random.randint(0, 100)
                print(ran)
                if ran < 5:
                    tohlcvs = {}
                    for m in toms:

                        with open(m + '-trades.json', 'r') as f:
                            tohlcvs[m] = (json.loads(f.read()))
                        for ohlcv in tohlcvs[m]:
                            ohlcvs[m].append(ohlcv)
                        with open(m + '-trades.json', 'w') as f:
                            f.write(json.dumps(ohlcvs[m]))
                        tohlcvs[m] = []
                        ohlcvs[m] = []
                loop = asyncio.get_event_loop()
                futuresloop = []
                for u in urls:
                        futuresloop.append(
                                            loop.run_in_executor(
                                                None, 
                                                requests.get, 
                                                u
                                            )
                                        )
                urls = []
                for response in await asyncio.gather(*futuresloop):
                    ftx = response.json()['result']
                    #print(ftx)
                    #print(response.url)  
                    astring = response.url.split('/trades')[0].split('markets/')[1]
                    #print(astring)
                    m = {}
                    m['id'] = astring
                    #sleep(100)          
                    #sleep(100)
                    #ohlcvs = {}
                    if len(ftx) > 0:
                        try:
                            futs = []
                            #print(dodo)
                            if dodo == True:
                                try:
                                    least = dateutil.parser.parse(ftx[0]['time'][:-13])
                                    #print(ftx[0]['time'][:-13])
                                    most = dateutil.parser.parse(ftx[-1]['time'][:-13]) - timedelta(hours=4)
                                except:
                                    least = dateutil.parser.parse(ftx[0]['time'][:-7])
                                    #print(ftx[0]['time'][:-7])
                                    most = dateutil.parser.parse(ftx[-1]['time'][:-7]) - timedelta(hours=4)
                            else:
                                least = leasts[m['id']]
                                most = mosts[m['id']]
                            if m['id'] == 'BTC-PERP':
                                print(ftx[-1]['time'])
                            ts = time.mktime(least.timetuple())
                            ts2 = time.mktime(most.timetuple())
                            if least > yearago:
                        
                                """
                                for m2 in futures:
                                    if 'expiry' in m2 and 'MOVE' not in m2['name'] and 'HASH' not in m2['name'] and m['id'].replace('-PERP','') == m2['underlying']:
                                        if dateutil.parser.parse(m2['expiry']) < most:
                                            m2['id'] = m2['name']
                                            print(m2['id'])
                                            fut = requests.get("https://ftx.com/api/markets/" + m2['id'] + "/candles?resolution=3600").json()['result']
                                            for candle in fut:
                                                if candle['time'][:-13] not in ohlcvs:
                                                    ohlcvs[candle['time'][:-13]] = {}
                                                    ohlcvs2[candle['time'][:-13]] = {}
                                                ohlcvs[candle['time'][:-13]][m2['id']] = candle['close']
                                                ohlcvs2 [candle['time'][:-13]][m2['id']] =  ((dateutil.parser.parse(m2['expiry']) - dateutil.parser.parse(candle['time'][:-13])).total_seconds() / 60 / 60 / 24 / 365)
                                
                                for m2 in markets:
                                    if 'expiry' in m2 and 'MOVE' not in m2['name'] and m['id'].replace('-PERP','') in m2['underlying']:
                                        if dateutil.parser.parse(m2['expiry']) < most:
                                            m2['id'] = m2['name']
                                            print(m2['id'])
                                            fut = requests.get("https://ftx.com/api/markets/" + m2['id'] + "/candles?resolution=3600").json()['result']
                                            for candle in fut:
                                                if candle['time'][:-13] not in ohlcvs:
                                                    ohlcvs[candle['time'][:-13]] = {}
                                                    ohlcvs2[candle['time'][:-13]] = {}
                                                print((dateutil.parser.parse(m2['expiry']) - dateutil.parser.parse(candle['time'][:-13]).total_seconds() / 60 / 60 / 24 / 365))
                                                ohlcvs[candle['time'][:-13]][m2['id']] = candle['close']
                                                ohlcvs2 [candle['time'][:-13]][m2['id']] =  ((dateutil.parser.parse(m2['expiry']) - dateutil.parser.parse(candle['time'][:-13])).total_seconds() / 60 / 60 / 24 / 365)
                                """
                                for candle in ftx:
                                    if m['id'] not in ohlcvs:
                                        ohlcvs[m['id']] = []
                                        ohlcvs2[candle['time'][:-13]] = {}
                                    if candle not in ohlcvs[m['id']]:
                                        ohlcvs[m['id']].append(candle)
                                    #ohlcvs2 [candle['time'][:-13]][m['id']] =  3000
                                    try:
                                        d = dateutil.parser.parse(candle['time'][:-13])
                                    except:
                                        d = dateutil.parser.parse(candle['time'][:-7])
                                    least = d
                                    ts = time.mktime(d.timetuple())
                                
                                #print(len(ohlcvs[m['id']]))
                                #print(str(ts))
                                #print("https://ftx.com/api/markets/" + m['id'] + "/trades?end_time=" + str(int(ts2))
                                 #   )
                                done = False 
                                while done == False:
                                    try: 
                                        u = "https://ftx.com/api/markets/" + m['id'] + "/trades?limit=5000&end_time=" + str(int(ts2))
                                        if m['id'] == 'BTC-PERP':
                                            print(u)
                                        urls.append(u)
    #                                    ftx = requests.get("https://ftx.com/api/markets/" + m['id'] + "/trades?limit=5000&end_time=" + str(int(ts2))).json()['result']
                                        done = True
                                        sleep(0.01)
                                    except:
                                        sleep(10)

                                #sleep(100)
                                if len(ftx) < 10:
                                    least = yearago
                                
                        
                        except Exception as e:
                            print(e)
                            with open('errors.log', 'r') as f:
                                errs = f.read()
                            errs = errs + e + '\n'
                            with open('errors.log', 'a') as f:
                                f.write(errs)
                    #else:
                        #print(response.text)
                await doStuff(urls)  
while True:         
    try:
        loop = asyncio.get_event_loop()
    except:
        abc=123
    try:
        loop.run_until_complete(doStuff(None))
    except:
        abc=123    
"""
                
                for st in ohlcvs:
                        
                        perp = 0
                        expi = 0
                        coin = ""
                        for inst in ohlcvs[st]:
                            #print(inst)
                            if 'PERP' in inst:
                                #print(inst)
                                perp = float(ohlcvs[st][inst])
                                coin = inst.replace('-PERP', '')
                                #print(perp)
                                diffs = []
                                diffas = {}
                                for inst2 in ohlcvs[st]:
                                    if 'PERP' not in inst2 and coin in inst2:
                                        #print(inst)
                                    #    print(ohlcvs[st][inst])
                                        expi = float(ohlcvs2[st][inst2])
                                        if expi > 0:
                                            diffs.append(abs(perp - float(ohlcvs[st][inst2])) / expi)

                                            diffas[abs((perp - float(ohlcvs[st][inst2])) / expi)] = inst2
                                #print(diffs)
                                #print(len(diffs))

                                if len(diffs) > 0 and expi > 0:
                                    
                                    if st not in futuresOpps['ftx']:
                                        futuresOpps['ftx'][st] = {}
                                    maxdiff = max(diffs)
                                    try: 
                                        winner = diffas[maxdiff]  
                                        thediff = perp / ohlcvs[st][winner] # 8000 futures 6000 perps, short futures and long perp
                                        thediff = thediff - 1
                                        thediff = thediff * 100
                                        thediff = thediff / expi
                                        
                                        futuresOpps['ftx'][st][coin] = thediff
                                    except Exception as e:
                                        print(e)
                with open('futures_rates.json', 'w') as f:
                    f.write(json.dumps(futuresOpps))            
                ohlcvs2 = {}
                ohlcvs = {}
                
                ftx = requests.get("https://ftx.com/api/markets/" + m['id'] + "/trades").json()['result']

                least = dateutil.parser.parse(ftx[0]['startTime'])
                most = dateutil.parser.parse(ftx[-1]['startTime'])
                ts = time.mktime(least.timetuple())

                while least > yearago:
                    futs = []
                    least = dateutil.parser.parse(ftx[0]['startTime'])
                    most = dateutil.parser.parse(ftx[-1]['startTime'])
                    ts = time.mktime(least.timetuple())
                    
                    for m2 in futures:
                        if 'expiry' in m2 and 'MOVE' not in m2['name'] and 'HASH' not in m2['name'] and m['id'].replace('-PERP','') == m2['underlying']:
                            if dateutil.parser.parse(m2['expiry']) < most:
                                m2['id'] = m2['name']
                                print(m2['id'])
                                fut = requests.get("https://ftx.com/api/markets/" + m2['id'] + "/candles?resolution=3600").json()['result']
                                for candle in fut:
                                    if candle['startTime'] not in ohlcvs:
                                        ohlcvs[candle['startTime']] = {}
                                        ohlcvs2[candle['startTime']] = {}
                                    ohlcvs[candle['startTime']][m2['id']] = candle['close']
                                    ohlcvs2 [candle['startTime']][m2['id']] =  ((dateutil.parser.parse(m2['expiry']) - dateutil.parser.parse(candle['startTime'])).total_seconds() / 60 / 60 / 24 / 365)
                    
                    for m2 in markets:
                        if 'expiry' in m2 and 'MOVE' not in m2['name'] and m['id'].replace('-PERP','') in m2['underlying']:
                            if dateutil.parser.parse(m2['expiry']) < most:
                                m2['id'] = m2['name']
                                print(m2['id'])
                                fut = requests.get("https://ftx.com/api/markets/" + m2['id'] + "/candles?resolution=3600").json()['result']
                                for candle in fut:
                                    if candle['startTime'] not in ohlcvs:
                                        ohlcvs[candle['startTime']] = {}
                                        ohlcvs2[candle['startTime']] = {}
                                    print((dateutil.parser.parse(m2['expiry']) - dateutil.parser.parse(candle['startTime']).total_seconds() / 60 / 60 / 24 / 365))
                                    ohlcvs[candle['startTime']][m2['id']] = candle['close']
                                    ohlcvs2 [candle['startTime']][m2['id']] =  ((dateutil.parser.parse(m2['expiry']) - dateutil.parser.parse(candle['startTime'])).total_seconds() / 60 / 60 / 24 / 365)
                    
                    for candle in ftx:
                        if candle['startTime'] not in ohlcvs:
                            ohlcvs[candle['startTime']] = {}
                            ohlcvs2[candle['startTime']] = {}
                        ohlcvs[candle['startTime']][m['id']] = candle['close']
                        ohlcvs2 [candle['startTime']][m['id']] =  3000
                        d = dateutil.parser.parse(candle['startTime'])
                        if d < least:
                            least = d
                            ts = time.mktime(d.timetuple())
                    
                    ftx = requests.get("https://ftx.com/api/markets/" + m['id'] + "/candles?resolution=3600&end_time=" + str(int(ts))).json()['result']
                    if len(ftx) < 10:
                        least = yearago
                #print(len(ohlcvs))
                for st in ohlcvs:
                        
                        perp = 0
                        expi = 0
                        coin = ""
                        for inst in ohlcvs[st]:
                            #print(inst)
                            if 'PERP' in inst:
                                #print(inst)
                                perp = float(ohlcvs[st][inst])
                                coin = inst.replace('-PERP', '')
                                #print(perp)
                                diffs = []
                                diffas = {}
                                for inst2 in ohlcvs[st]:
                                    if 'PERP' not in inst2 and coin in inst2:
                                        #print(inst)
                                    #    print(ohlcvs[st][inst])
                                        expi = float(ohlcvs2[st][inst2])
                                        if expi > 0:
                                            diffs.append(abs(perp - float(ohlcvs[st][inst2])) / expi)

                                            diffas[abs((perp - float(ohlcvs[st][inst2])) / expi)] = inst2
                                #print(diffs)
                                #print(len(diffs))

                                if len(diffs) > 0 and expi > 0:
                                    
                                    if st not in futuresOpps['ftx']:
                                        futuresOpps['ftx'][st] = {}
                                    maxdiff = max(diffs)
                                    try: 
                                        winner = diffas[maxdiff]  
                                        thediff = perp / ohlcvs[st][winner] # 8000 futures 6000 perps, short futures and long perp
                                        thediff = thediff - 1
                                        thediff = thediff * 100
                                        thediff = thediff / expi
                                        
                                        futuresOpps['ftx'][st][coin] = thediff
                                    except Exception as e:
                                        print(e)
                with open('futures_rates.json', 'w') as f:
                    f.write(json.dumps(futuresOpps))            
                ohlcvs2 = {}
                ohlcvs = {}
            else:
            
                print(m['id'])
"""
from time import sleep
sleep(1000)
"""



huobi = ccxt.huobipro({"urls": {'api':{'public': 'https://api.hbdm.com/swap-api',
'private': 'https://api.hbdm.com/swap-api'}}})
insts              = binance.fetchMarkets()
#print(insts[0])

bin_futures_all =   insts
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
    now  = datetime.datetime.utcnow()

    days    = ( expiry - now ).total_seconds() / SECONDS_IN_DAY
    #print(days)
    expis[dt] = days
    #print(expis)

    #print(huobi[market])
\

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

        now  = datetime.datetime.utcnow()
        days    = ( expi - now ).total_seconds() / SECONDS_IN_DAY
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
print(expis)
import json

import random, string
import requests
import math
from datetime import timedelta
  
  
# Calculating future dates
# for two years
import time
funding = {}
exchanges = ['ftx']#['binance', 'kraken', 'ftx', 'phemex', 'okex']
for ex in exchanges:
    funding[ex] = {}
def randomword(length):
       letters = string.ascii_lowercase
       return ''.join(random.choice(letters) for i in range(length))
def doupdates():
    global fundingwinners
    #todo: replace with dapi.binance.com/, and change all of the ccxt stuff in ccxt/binance.py to dapi.binance.com
    """
    binance2 = requests.get('https://dapi.binance.com/dapi/v1/premiumIndex').json()
    for obj in binance2:
        try:
            funding['binance'][obj['symbol'].replace('USDT', '')] = float(obj['lastFundingRate']) * 3
        except:
            abc=123
    
    kraken = requests.get('https://futures.kraken.com/derivatives/api/v3/tickers').json()['tickers']
    for obj in kraken:
        if 'tag' in obj:
            if obj['tag'] == 'perpetual':
                funding['kraken'][obj['pair'].replace('XBT','BTC').replace(':USD', '')] = float(obj['fundingRate']) * 3
    """   
    ftx = requests.get('https://ftx.com/api/funding_rates').json()['result']
    takenftx = []
    least = 0
    ts = 0
    most = 0
    for obj in ftx:
            if 'ftx' not in funding:
                funding['ftx'] = {}
            if  obj['time'][:-13] not in funding['ftx']:
                funding['ftx'][obj['time'][:-13]] = {}
            funding['ftx'][obj['time'][:-13]][obj['future'].replace('-PERP','')] = float(obj['rate']) * 24 * 365 * 100

            d = dateutil.parser.parse(obj['time'][:-13])
            if least == 0:
                least = d
                most = d
                ts = time.mktime(d.timetuple()) - 14400
                print(ts)
            if most < d:
                most = d
            if least > d:
                least = d
                ts = time.mktime(d.timetuple()) - 14400
                print(ts)
    start_time = most - least
    start_time = start_time.total_seconds() * 1000
    start_time = int(ts) - start_time
    ftx = requests.get('https://ftx.com/api/funding_rates?start_time=' + str(int(start_time)) + '&end_time=' + str(int(ts))).json()['result']
    done = False
    while done == False:
        
        for obj in ftx:
            if 'ftx' not in funding:
                funding['ftx'] = {}
            if  obj['time'][:-13] not in funding['ftx']:
                funding['ftx'][obj['time'][:-13]] = {}
            funding['ftx'][obj['time'][:-13]][obj['future'].replace('-PERP','')] = float(obj['rate']) * 24 * 365 * 100

            d = dateutil.parser.parse(obj['time'][:-13])
            if least == 0:
                least = d
                most = d
                ts = time.mktime(d.timetuple()) - 14400
          #      print(ts)
            if most < d:
                most = d
            if least > d:
                least = d
                ts = time.mktime(d.timetuple()) - 14400
         #       print(ts)
                #print(ts)
        #print(ts)
        start_time = most - least
        start_time = start_time.total_seconds() * 1000
        #print(start_time)
        start_time = int(ts) - start_time
        #print(start_time)
        #print(ts)
        date = datetime.datetime.fromtimestamp(ts)
        print(date)
        #print('https://ftx.com/api/funding_rates?start_time=' + str(int(start_time)) + '&end_time=' + str(int(ts)))
        #   sleep(100)
        if least < yearago:
            done = True
        ftx = requests.get('https://ftx.com/api/funding_rates?start_time=' + str(int(start_time)) + '&end_time=' + str(int(ts))).json()['result']
        #print(len(ftx))
        most = 0
        least = 0
    with open('funding_rates.json', 'w') as f:
        f.write(json.dumps(funding))
    sleep(100000)
    """
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
                    percs[coin] = 1#APRS[ex][coin] / t
                                   #((1000000 * 0.66) * 75 /2) / 10
                    #((25 * 0.25 ) * 75 / 2) / 10
                    
                    tobuy[coin] = ((balances[coin.split('_')[0].replace('USD', '')] * percs[coin]) * 75 / 2) / 10
                    tobuy[coin.replace('PERP', futs)] = tobuy[coin] * -1
                    
            elif 'LINK' in coin or 'BTC' in coin or 'ETH' in coin or 'ADA' in coin:
                tobuy[coin] = 0
                tobuy[coin.replace('PERP', futs)] = 0
    print(percs)        
    for coin in longshorts:
        if longshorts[coin] == 'short':
            try:
                tobuy[coin] = tobuy[coin] * -1
                tobuy[coin.replace('PERP', futs)] = tobuy[coin.replace('PERP', futs)] * -1
            except:
                abc=123
    print(tobuy)
    #sleep(100)
    for coin in tobuy:
        cancelall(coin)
        #-100 btc
        #-800 
        #100
        #800
        try:
            
        
            if math.fabs((tobuy[coin]) / (balances[coin.split('_')[0].replace('USD', '')] * 75)) > ((1/divisor) * 0.5) / 75: 
                        
                if 'BTC' in coin:
                    tobuy[coin] = tobuy[coin] / 10
                    tobuy[coin] = tobuy[coin] - pos[coin] / 10
                else:
                    tobuy[coin] = tobuy[coin] - pos[coin] / 100
                #print(tobuy)
                direction = 'BUY'
                if tobuy[coin] < 0:
                    direction = 'SELL'
                    tobuy[coin] = tobuy[coin] * -1
                if tobuy[coin] != 0:
                    #print(tobuy[coin])
                    bbo = mids['binance'][coin.replace('USD', '-USD')]
                    
                    print(int(tobuy[coin] / divisor))
                    print(tobuy[coin])
                    if direction == 'SELL':
                        
                        binance.dapiPrivatePostOrder(  {'timeInForce': 'GTC', 'symbol': coin, 'side': direction, 'type': 'LIMIT', 'price': bbo['bid'], 'quantity': int(tobuy[coin] / divisor),"newClientOrderId": "x-v0tiKJjj-" + randomword(15)})
                    else:
                        binance.dapiPrivatePostOrder(  {'timeInForce': 'GTC', 'symbol': coin, 'side': direction, 'type': 'LIMIT', 'price': bbo['ask'], 'quantity': int(tobuy[coin] / divisor),"newClientOrderId": "x-v0tiKJjj-" + randomword(15)})
        except:
            PrintException()
    print(tobuy)
balances = {}
totrade = ['BTC', 'ETH', 'LINK', 'ADA']
pos = {}
doupdates()
for t in totrade:
    balances[t] = 0
def updatePositions():
    global positions
    positions      = binance.dapiPrivateGetPositionRisk()
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
    btc_perp = (mids['binance']['BTC-USD_PERP']['ask'] + mids['binance']['BTC-USD_PERP']['bid']) / 2
    ada_perp = (mids['binance']['ADA-USD_PERP']['ask'] + mids['binance']['ADA-USD_PERP']['bid']) / 2
    eth_perp = (mids['binance']['ETH-USD_PERP']['ask'] + mids['binance']['ETH-USD_PERP']['bid']) / 2
    link_perp = (mids['binance']['LINK-USD_PERP']['ask'] + mids['binance']['LINK-USD_PERP']['bid']) / 2
    
    ##print(bal2)
    for coin in bal2['info']['assets']:
        if coin['asset'] == 'BTC':
            balances['BTC'] = float(coin['marginBalance']) * btc_perp
        if coin['asset'] == 'ADA':
            balances['ADA'] = float(coin['marginBalance']) * ada_perp
        if coin['asset'] == 'ETH':
            balances['ETH'] = float(coin['marginBalance']) * eth_perp
        if coin['asset'] == 'LINK':
            balances['LINK'] = float(coin['marginBalance']) * link_perp

        im = float(coin['initialMargin'])
        if newbal != 0:
            im = im / newbal
    #balance = newbal
    #print(balance)
#while True:
#updatePositions()
for ex in mids:
    for dt in mids[ex]:
        if dt.split('-')[1] not in expis:
            try:
            
                if 'PERP' in dt:
                    expis[dt.split('-')[1]] = 30000
                else:
                    now  = datetime.datetime.utcnow()
                    expiry  = datetime.datetime.strptime( 
                                               '2021' + dt.split('-')[1], 
                                                '%Y%m%d' )
                    days    = ( expiry - now ).total_seconds() / SECONDS_IN_DAY
                    print(days)
                    print(dt.split('-')[1])
                    expis[dt.split('-')[1]] = days
            except:
                abc=123
#doCalc()
#sleep(20)
#updateBalance()
#sleep(5)
doupdates()
sleep(35)
