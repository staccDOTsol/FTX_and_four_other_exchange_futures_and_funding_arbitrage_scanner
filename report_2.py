import json
import datetime
from datetime import timedelta
import dateutil.parser
import time
import requests
import pandas as pd
import matplotlib.pyplot as plt
volume = 0
closedlongs = 0
closedshorts = 0
#Enter the ticker of the companies that you want to analyse
#companies = ['AAPL','FB','GOOG','F','TSLA']
#empty list to add each of the companies
listofdf = []


entries = {}
with open('futures_rates.json', 'r') as f:
	futures_rates = json.loads(f.read())['ftx']

with open('funding_rates.json', 'r') as f:
	funding_rates = json.loads(f.read())['ftx']
net_rates = {}
net_rates['futures'] = {}
net_rates['funding'] = {}
net_rates['net'] = {}
equity = 100000 * 6
startequity = 100000 * 6
		#768477
freeequity = equity
freeequitys = 0

equitys = 0


hodling = {}
direction = {}
winner = {}
maxts = 0
mints = 99999999999999999999
tfr = {}
futures_rates2 = []
funding_rates2 = []
backwards = []
tssts = {}
tssts2 = {}
for st in funding_rates:
	d = dateutil.parser.parse(st).replace(tzinfo=dateutil.tz.gettz('UTC'))
	
	ts = time.mktime(d.timetuple())
	backwards.append(ts)
	funding_rates[st]['st'] = st
	futures_rates[st]['st'] = st
	tssts[ts] = funding_rates[st]
	tssts2[ts] = futures_rates[st]
backwards.reverse()
tfutsrs = {}
tfundrs = {}
for ts in backwards:
	tfutsrs[tssts2[ts]['st']] = tssts2[ts]
	tfundrs[tssts[ts]['st']] = tssts[ts]
funding_rates = tfundrs
futures_rates = tfutsrs
"""
for st in futures_rates:
	st = st
	futures_rates2.append(futures_rates[st])

for st in funding_rates:
	st = st
	funding_rates2.append(funding_rates[st])
futures_rates = sorted(futures_rates2, key=lambda x: dateutil.parser.parse(x['st']))
funding_rates = sorted(funding_rates2, key=lambda x: dateutil.parser.parse(x['st']))
futures_rates.reverse()
#for st in futures_rates:
	#print(st)
	#sleep(100)
funding_rates.reverse()

for st in futures_rates:

	st = st
for st in funding_rates:

	st = st
"""
for st in futures_rates:


	d = dateutil.parser.parse(st)
	ts = time.mktime(d.timetuple())
	if maxts < ts:
		maxts = ts
	if mints > ts:
		mints = ts
	#print(futures_rates[st])
	net_rates['net'][ts] = {}
	net_rates['futures'][ts] = futures_rates[st]
diff = maxts - mints
diff = diff / 365 / 24 
daysinsim = diff
#equity = 100000
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
tsold = 0
ts = 0
expis = ['PERP', '1231', '0924', '0625', '0326']
trades = {}
trades['BTC'] = {}
todo = ["BTC", "ETH", "BNB", "ADA", "XRP", "DOT","UNI","SOL"]
import pandas as pd

for coin in todo:
	trades[coin] = {}
	for exp in expis:
		try:
			df = pd.read_json (coin + '-' + exp + '-trades.json')
			
			#df['Datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])
			trades[coin][exp] = df
			trades[coin][exp]['date'] = pd.to_datetime(trades[coin][exp]['time'])
			if exp == 'PERP' and coin == 'BTC':
				start, end = trades[coin][exp]['date'].iloc(-1), trades[coin][exp]['date'].iloc(0)
				print(start)
				print(end)
				print(end - start)
			print(len(trades[coin][exp]))
			#trades[coin][exp] = trades[coin][exp].set_index('time')

			
			# = idx.DataFrame(index=idx)

			#print(len(trades[coin][exp]))
		except Exception as e: 
			print(e)
tradesst = {}
import dateutil.tz

utc = dateutil.tz.gettz('UTC')

