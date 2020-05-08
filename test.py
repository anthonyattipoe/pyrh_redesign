from session import begin_robinhood_session, end_robinhood_session
from instrument import Instrument
from order import Order
from user import User
from portfolio import Portfolio

creds = open("credentials").readlines()
email = creds[0].strip()
password = creds[1].strip()


def test_quote():
    ins = Instrument(Instrument.Type.STOCK, "GOOG")
    print(ins.quote())


def test_user():
    print("testing Portfolio..............................")
    p = Portfolio()
    print(p)

    print("testing User...................................")
    user = User()

    print("Testing: order_history()")
    print(user.order_history())

    print("Testing: get_open_orders()")
    print(user.get_open_orders())


def test_instrument():
    print("testing Instrument..............................")
    amazon_stock = Instrument(Instrument.Type.STOCK, "AMZN")
    print("Amazon stock " + str(amazon_stock))
    print("Amazon stock symbol: " + str(amazon_stock.symbol()))
    print("Quote for Amazon stock: " + str(amazon_stock.quote()))
    print("Ask price x size: " + str(amazon_stock.ask_info()))
    print("Bid price x size: " + str(amazon_stock.bid_info()))
    print("Fundamental: " + str(amazon_stock.fundamental()))
    print("Historical data for Amazon: " + str(amazon_stock.historical_quotes("5minute", "week")))
    print("News: " + str(amazon_stock.news()))
    print("Option chain ID: " + str(amazon_stock.option_chain_id()))
    print("Market data for Amazon: " + str(amazon_stock.market_data()))
    print("Popularity of Amazon stock as measured by number of Robinhood users who own it: "
          + str(amazon_stock.popularity()))
    print("Last trade price of Amazon stock: " + str(amazon_stock.last_trade_price()))
    print("Price for Amazon stock last updated at: " + str(amazon_stock.last_updated_at()))
    print("Previous closing price for Amazon stock, not adjusted: " + str(amazon_stock.previous_close()))
    print("Previous closing price for Amazon stock, adjusted: " + str(amazon_stock.previous_close(adjusted=True)))

def test_order():
    # Q1: Can all instruments have any time in force? Is GTC only available for gold members? Or restricted to certain kinds of instruments?
    zomedica = Instrument(Instrument.Type.STOCK, 'ZOM') # Currently ~ $0.3
    print('*****************')
    print('PLACING BUY ORDER')
    print('*****************')
    zomedica_buy = Order(zomedica, Order.Type.BUY, quantity=3)
    response = zomedica_buy.place()
    print(response)
    print("")

    print('*****************')
    print('PLACING SELL ORDER')
    print('*****************')
    # Defaults to good for day.
    zoomedica_sell = Order(zomedica, Order.Type.SELL, quantity=1)
    print(zoomedica_sell.place())


if __name__ == "__main__":
    begin_robinhood_session(email, password)
    test_quote()
    test_user()
    test_instrument()
    test_order()
    end_robinhood_session()
