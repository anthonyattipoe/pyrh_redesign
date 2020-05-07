from enum import Enum
from session import begin_robinhood_session, end_robinhood_session
import __init__


class Instrument:
    """A tradeable instrument on the Robinhood platform."""

    class Type(Enum):
        """The type of instrument in question."""
        STOCK = 1
        BOND = 2
        ETF = 3
        CRYPTO = 4

    def __init__(self, instrument_type, symbol):
        """Creates a new object which can be used to track
        updates about an instrument or be included in an order.

        Args:
            instrument_type: an enum delineating the type of instrument.
            symbol: the symbol corresponding with the desired instrument.

        Returns:
            An instrument object.

        Raises:
            MalformedInstrumentError: If an invalid combination of symbol and instrument type is provided.
        """
        self.instrument_type = instrument_type
        self.ticker_symbol = symbol
        self.rh = __init__.session_token.rh

    def __str__(self):
        """Custom pretty print function for an Instrument"""
        """prints instrument data"""
        return self.ticker_symbol

    def symbol(self):
        return self.ticker_symbol

    def quote(self):
        return self.rh.quote_data(self.ticker_symbol)

    def ask_info(self):
        price_string = self.rh.ask_price(self.ticker_symbol)
        price = float(price_string[0][0])
        size_string = self.rh.ask_size(self.ticker_symbol)
        size = float(size_string[0][0])
        return price, size

    def bid_info(self):
        price_string = self.rh.bid_price(self.ticker_symbol)
        price = float(price_string[0][0])
        size_string = self.rh.bid_size(self.ticker_symbol)
        size = float(size_string[0][0])
        return price, size

    def fundamental(self):
        return self.rh.get_fundamentals(self.ticker_symbol)

    def historical_quotes(self, interval, span):
        return self.rh.get_historical_quotes(interval, span)

    def news(self):
        return self.rh.get_news(self.ticker_symbol)

    def option_chain(self):
        return self.rh.get_option_chainid(self.ticker_symbol)

    def market_data(self, option_id=None):
        if option_id is None:
            return self.rh.get_option_marketdata(self.ticker_symbol)
        else:
            return self.rh.get_option_market_data(option_id)

    def popularity(self):
        return self.rh.get_popularity(self.ticker_symbol)

    def last_trade_price(self):
        trade_price_string = self.rh.last_trade_price(self.ticker_symbol)
        return trade_price_string[0][0]

    def last_updated_at(self):
        updated_at_string = self.rh.last_updated_at(self.ticker_symbol)
        return updated_at_string[0][0]

    def previous_close(self, adjusted=False):
        date_string = self.rh.previous_close_date(self.ticker_symbol)
        date = date_string[0][0]
        if adjusted:
            price_string = self.rh.previous_close(self.ticker_symbol)
            price = price_string[0][0]
            return price, date
        else:
            price_string = self.rh.adjusted_previous_close(self.ticker_symbol)
            price = price_string[0][0]
            return price, date


# unit testing
if __name__ == "__main__":
    creds = open("credentials").readlines()
    email = creds[0].strip()
    password = creds[1].strip()
    begin_robinhood_session(email, password)
    amazon_stock = Instrument(Instrument.Type.STOCK, "AMZN")
    print("Amazon stock " + str(amazon_stock))
    print("Amazon stock symbol: " + str(amazon_stock.symbol()))
    print("Quote for Amazon stock: " + str(amazon_stock.quote()))
    print("Ask price x size: " + str(amazon_stock.ask_info()))
    print(("Bid price x size: " + str(amazon_stock.bid_info())))
    # print("Fundamental: " + str(amazon_stock.fundamental()))
    # print("Historical data for Amazon: " + str(amazon_stock.historical_quotes()))
    # print("News: " + str(amazon_stock.news()))
    # print("Option chain ID: " + str(amazon_stock.option_chain()))
    # print("Market data for Amazon: " + str(amazon_stock.market_data()))
    # print("Popularity of Amazon stock as measured by number of Robinhood users who own it: "
    #       + str(amazon_stock.popularity()))
    print("Last trade price of Amazon stock: " + str(amazon_stock.last_trade_price()))
    print("Price for Amazon stock last updated at: " + str(amazon_stock.last_updated_at()))
    print("Previous closing price for Amazon stock, not adjusted: " + str(amazon_stock.previous_close()))
    print("Previous closing price for Amazon stock, adjusted: " + str(amazon_stock.previous_close(adjusted=True)))
    end_robinhood_session()
