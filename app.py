import requests
import math

funding = {}
exchanges = ['binance', 'kraken', 'ftx', 'phemex', 'okex']
for ex in exchanges:
    funding[ex] = {}
def doupdates():
    binance = requests.get('https://fapi.binance.com/fapi/v1/premiumIndex').json()
    for obj in binance:
        
        funding['binance'][obj['symbol'].replace('USDT', '')] = float(obj['lastFundingRate']) * 3
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
    rates = {}
    for ex in funding:
        rates[ex] = {}
        for coin in funding[ex]:
            rates[ex][coin] = []
    for ex in funding:
        for coin in funding[ex]:
            rates[ex][coin].append(float(funding[ex][coin]))
    APRS = {}
    for ex in rates:
        APRS[ex] = {}
        for coin in rates[ex]:
                
            maximum = max(rates[ex][coin])
            minimum = min(rates[ex][coin])
            if math.fabs(maximum) > math.fabs(minimum):
                APRS[ex][coin] = math.fabs(maximum) * 365 * 100
            else:
                APRS[ex][coin] = math.fabs(minimum) * 365 * 100
    print(APRS)
    for ex in APRS:
        maximum = 0

        winner = ""
        for coin in APRS[ex]:
            if APRS[ex][coin] > maximum:
                maximum = APRS[ex][coin] 
                winner = coin
        print('The Maximum funding opportunity on ' + ex + ' now is ' + winner + ' with ' + str(maximum) + '%!')
    
doupdates()