d = None
from time import sleep
"""
for st in funding_rates:
	tradesst[st] = {}
	tsold = d
	d = dateutil.parser.parse(st).replace(tzinfo=dateutil.tz.gettz('UTC'))
	
	ts = d#time.mktime(d.timetuple())
	if tsold == None:
		tsold = d - timedelta(minutes=1)
	#print( ' ')
	#print(str((tsold - ts).total_seconds()))
	for coin2 in todo:
		try:
			for exp in trades[coin2]:
				#print(exp)
				#tradesst[st][exp] = []
				#d3 = dateutil.parser.parse(trades[coin2][exp][0]['time']) - timedelta(hours=4)
					
				#ts3 = time.mktime(d3.timetuple())
				#print(ts)
				#print(tsold)
				#print(ts3)
				#print(' ')
				#print(trades[coin2][exp])
				mask = (trades[coin2][exp]['date'] > tsold) & (trades[coin2][exp]['date'] <= ts)
				df = trades[coin2][exp].loc[mask]
				#print(len(df))
				thetrades = []
				for side in df['side']:
					thetrades.append([side])
				a = 0
				for price in df['price']:
					thetrades[a].append(price)
					a = a + 1
				a = 0
				for size in df['size']:
					thetrades[a].append(size)
					a = a + 1
				print(thetrades)
				#sleep(100)
				if True:
					sleep(1)
					#print(len(trades['BTC'][exp]))
					#print(trade['time'])
					#d2 = dateutil.parser.parse(trade['time']) - timedelta(hours=4)
					#print(d2)
					#sleep(100)
					#ts2 = time.mktime(d2.timetuple())
					#print(ts)
					#print(tsold)
					#print(ts2)
					#sleep(100)
					#print(tsold)
					if True:# ts2 < ts and ts2 > tsold:
						#print(ts2)

						#tradesst[st][exp].append(trade)
						
						if wanted[coin] > hodling[coin] and trade['side'] == 'buy':
							hodling[coin] = hodling[coin] +  (trades['size'] * trades['price']) / 100 / 1
							freeequity = freeequity - (trades['size'] * trades['price']) / 100 / 1
						if wanted[coin] < hodling[coin] and trade['side'] == 'sell':
							hodling[coin] = hodling[coin] -  (trades['size'] * trades['price']) / 100 / 1
							freeequity = freeequity + (trades['size'] * trades['price']) / 100 / 1

						print(hodling)
						print(freeequity)

						
						abc=123#trades[coin2][exp].remove(trade)
		except:
			abc=123
with open('tradesst.json', 'w') as f:
	f.write(json.dumps(tradesst))
sleep(100)
"""
dold = None
d = None
dbegin = None 
if True:#for coin in trades:
	exp = 'PERP'
	coin = 'BTC'
	#for name, values in trades[coin][exp].iteritems():
		#if name == 'time':
			#for v in values:


#	for index in enumerate(trades[coin][exp]['time']):

	d4 = trades[coin][exp]['date'].min()

#d = dateutil.parser.parse(d2).replace(tzinfo=dateutil.tz.gettz('UTC'))
	#d4 = dateutil.parser.parse(d3).replace(tzinfo=dateutil.tz.gettz('UTC'))

	if dbegin == None:
		dbegin = d4
	if d4 < dbegin:
		dbegin = d4
