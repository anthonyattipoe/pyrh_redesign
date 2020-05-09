

Maintaining Equity Example Walkthrough
======================================

Let's say that I would like to keep my market value of a certain stock at a certain percentage of my portfolio.

I'm going to choose Facebook for example (the ticker is "FB")

Also in this example, I am going to keep my market value at 1/3 of my current equity with a 5% tolerance

Let's first do our login process and start our session, then call our function maintain_equity

.. code-block:: python

	if __name__ == "__main__":
	    creds = open("credentials").readlines()
	    email = creds[0].strip()
	    password = creds[1].strip()
	    begin_robinhood_session(email, password)
	    # Facebook ticker, at 1/3 balance, with 5% tolerance
	    maintain_equity("FB",Decimal(1/3),Decimal(.05))
	    end_robinhood_session()

We should also define a helper function that will let us see if we're within our tolerance

.. code-block:: python

	def within_bounds(lower_bound, upper_bound, point):
		"""
		Returns true if the point is within the lower and upper bounds
		"""
		return (lower_bound < point) and (upper_bound > point)

And give a function definition of our maintain_equity function

.. code-block:: python

	def maintain_equity(symbol_ticker, desired_portion, tolerance):
		"""
		Maintains equity of stocks you own to a certain percentage.

		Args:
			symbol_ticker: str of the symbol
			desired_portion: Decimal value of the fraction you want your portfolio
							 to be of this stock
			tolerance: Decimal value of the tolerance you can respect with your
					   desired portion

		Returns:
			list of Orders that are suggested to maintain the desired_portion
		"""

In this block we are going to get our portfolio, the available funds of money we can spend, 
and the amount of money in our portfolio at market value.

We also need to create an instrument based off our stock and then we'll gather all our positions to 
filter through our stock.

.. code-block:: python

	def maintain_equity(symbol_ticker, desired_portion, tolerance):
		my_portfolio = Portfolio()
		available_funds = my_portfolio.excess_margin()
		invested_funds = my_portfolio.value(Portfolio.ValueType.MARKET_VALUE)
		equity_instrument = Instrument(Instrument.Type.STOCK, symbol_ticker)
		current_positions = my_portfolio.positions()
	...

Since we are focused on rebalancing, we'll weigh our entire portfolio and specific instrument

.. code-block:: python

	...
		weights = []
		symbol_quantity = 0
		symbol_value = 0.0
	...

As we loop through our positions, we create an instrument to check if it matches our symbol.
If it does match our symbol, then we'll get the quantity and value in our portfolio.
For all others in our portfolio, we save the quantity, value, and symbol for later calculation on a max-heap.

* Note - to create a max-heap we needed to save a negative value of the price. 

.. code-block:: python
	
	...
		for position in current_positions:
			check_instrument = Instrument(Instrument.Type.STOCK, position['symbol'])

			if position['symbol'] == symbol_ticker:
				symbol_quantity, symbol_value = my_portfolio.share_info(check_instrument)
				continue

			quantity, value = my_portfolio.share_info(check_instrument)
			heapq.heappush(weights, [-value, quantity, position['symbol']])
	...

This is where the code can be tricky. First we generate the weight of the desired symbol and note the difference
between what we want our symbol to be weighted as versus what it is now. Since the difference can be negative or positive,
We need to account for buying or selling the shares to maintain the weight. We also now have a set of reallocated funds,
the money from buying/selling, to redistribute between our remaining positions. 

We set trade based off of the Order Type we need.

.. code-block:: python

	...
		weight = (symbol_quantity*symbol_value)/invested_funds
		difference = desired_portion - weight
		needed_shares_to_buy = 0
		needed_shares_to_sell = 0
		reallocated_funds = invested_funds*difference

		if difference > 0:
			trade = Order.Type.BUY
			needed_shares_to_buy = (reallocated_funds)//symbol_value
		elif difference < 0:
			trade = Order.Type.SELL
			reallocated_funds = reallocated_funds*-1
			needed_shares_to_sell == (reallocated_funds)//symbol_value
		else:	
			return
	...

The return_orders value is a list of order to later be placed by us if we want to go through with the 
suggestions. Based off our order type we'll create an order and append it to our list. We then set
the trade value equal to the opposite of the current value because we would need to buy/sell other stocks
to reach our goal.

.. code-block:: python

	...
		return_orders = []

		if trade == Order.Type.SELL:
			sell_order = Order(equity_instrument, trade, needed_shares_to_sell, Order.TimeInForce.GFD)
			return_orders += [sell_order]
			trade = Order.Type.BUY
		else:
			buy_order = Order(equity_instrument, trade, needed_shares_to_buy, Order.TimeInForce.GFD)
			return_orders += [buy_order]
			trade = Order.Type.SELL
	...

In this block we set the bounds with our tolerance of what is acceptable and start a running total of what
we've spent so far. While the total spent is not within the bounds we grab one of the heaviest weights,
buy or sell as many as we can, and then add the order to our list. This is a greedy-like algorithm so we can
do it in as few orders as possible.


.. code-block:: python

	...
		lower_bound = reallocated_funds - (reallocated_funds*tolerance)
		upper_bound = reallocated_funds + (reallocated_funds*tolerance)

		total_spent = 0

		while not (within_bounds(lower_bound, upper_bound, total_spent)):
			try:
				[value, quantity, ticker] = weights.pop()
				shares_needed = int((reallocated_funds-total_spent)/value)
				instrument_trade = Instrument(Instrument.Type.STOCK, ticker)
				if shares_needed >= quantity:
					add_to_order = Order(instrument_trade, trade, quantity, Order.TimeInForce.GFD)
					total_spent += quantity*value
				else:
					add_to_order = Order(instrument_trade, trade, quantity-shares_needed, Order.TimeInForce.GFD)
					total_spent += (quantity-shares_needed)*value
				return_orders += [add_to_order]
			except:
				break

		return return_orders
	...

Then all we have to do is return our orders!

* Post-Script Note - to place these orders, one would have to have to sell and then buy if there are insufficient funds to make additional buy orders.


