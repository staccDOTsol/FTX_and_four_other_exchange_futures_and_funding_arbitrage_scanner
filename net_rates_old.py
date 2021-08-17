import json
import datetime
import dateutil.parser
import time
with open('futures_rates.json', 'r') as f:
	futures_rates = json.loads(f.read())['ftx']

with open('funding_rates.json', 'r') as f:
	funding_rates = json.loads(f.read())['ftx']
net_rates = {}
net_rates['futures'] = {}
net_rates['funding'] = {}
net_rates['net'] = {}
direction = {}
winner = {}
for st in futures_rates:
	d = dateutil.parser.parse(st)
	ts = time.mktime(d.timetuple())
	net_rates['net'][ts] = {}
	net_rates['futures'][ts] = futures_rates[st]
for st in funding_rates:
	d = dateutil.parser.parse(st)
	ts = time.mktime(d.timetuple())
	
	net_rates['funding'][ts] = funding_rates[st]

	coins = []

	for coin in funding_rates[st]:
		coins.append(coin)
	if ts in net_rates['futures']:
		if ts not in direction:
			direction[ts] = {}
			winner[ts] = {}
		for coin in net_rates['futures'][ts]:
			if coin in coins:

				if abs(net_rates['futures'][ts][coin]) > abs(net_rates['funding'][ts][coin]):
					winner[ts][coin] = 'futures'
					net_rates['net'][ts][coin] = abs(net_rates['futures'][ts][coin] - net_rates['funding'][ts][coin])
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
coinAvgs = {}
winners = {}
directions = {}
winners['funding'] = 0
winners['futures'] = 0
directions['long perp, short futs'] = 0

directions['short perp, long futs'] = 0
for ts in net_rates['net']:
	for coin in net_rates['net'][ts]:
		if coin not in winners:
			winners[coin] = {}
		if coin not in coinAvgs:
			coinAvgs[coin] = []
		if winner[ts][coin] not in winners[coin]:
			winners[coin][winner[ts][coin]] = 0
		coinAvgs[coin].append(net_rates['net'][ts][coin])
		winners[coin][winner[ts][coin]] = winners[coin][winner[ts][coin]] + 1
		winners[winner[ts][coin]] = winners[winner[ts][coin]] + 1
		directions[direction[ts][coin]] = directions[direction[ts][coin]] + 1
avgs = []
for coin in coinAvgs:

	avg = sum(coinAvgs[coin]) / len(coinAvgs[coin])
	print(coin + ' average APY: ' + str(round(avg) ) + '% and # times funding/futures won: ' + str(winners[coin]['funding']) + '/' + str(winners[coin]['futures']))
	avgs.append(avg)
avgavg = sum(avgs) / len(avgs)
print(' ')
print('Times funding was the play: ' + str(winners['funding']))
print('Times futures was the play: ' + str(winners['futures']))
print('Times we long perp, short futs: ' + str(directions['long perp, short futs']))
print('Times we short perp, long futs: ' + str(directions['short perp, long futs']))
print(' ')
print('Average of all average APYs: ' + str(round(avgavg)) + '%')
"""
print(' ')
print(' ')
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