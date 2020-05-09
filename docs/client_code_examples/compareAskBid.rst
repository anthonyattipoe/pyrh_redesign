

Compare Ask Bid Example Code
============================

`Source Code Here <https://github.com/anthonyattipoe/pyrh_redesign/blob/master/client/compare_ask_bid.py>`_

.. code-block:: python

	from pyrh_redesign.instrument import Instrument
	import numpy as np
	import time
	import matplotlib.pyplot as plt
	from session import begin_robinhood_session, end_robinhood_session


	def get_ask_bid_periodically(ticker_symbol, iterations, interval):
	    timer = 0
	    ins = Instrument(Instrument.Type.STOCK, ticker_symbol)
	    ask_prices = np.zeros(iterations)
	    bid_prices = np.zeros(iterations)

	    while timer < iterations:
	        ask_price, ask_size = ins.ask_info()
	        ask_prices[timer] = float(ask_price) / ask_size
	        bid_price, bid_size = ins.ask_info()
	        bid_prices[timer] = float(bid_price) / bid_size
	        timer += 1
	        time.sleep(interval)

	    x = np.arange(iterations)
	    plt.clf()
	    plt.plot(x, ask_prices)
	    plt.plot(x, bid_prices)
	    plt.savefig("../results/ask_bid_prices_every_" + str(interval) + "s_" + ticker_symbol + ".jpg")


	if __name__ == "__main__":
	    creds = open("../credentials").readlines()
	    email = creds[0].strip()
	    password = creds[1].strip()
	    begin_robinhood_session(email, password)
	    get_ask_bid_periodically("AMZN", 60, 1)
	    get_ask_bid_periodically("AAPL", 60, 1)
	    end_robinhood_session()