print(dbegin)
tequities = {}
#sleep(100)
theprices = {}
equities = []
amts = {}
amtb = {}
for st in funding_rates:

	#print(st)
	opps = {}
	wanted = {}
	dold = d
	d = dateutil.parser.parse(st).replace(tzinfo=dateutil.tz.gettz('UTC'))
	if d > dbegin:
		if dold == None:
			dold = d - timedelta(minutes=1)
		tsold = ts
		ts = time.mktime(d.timetuple())
		net_rates['funding'][ts] = funding_rates[st]
		#net_rates['futures'][ts] = futures_rates[st]
		coins = []
		topp = 0
		for coin in funding_rates[st]:
			if coin in todo:
				#print(coin)
				if coin not in hodling:

					hodling[coin] = {}
					for expi in expis:
						hodling[coin][expi]  = 0
				else:
					if 'PERP' not in expi:
						if dateutil.parser.parse('2021/' + expi[:-2] + '/' + expi[2:]).replace(tzinfo=dateutil.tz.gettz('UTC')) < d:
							hodling[coin][expi]  = 0
				coins.append(coin)

		#print(net_rates['futures'])
		if ts in net_rates['futures']:
			#print(ts)
			if ts not in direction:
				net_rates['net'][ts] = {}
				direction[ts] = {}
				winner[ts] = {}
			for coin in net_rates['futures'][ts]:
				equity = startequity + equitys
				freeequity = startequity + freeequitys

			
			
				#print(coin)
				#coin = 'BTC'
				if coin in coins:
					if coin not in net_rates['net'][ts]:
						net_rates['net'][ts][coin] = 0
						#print(coin)
					#11000 / 100 / 1, positive means short perps
					#funding negative means long perps
					#funding positive means short perps

					#negative means long perps


					#if abs(net_rates['futures'][ts][coin]) > abs(net_rates['funding'][ts][coin]):
					winner[ts][coin] = 'futures'
					#print(topp)
					if (net_rates['futures'][ts][coin] < 0 and net_rates['funding'][ts][coin] < 0) or (net_rates['futures'][ts][coin] > 0 and net_rates['funding'][ts][coin] > 0):

						net_rates['net'][ts][coin] = (net_rates['futures'][ts][coin] / 365 / 24) + (net_rates['funding'][ts][coin] / 365 / 24)
						topp = topp + abs(net_rates['futures'][ts][coin] / 365 / 24) + abs(net_rates['funding'][ts][coin] / 365 / 24)
					
					else: #fut -40 fund 20, =20
					#fut -20 fund 40, =-20
					#fut 40 fund -20, =20
					#fut 20 fund -40, =-20
						net_rates['net'][ts][coin] =  (net_rates['futures'][ts][coin] / 365 / 24) - (net_rates['funding'][ts][coin] / 365 / 24)
					
						#else:

						topp = topp + abs(net_rates['futures'][ts][coin] / 365 / 24) - abs(net_rates['funding'][ts][coin] / 365 / 24)
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
			topps = 0
			

			for coin in net_rates['net'][ts]:
				
				#print(coin)
				opps[coin] = (net_rates['net'][ts][coin] / topp)# / 2 * 6
				topps = topps + opps[coin]
				wanted[coin] = {}

				if coin not in entries:
					entries[coin] = {}

				for expi in expis:

					if expi not in entries[coin]:
						entries[coin][expi] = []
					if expi != 'PERP':
						wanted[coin][expi] = -1 * ((abs(opps[coin] * equity) / 2) * 6)# / len(todo)
					else:
						wanted[coin][expi] = (abs(opps[coin] * equity) / 2 * 6)# / len(todo)
					exp = expi
					
				for exp in trades[coin]:
					#print(exp)
					if exp not in entries[coin]:
						entries[coin][exp] = []
					if coin not in amtb:
						amtb[coin] = {}
						amts[coin] = {}
					if exp not in amtb[coin]:
						amtb[coin][exp] = 0
					if exp not in amts[coin]:
						amts[coin][exp] = 0
					coin2 = coin
					mask = (trades[coin2][exp]['date'] > dold) & (trades[coin2][exp]['date'] <= d)
				
					df = trades[coin2][exp].loc[mask]
					#if len(df) > 0:
					#	print(len(df))
					thetrades = []
					for side in df['side']:
						thetrades.append([side])
					a = 0
					for price in df['price']:
						thetrades[a].append(price)
						a = a + 1
					if coin not in theprices:
						theprices[coin] = {}
					theprices[coin][exp] = price
					a = 0
					for size in df['size']:
						thetrades[a].append(size)
						a = a + 1
					#print(thetrades)
					#sleep(0.05)
					for trade in thetrades:
							#print(trade[0])

							if wanted[coin][exp] > hodling[coin][exp] and trade[0] == 'buy':
								gogo = True
								if 'PERP' in exp:
									futsb = 0
									#perp -10000 futs 11000 sell
									#perp -11000 futs 10000 not sell
									#perp 10000 futs -11000 not sell
									#perp 11000 futs -10000 do sell
									for eee in expis:
										if 'PERP' not in eee:
											futsb = futsb + abs(hodling[coin][eee])
									if (hodling[coin][exp]) < 0:
										if futsb >  abs(hodling[coin][exp])* 1.15:
											gogo = False
									else:
										if futsb < abs(hodling[coin][exp]) * 0.85:
											gogo = False
								else:
									futsb = 0
									#perp -10000 futs 11000 sell
									#perp -11000 futs 10000 not sell
									#perp 10000 futs -11000 not sell
									#perp 11000 futs -10000 do sell
									for eee in expis:
										if 'PERP' not in eee:
											futsb = futsb + abs(hodling[coin][eee])
									if (hodling[coin][exp]) < 0:
										if  abs(hodling[coin][exp]) > futsb * 1.01:
											gogo = False
									else:
										if abs(hodling[coin][exp]) < futsb * 0.99:
											gogo = False
								if gogo == True:
									if ((trade[2] * trade[1]) / 100 / 1) < equity / 100:
										volume = volume +  ((trade[2] * trade[1]) / 100 / 1)
										amtb[coin][exp] = amtb[coin][exp] + (trade[2] / 100 / 1)
										#print(entries[coin][exp])
										
														
										entries[coin][exp].append(['buy', (trade[2] / 100 / 1), trade[1] * (1 - (0.0001))])
										hodling[coin][exp] = hodling[coin][exp] +  ((trade[2] * trade[1]) / 100 / 1)
										#freeequity = freeequity - ((trade[2] * trade[1]) / 100 / 1)# / 6
							if wanted[coin][exp] < hodling[coin][exp] and trade[0] == 'sell':
								gogo = True
								if 'PERP' in exp:
									futsb = 0
									#perp -10000 futs 11000 sell
									#perp -11000 futs 10000 not sell
									#perp 10000 futs -11000 not sell
									#perp 11000 futs -10000 do sell
									for eee in expis:
										if 'PERP' not in eee:
											futsb = futsb + abs(hodling[coin][eee])
									if (hodling[coin][exp]) < 0:
										if abs(hodling[coin][exp]) > futsb * 1.15:
											gogo = False
									else:
										if abs(hodling[coin][exp]) < futsb * 0.85:
											gogo = False
								else:
									futsb = 0
									#perp -10000 futs 11000 sell
									#perp -11000 futs 10000 not sell
									#perp 10000 futs -11000 not sell
									#perp 11000 futs -10000 do sell
									for eee in expis:
										if 'PERP' not in eee:
											futsb = futsb + abs(hodling[coin][eee])
									if (hodling[coin][exp]) < 0:
										if futsb  > abs(hodling[coin][exp]) * 1.01:
											gogo = False
									else:
										if futsb < abs(hodling[coin][exp]) * 0.99:
											gogo = False
								if gogo == True:
									if ((trade[2] * trade[1]) / 100 / 1) < equity / 100:
										volume = volume +  ((trade[2] * trade[1]) / 100 / 1)
										amts[coin][exp] = amts[coin][exp] + (trade[2] / 100 / 1)
										
										entries[coin][exp].append(['sell', (trade[2] / 100 / 1), trade[1] * (1 + (0.0001))])
										hodling[coin][exp] = hodling[coin][exp] -  ((trade[2] * trade[1]) / 100 / 1)
								#freeequity = freeequity - (((trade[2] * trade[1]) / 100 / 1) - 
							"""
							if wanted[coin][exp] > hodling[coin][exp] and trade[0] == 'sell':
								hodling[coin][exp] = hodling[coin][exp] -  ((trade[2] * trade[1]) / 100 / 1) / 50
								freeequity = freeequity + ((trade[2] * trade[1]) / 100 / 1)# / 6
							if wanted[coin][exp] < hodling[coin][exp] and trade[0] == 'buy':
								hodling[coin][exp] = hodling[coin][exp] +  ((trade[2] * trade[1]) / 100 / 1) /50
								freeequity = freeequity - ((trade[2] * trade[1]) / 100 / 1) / 50# / 6
							"""
					#print(hodling)
					#print(freeequity)	
			for coin in entries:
				"""
				saveb = 0
				saves = 0
				count = 0
				total = 0
				percsb = {}

				percss = {}
				ts = 0
				tb = 0
				for exp in entries[coin]:
					if amts[coin][exp] > 0:
						count = count + 1
						ts = ts + amts[coin][exp]
					if amtb[coin][exp] > 0:
						count = count + 1
						tb = tb + amtb[coin][exp]
				for exp in entries[coin]:	
						percss[exp] = amts[coin][exp] / ts
						percsb[exp] = amtb[coin][exp] / tb
				print(percsb)
				print(percss)
				for exp in entries[coin]:
					if amts[coin][exp] == 0:
						amts[coin][exp] = tb * percsb[exp]
					if amtb[coin][exp] == 0:
						amtb[coin][exp] = ts * percss[exp]
						#saveb = saveb + amtb[coin][exp]
						#saves = saves + amts[coin][exp]

					for entry in entries[coin][exp]:
							
							if exp == 'PERP':
								saves = amts[coin][exp]
								saveb = amtb[coin][exp]
								abt = 0
								ast = 0
								for exp2 in entries[coin]:
									#print(exp2)
									if exp2 != 'PERP':

										ast = ast + amts[coin][exp]
										abt = abt + amtb[coin][exp]
										if amtb[coin][exp2] == 0:
											amtb[coin][exp2] = saves

										if amts[coin][exp2] == 0:
											amts[coin][exp2] = saveb
											print(amts[coin][exp2])
							
				#for coin in entries:
				amtb[coin]['PERP'] = saves
				amts[coin]['PERP'] = saveb
				
				winner2 = None
				most = 0
				for exp in entries[coin]:
					if hodling[coin][exp] > most:
						most = hodling[coin][exp]
						winner2 = exp
				for exp in entries[coin]:
					amtb2 = amtb[coin][exp]
					amts2 = amts[coin][exp]
					if exp != 'PERP':
						print(2)
						print(amtb[coin][exp])
						print(amts[coin]['PERP'])
						if amtb[coin][exp] == 0:
							amtb2 = amts[coin]['PERP']
						
						if amts[coin][exp] == 0:
							amts2  = amtb[coin]['PERP']
						
						#oldexp = exp
						exp123 = 'PERP'
					else:
						print(1)
						print(amtb[coin]['PERP'] )
						print(amts[coin][exp])
						if amts[coin]['PERP'] == 0:
							amtb2 = amts[coin][exp]
						
						if amtb[coin]['PERP'] == 0:
							amts2 = amtb[coin][exp]
						#oldexp = exp
						#amts[coin][exp] = amts[coin]['PERP']
						exp123 = winner2
					print( ' ' )
					print(amtb2)
					print(amts2)
					print( ' ' )
				"""
				for exp in amtb[coin]:
				#if True:
					theprice = theprices[coin][exp]
					amtb2 = amts[coin][exp]
					amts2 = amtb[coin][exp]
					for entry in entries[coin][exp]:	
							if entry[0] == 'buy':
								freeequity = freeequity - (entry[1] * (theprice - entry[2])) 
							else:
								freeequity = freeequity - (entry[1] * (entry[2] - theprice)) 
							if entry[0] == 'buy':
								equity = equity + (entry[1] * (theprice - entry[2])) 
							else:
								equity = equity + (entry[1] * (entry[2] - theprice))
							if entry[0] == 'sell' and amtb2 > 0:
								
								if amtb2 > entry[1]:
									
									#print(equity)
									
									amtb2 = amtb2 - entry[1]
									amts[coin][exp] = amts[coin][exp] - entry[1]
									if entry[0] == 'buy':
										freeequitys = freeequitys - (entry[1] * (theprice - entry[2])) 
									else:
										freeequitys = freeequitys - (entry[1] * (entry[2] - theprice)) 
									if entry[0] == 'buy':
										equitys = equitys + (entry[1] * (theprice - entry[2])) 
									else:
										equitys = equitys + (entry[1] * (entry[2] - theprice))
									entries[coin][exp].remove(entry)
									closedlongs = closedlongs + 1
									#print(len(entries[coin][exp]))
								else:
									entry[1] = entry[1]  - amtb[coin][exp]
									
									amtb2 = 0#amtb[coin][exp] - entry[1]
									amts[coin][exp] = 0

							if entry[0] == 'buy' and amts2 > 0:
								
								if amts2 > entry[1]:
									
									#print(equity)
									if entry[0] == 'buy':
										freeequitys = freeequitys - (entry[1] * (theprice - entry[2])) 
									else:
										freeequitys = freeequitys - (entry[1] * (entry[2] - theprice)) 
									if entry[0] == 'buy':
										equitys = equitys + (entry[1] * (theprice - entry[2])) 
									else:
										equitys = equitys + (entry[1] * (entry[2] - theprice))
									amts2 = amts2 - entry[1]
									amtb[coin][exp] = amtb[coin][exp] - entry[1]
									entries[coin][exp].remove(entry)
									closedshorts = closedshorts + 1
									#print(len(entries[coin][exp]))
								else:
									entry[1] = entry[1] - amts[coin][exp]
									
									amts2 = 0#amts[coin][exp] - entry[1]
									amtb[coin][exp] = 0
								#print(len(entries))
							
							#print(theprice)
							#print(entry[2])
							#print(entry)
							
					
					#equity = equity + freeequity
					
					print('1 and 2')
					print(amts2)
					print(amtb2)
	print(' ')
	print(hodling)
	print(freeequity)
	print(equity)
	print(volume)
	#sleep(1)
	if equity < startequity * 1.5:
		equities.append({'date': d, 'equity': equity})
	print(' ')
df = pd.DataFrame(equities)

#listofdf.append(df)
#set index of each DataFrame by common column before concatinatinghtem
df = df.set_index('date')

#histpriceconcat = pd.concat(dfs,axis=1)

for i, col in enumerate(df.columns):
    df[col].plot()

plt.title('Equity $ Delta, closed longs/shorts: ' + str(closedlongs) + '/' + str(closedshorts))

plt.xticks(rotation=70)
plt.legend(df.columns)
plt.show()

#Saving the graph into a JPG file
plt.savefig('foo1.png', bbox_inches='tight')
