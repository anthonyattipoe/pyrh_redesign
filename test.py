from session import begin_robinhood_session, end_robinhood_session
from instrument import Instrument
from order import Order
from user import User
from portfolio import Portfolio

creds = open("credentials").readlines()
email = creds[0].strip()
password = creds[1].strip()


def pretty_print(text):
    print('*****************')
    print(text)
    print('*****************')
    print('')

def test_quote():
    ins = Instrument(Instrument.Type.STOCK, "GOOG")
    print(ins.quote())

def test_portfolio():
    pretty_print("TESTING PORTFOLIO")
    p = Portfolio()
    print(p)

def test_positions():
    pretty_print('TESTING POSITIONS')
    pos = Portfolio().positions()
    print(pos)

def test_order_history():
    pretty_print('TESTING ORDER HISTORY')
    user = User()
    print(user.order_history())

def test_open_orders():
    pretty_print('TESTING OPEN ORDERS')
    user = User()
    print(user.get_open_orders())

def test_instrument():
    pretty_print("TESTING INSTRUMENT")
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

def test_buy_order():
    pretty_print('TESTING BUY ORDER')
    zom = Instrument(Instrument.Type.STOCK, 'ZOM')
    zom_order = Order(zom, Order.Type.BUY, quantity=3)
    print(zom_order.place())

def test_sell_order():
    pretty_print('TESTING SELL ORDER')
    zom = Instrument(Instrument.Type.STOCK, 'ZOM')
    zom_order = Order(zom, Order.Type.SELL, quantity=1)
    print(zom_order.place())

def test_limit_buy_order():
    pretty_print('TESTING LIMIT BUY ORDER')
    zom = Instrument(Instrument.Type.STOCK, 'ZOM')
    zom_order = Order(zom, Order.Type.LIMIT_BUY_ORDER, quantity=2, time_in_force=Order.TimeInForce.GTC, price=0.25)
    print(zom_order.place())

def test_limit_sell_order():
    pretty_print('TESTING LIMIT SELL ORDER')
    zom = Instrument(Instrument.Type.STOCK, 'ZOM')
    zom_order = Order(zom, Order.Type.LIMIT_SELL_ORDER, quantity=1, time_in_force=Order.TimeInForce.GTC, price=0.275)
    print(zom_order.place())

def test_market_buy_order():
    pretty_print('TESTING MARKET BUY ORDER')
    zom = Instrument(Instrument.Type.STOCK, 'ZOM')
    zom_order = Order(zom, Order.Type.MARKET_BUY_ORDER, quantity=2, time_in_force=Order.TimeInForce.GTC)
    print(zom_order.place())

def test_market_sell_order():
    pretty_print('TESTING MARKET SELL ORDER')
    zom = Instrument(Instrument.Type.STOCK, 'ZOM')
    zom_order = Order(zom, Order.Type.MARKET_SELL_ORDER, quantity=1, time_in_force=Order.TimeInForce.GFD)
    print(zom_order.place())

def test_stop_limit_buy_order():
    pretty_print('TESTING STOP LIMIT BUY ORDER')
    zom = Instrument(Instrument.Type.STOCK, 'ZOM')
    zom_order = Order(zom, Order.Type.STOP_LIMIT_BUY_ORDER, quantity=2, time_in_force=Order.TimeInForce.GTC, price=0.250, stop_price=0.275)
    print(zom_order.place())

def test_stop_limit_sell_order():
    pretty_print('TESTING STOP LIMIT SELL ORDER')
    zom = Instrument(Instrument.Type.STOCK, 'ZOM')
    zom_order = Order(zom, Order.Type.STOP_LIMIT_SELL_ORDER, quantity=2, time_in_force=Order.TimeInForce.GTC, price=0.250, stop_price=0.20)
    print(zom_order.place())

def test_stop_loss_buy_order():
    pretty_print('TESTING STOP LOSS BUY ORDER')
    zom = Instrument(Instrument.Type.STOCK, 'ZOM')
    zom_order = Order(zom, Order.Type.STOP_LOSS_BUY_ORDER, quantity=2, time_in_force=Order.TimeInForce.GTC, stop_price=0.255)
    print(zom_order.place())

def test_stop_loss_sell_order():
    pretty_print('TESTING STOP LOSS SELL ORDER')
    zom = Instrument(Instrument.Type.STOCK, 'ZOM')
    zom_order = Order(zom, Order.Type.STOP_LOSS_SELL_ORDER, quantity=2, time_in_force=Order.TimeInForce.GTC, stop_price=0.200)
    print(zom_order.place())

if __name__ == "__main__":
    begin_robinhood_session(email, password)
    # test_quote()
    # test_portfolio()
    # test_positions()
    # test_order_history()
    # test_open_orders()
    # test_instrument()
    # test_buy_order()
    # test_sell_order()
    # test_limit_buy_order()
    # test_limit_sell_order()
    # test_market_buy_order()
    # test_market_sell_order()
    # test_stop_limit_buy_order()
    # test_stop_limit_sell_order()
    # test_stop_loss_buy_order()
    test_stop_loss_sell_order()
    end_robinhood_session()
