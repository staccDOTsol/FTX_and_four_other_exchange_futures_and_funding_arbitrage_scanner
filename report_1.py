import json
import datetime
import dateutil.parser
import time
todo = ["BTC", "ETH", "BNB", "ADA", "XRP", "DOT","UNI","SOL"]

with open('futures_rates.json', 'r') as f:
	futures_rates = json.loads(f.read())['ftx']

with open('funding_rates.json', 'r') as f:
	funding_rates = json.loads(f.read())['ftx']
net_rates = {}
net_rates['futures'] = {}
net_rates['funding'] = {}
net_rates['net'] = {}
equity = 100000
direction = {}
winner = {}
maxts = 0
mints = 99999999999999999999
for st in futures_rates:
	d = dateutil.parser.parse(st)
	ts = time.mktime(d.timetuple())
	if maxts < ts:
		maxts = ts
	if mints > ts:
		mints = ts
	net_rates['net'][ts] = {}
	net_rates['futures'][ts] = futures_rates[st]
diff = maxts - mints
diff = diff / 365 / 24 
daysinsim = diff

since = datetime.datetime.utcnow() - datetime.timedelta(days=20)
daysinsim = (datetime.datetime.utcnow() - since).total_seconds() / 60 / 60 / 24
print(daysinsim)
#sleep(100)
for st in funding_rates:

	d = dateutil.parser.parse(st)
	if d > since:
		#print(d)
		ts = time.mktime(d.timetuple())
		
		net_rates['funding'][ts] = funding_rates[st]

		coins = []
		topp = 0
		for coin in funding_rates[st]:
			#if coin in todo:
			coins.append(coin)
		#print(coins)
		if ts in net_rates['futures']:
			if ts not in direction:
				direction[ts] = {}
				winner[ts] = {}
			for coin in net_rates['futures'][ts]:
				if coin in coins:
					if coin not in net_rates['net'][ts]:
						net_rates['net'][ts][coin] = 0
					#11000 / 10000, positive means short perps
					#funding negative means long perps
					#funding positive means short perps

					#negative means long perps


					#if abs(net_rates['futures'][ts][coin]) > abs(net_rates['funding'][ts][coin]):
					winner[ts][coin] = 'futures'
					if (net_rates['futures'][ts][coin] < 0 and net_rates['funding'][ts][coin] < 0) or (net_rates['futures'][ts][coin] > 0 and net_rates['funding'][ts][coin] > 0):

						net_rates['net'][ts][coin] = abs(net_rates['futures'][ts][coin] / 365 / 24) + abs(net_rates['funding'][ts][coin] / 365 / 24)
						topp = topp + abs(net_rates['futures'][ts][coin] / 365 / 24) + abs(net_rates['funding'][ts][coin] / 365 / 24)
					
					else: #fut -40 fund 20, =20
					#fut -20 fund 40, =-20
					#fut 40 fund -20, =20
					#fut 20 fund -40, =-20
						topp = topp + abs(net_rates['futures'][ts][coin] / 365 / 24) - abs(net_rates['funding'][ts][coin] / 365 / 24)
						net_rates['net'][ts][coin] =  abs(net_rates['futures'][ts][coin] / 365 / 24) - abs(net_rates['funding'][ts][coin] / 365 / 24)	

						
					"""
					if net_rates['futures'][ts][coin] < 0:
						direction[ts][coin] = 'short perp, long futs'
					else:
						direction[ts][coin] = 'long perp, short futs'
					
					else:
						winner[ts][coin] = 'funding'
						net_rates['net'][ts][coin] = abs(net_rates['funding'][ts][coin]) + abs(net_rates['futures'][ts][coin])
						if net_rates['funding'][ts][coin] > 0:
							direction[ts][coin] = 'short perp, long futs'
						else:
							direction[ts][coin] = 'long perp, short futs'
					"""
			opps = {}
			wanted = {}
			for coin in net_rates['net'][ts]:
				#if coin in todo:
				opps[coin] = (net_rates['net'][ts][coin] / topp) / 2 * 6
				
			#for coin in opps:
		#		shouldbeone = shouldbeone + opps[coin]

			#print(opps)
			#print(shouldbeone)
			#sleep(100)
