from instrument import Instrument
from portfolio import Portfolio
from order import Order
from session import begin_robinhood_session, end_robinhood_session
from decimal import *
import heapq

def within_bounds(lower_bound, upper_bound, point):
	"""
	Returns true if the point is within the lower and upper bounds
	"""
	return (lower_bound < point) and (upper_bound > point)

# Keep my equity as 1/3 Facebook shares

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
	my_portfolio = Portfolio()
	available_funds = my_portfolio.excess_margin()
	invested_funds = my_portfolio.value(Portfolio.ValueType.MARKET_VALUE)
	equity_instrument = Instrument(Instrument.Type.STOCK, symbol_ticker)

	current_positions = my_portfolio.positions()

	available_quantity = 0.0
	quantity_equity = 0.0


	weights = []
	symbol_quantity = 0
	symbol_value = 0.0

	for position in current_positions:
		check_instrument = Instrument(Instrument.Type.STOCK, position['symbol'])

		if position['symbol'] == symbol_ticker:
			symbol_quantity, symbol_value = my_portfolio.share_info(check_instrument)
			continue

		quantity, value = my_portfolio.share_info(check_instrument)
		heapq.heappush(weights, [-value, quantity, position['symbol']])

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

	return_orders = []

	if trade == Order.Type.SELL:
		sell_order = Order(equity_instrument,trade,needed_shares_to_sell,Order.TimeInForce.GFD)
		return_orders += [sell_order]
		trade = Order.Type.BUY
	else:
		buy_order = Order(equity_instrument,trade,needed_shares_to_buy,Order.TimeInForce.GFD)
		return_orders += [buy_order]
		trade = Order.Type.SELL

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

	print("Suggested Order List:")
	for order in return_orders:
		print(str(order))
		print("\n##########################################\n")

	return return_orders


if __name__ == "__main__":
    creds = open("credentials").readlines()
    email = creds[0].strip()
    password = creds[1].strip()
    begin_robinhood_session(email, password)
    maintain_equity("ZOM",Decimal(1/3),Decimal(.05))
    end_robinhood_session()