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
