If you found this repo useful, consider clicking the sponsor button near the top :) Sponsoring via GitHub is as little as $1/month and if you do not use banks or credit cards, there are crypto links included :)<br /><br />
# New, much more profitable bot available in return for referral link use:

https://hacks.substack.com/p/huobi-trader-live-now-we-watch



Hey all, Remi, Lester, sim_tee,



Work has been progressing on this bot. On stream so far we've built and compared opportunities among exchanges for futures premium arbitrage and funding opportunities, then focused on Binance's coin margined futures which will cross margin the perpetuals perfectly hedged with futures to be a delta-neutral strategy that earns funding payments and doesn't have much exposure to the underlying's price up or down. 



Focusing on Binance had a number of advantages:



1. The funding opps we saw were second only to FTX, who have far many more options
2. The taker fee (to get into position as quickly as possible in order to avoid exposure we'd see if we limited into position, as well as delays) is 0.04% or 0.08% round-trip, vs 0.06% or 0.12% round-trip on FTX. 
3. There's a testnet! Our bot has been nearly fully tested without risking funds. Bonus!
4. More selfishly I'm a Binance Broker and I've inserted my Broker key into the code to market into position, making this bot a marketable business venture by contacting you folks. 
5. We have 75x leverage to play with instead of max 20x on most FTX markets. This magnifies returns. 



Note: in order for me to receive my broker revenues, please please use a Binance account that wasn't referred by another user. If you do have one already that had been referred, Binance will not mind if you open another account without using referral links and they'll even let you KYC verify it if you'd like to be able to withdraw more than 1 BTC a day. 



Hold on! Wait a min!



There's still some risks. 1. The net difference in hedge vs perp might not be more than the earning potential from funding (less fees). 2. That's about it...



So, I'm going to push a livenet version of the Binance coin-m funding bot to GitHub within the next hour or so, then put $25 to test it and put a chart of the balance up on YouTube for everyone to follow. We're specifically watching to see if the funding payments on every 8 hours outweigh the ups and downs of holding a perp and it's hedge. 



...
... ...
... ... ...



This email now exists as the GitHub readme. 



To use this project: 



1. Use a Binance account that wasn't referred by anyone. 
2. Edit app2.py and enter your key and secret. Note that you must create the key after enabling futures on your account, then edit the restrictions on the key and allow futures trading. 
3. Transfer funds into your coin margined futures. 
4. Run python app2.py. 
5. If any packages are missing it will tell you which ones and you can install them using the command pip install whatever. 



Note: on the coin-margined perps with futures, there were no opportunities at entry-level Binance fees (0.04%) at time of writing. As such, the bot has been redesigned to maker into position by making orders for 1/100 the size of where it wants to be, unless it's <5% of balance at leverage. This code is HIGHLY BETA. 



NEEDS a minimum balance of $1000 in BTC, split 1/4 evenly with ADA, ETH, LINK and BTC coin-m balances. If using a lesser balance, change divisor=100 along the top and replace with a number lesser than 100. Note this will create larger maker orders and mess up the exposure, meaning that my trial on youtube means basically nothing.




Alright so, coin-m futures need you to have balance in the coins you're looking to trade, rather than balance just in BTC. So, the script now assumes you have 1/4 your balance equally across LINK, ADA, ETH and BTC. I also was unable to test with my measly $25, as that wasn't enough for minimum trades into all those coins @ spot. USE AT OWN RISK. I haven't seen it enter into a set of orders yet.



The minimum funding opp is calculated by assuming that it doesn't long/short an entire position every time it readjusts every 8hrs. The minimum arb is therefore 410.625% APR, at leverage, a product of 0.015% fees, 75x leverage and 365x days in a year - which assumes that the +/- delta to get in a new position after adjusting for the first position is anything less than 1/3 a day.
