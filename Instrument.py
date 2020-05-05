from enum import Enum
from pyrh import Robinhood


class Instrument:
    """A tradeable instrument on the Robinhood platform."""

    instrument_type = None
    ticker_symbol = None
    rh = Robinhood()

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

    def _str_(self):
        """Custom pretty print function for an Instrument"""
        """prints instrument data"""
        return "{self.name}: {self.instrument_type}"

    def symbol(self):
        return self.ticker_symbol

    def quote(self):
        return self.rh.quote_data(self.ticker_symbol)

    def ask_info(self):
        price = self.rh.ask_price(self.ticker_symbol)
        size = self.rh.ask_size(self.ticker_symbol)
        return price, size

    def bid_info(self):
        price = self.rh.bid_price(self.ticker_symbol)
        size = self.rh.bid_size(self.ticker_symbol)
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
        return self.rh.last_trade_price(self.ticker_symbol)

    def last_updated_at(self):
        return self.rh.last_updated_at(self.ticker_symbol)

    def previous_close(self, adjusted=False):
        date = self.rh.previous_close_date(self.ticker_symbol)
        if adjusted:
            price = self.rh.previous_close(self.ticker_symbol)
            return price, date
        else:
            price = self.rh.adjusted_previous_close(self.ticker_symbol)
            return price, date

    @staticmethod
    def search(name) -> List(Instrument):
        pass