coinAvgs = {}
winners = {}
directions = {}
winners['funding'] = 0
winners['futures'] = 0
directions['long perp, short futs'] = 0

directions['short perp, long futs'] = 0
coinvalues = {}
for ts in net_rates['net']:
	for coin in net_rates['net'][ts]:
		if coin not in coinvalues:# and coin in todo:
			coinvalues[coin] = 0
		coinvalues[coin] = coinvalues[coin] + net_rates['net'][ts][coin]
print(coinvalues)
		
"""
		if coin not in winners:
			winners[coin] = {}
		if coin not in coinAvgs:
			coinAvgs[coin] = []
		if winner[ts][coin] not in winners[coin]:
			winners[coin][winner[ts][coin]] = 0
		#winners[coin][winner[ts][coin]] = winners[coin][winner[ts][coin]] + 1
		#winners[winner[ts][coin]] = winners[winner[ts][coin]] + 1
		#directions[direction[ts][coin]] = directions[direction[ts][coin]] + 1
"""
avgs = []
negs = 0
for coin in coinvalues:
	coinvalues[coin] = coinvalues[coin] / (daysinsim / 365)
	coinvalues[coin] = coinvalues[coin] * 3# * 24 * 365
	#avg = sum(coinAvgs[coin]) / len(coinAvgs[coin])
	print(coin + ' average APY @ 5x leverage maintaining a hedge (10x total), if only focusing on futures cash n carry strategy and absorbing any losses from temporary spikes in funding +/-: ' + str(round(coinvalues[coin], 4) ) + '%')
	if coinvalues[coin] < 0:
		negs = negs + 1
	avgs.append(coinvalues[coin])
avgavg = sum(avgs) / len(avgs)
print(' ')
"""
print('Times funding was the play: ' + str(winners['funding']))
print('Times futures was the play: ' + str(winners['futures']))
print('Times we long perp, short futs: ' + str(directions['long perp, short futs']))
print('Times we short perp, long futs: ' + str(directions['short perp, long futs']))
print(' ')
"""
print('Average of all sustained APYs: ' + str(round(avgavg, 4)) + '%')
print(str(negs) + ' coins had negative net APYs. ' + str(round(negs / sum(avgs), 4) * 100) + '% of all coins.')

print(' ')
print(' ')
avgs = []
for coin in coinvalues:
	#coinvalues[coin] = coinvalues[coin] / (daysinsim / 365)
	#avg = sum(coinAvgs[coin]) / len(coinAvgs[coin])
	if coinvalues[coin] > avgavg:
		print(coin + ' is above average APY @ 5x leverage maintaining a hedge (10x total), if only focusing on futures cash n carry strategy and absorbing any losses from temporary spikes in funding +/-: ' + str(round(coinvalues[coin], 4) ) + '%')
		avgs.append(coinvalues[coin])
avgavg = sum(avgs) / len(avgs)
print(' ')

print('Average of all sustained APYs above the average: ' + str(round(avgavg, 4)) + '%')

"""

coinAvgs = {}
for ts in net_rates['net']:
	for coin in net_rates['net'][ts]:
		if coin not in coinAvgs:
			coinAvgs[coin] = []
		if net_rates['net'][ts][coin] < abs(avgavg):
			coinAvgs[coin].append(net_rates['net'][ts][coin])
avgs = []
for coin in coinAvgs:

	avg = sum(coinAvgs[coin]) / len(coinAvgs[coin])
	#print(coin + ' average APY: ' + str(round(avg) ) + '%')
	avgs.append(avg)
avgavg2 = sum(avgs) / len(avgs)
print(' ')
print('Average of all average APYs, excluding those outliers that are greater than the absolute value of the previou average: ' + str(round(avgavg2)) + '%')
"""