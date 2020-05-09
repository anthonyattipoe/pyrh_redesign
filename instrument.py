"""
    The following class, Instrument, is used to represent a tradable instrument on the Robinhood platform.
"""

from enum import Enum
from decimal import *
from typing import Tuple
import __init__


class Instrument:
    """A tradeable instrument on the Robinhood platform."""

    class Type(Enum):
        """The type of instrument in question."""
        STOCK  = 1
        BOND   = 2
        ETF    = 3
        CRYPTO = 4

    def __init__(self, instrument_type, symbol):
        """Creates a new object which can be used to track
        updates about an instrument or be included in an order.

        Args:
            instrument_type: an enum delineating the type of instrument.
            symbol: the symbol corresponding with the desired instrument.

        Returns:
            An Instrument object.

        Raises:
            MalformedInstrumentError: If an invalid combination of symbol and instrument type is provided.
        """
        self.instrument_type = instrument_type
        self.ticker_symbol = symbol
        self.rh = __init__.session_token.rh

        self.url = self.quote()["instrument"]

    def __str__(self):
        """ Prints the Instruments ticket symbol"""
        return self.ticker_symbol

    def symbol(self):
        """ Returns the Instrument's ticket symbol"""
        return self.ticker_symbol

    def quote(self) -> dict:
        """ Returns the current market quote of the Instrument."""
        return self.rh.quote_data(self.ticker_symbol)

    def order_object(self) -> dict:
        """ Returns the users URL and the Instrument's ticket symbol"""
        return {
            'url': self.url,
            'symbol': self.ticker_symbol
        } 

    def ask_info(self) -> Tuple[Decimal, int]:
        """ The ask price and ask size of a given instrument
        
        Returns:
            Tuple: (ask_price, ask_size)
        """
        price_string = self.rh.ask_price(self.ticker_symbol)
        price = float(price_string[0][0])
        size_string = self.rh.ask_size(self.ticker_symbol)
        size = float(size_string[0][0])
        return round(Decimal(price), 4), size

    def bid_info(self) -> Tuple[Decimal, int]:
        """ The bid price and bid size of a given instrument
        
        Returns:
            Tuple: (bid_price, bid_size)
        """
        price_string = self.rh.bid_price(self.ticker_symbol)
        price = float(price_string[0][0])
        size_string = self.rh.bid_size(self.ticker_symbol)
        size = float(size_string[0][0])
        return round(Decimal(price), 4), size

    def fundamental(self) -> dict:
        """ Fundamental analysis of an instrument
        
        Returns:
            dict: (ask_price, ask_size)
            example:
                {
                 'open': '158.310000', 
                 'high': '160.170000', 
                 'low': '155.260000', 
                 'volume': '4275536.000000', 
                 'average_volume_2_weeks': '6414987.900000', 
                 'average_volume': '6414987.900000', 
                 'high_52_weeks': '195.720000', 
                 'dividend_yield': None, 
                 'float': '859278760.000000', 
                 'low_52_weeks': '115.290000', 
                 'market_cap': '139951150000.000000', 
                 'pb_ratio': '4.120950', 
                 'pe_ratio': '1055.130000', 
                 'shares_outstanding': '895000000.000000', 
                 'description': 'salesforce.com, inc. engages in the ... blah blah blah', 
                 'instrument': 'https://api.robinhood.com/instruments/cf1d849d-06f7-4374-9e84-13129713d0c7/', 
                 'ceo': 'Marc Russell Benioff', 
                 'headquarters_city': 'San Francisco', 
                 'headquarters_state': 'California', 
                 'sector': 'Technology Services', 
                 'industry': 'Packaged Software', 
                 'num_employees': 49000, 'year_founded': 1999
                 }
        """
        return self.rh.get_fundamentals(self.ticker_symbol)

    def historical_quotes(self, interval, span) -> list:
        """ The historical data of a given instrument
        
        Returns:
            Tuple: (ask_price, ask_size)
        """
        historical_data_raw = self.rh.get_historical_quotes(self.ticker_symbol, interval, span)
        historical_data = historical_data_raw['results'][0]['historicals']
        return historical_data

    def news(self) -> dict:
        """ News relating to the given instrument
        
        Returns:
            dict: 
                important keys:
                    count: number of new items in results
                    results: list of dict that have information regarding the intstrument
        """
        return self.rh.get_news(self.ticker_symbol)

    def option_chain_id(self):
        return self.rh.get_option_chainid(self.ticker_symbol)

    def market_data(self) -> dict:
        """ The market_data of a given instrument
        
        Returns:
            dict:
                important keys:
                    rests: list of dict that have information regarding instrument
        """
        return self.rh.get_option_marketdata()

    def popularity(self) -> dict:
        """ How many users currently have this instrument
        
        Returns:
            int: the number of users
        """
        return int(self.rh.get_popularity(self.ticker_symbol))

    def last_trade_price(self) -> Decimal:
        """ The last trading price for the given instrument
        
        Returns:
            Decimal value: trading price
        """
        trade_price_string = self.rh.last_trade_price(self.ticker_symbol)
        return round(Decimal(trade_price_string[0][0]), 4)

    def last_updated_at(self) -> str:
        """ The last updated date for the given instrument
        
        Returns:
            str: date in form 'YYYY-MM-DD'
        """
        updated_at_string = self.rh.last_updated_at(self.ticker_symbol)
        return updated_at_string[0][0]

    def previous_close(self, adjusted=False) -> Tuple[Decimal, int]:
        """ The price and date of the given instrument for the previous close
        
        Returns:
            tuple: (price: Decimal, date: str)
        """
        date_string = self.rh.previous_close_date(self.ticker_symbol)
        date = date_string[0][0]
        if adjusted:
            price_string = self.rh.previous_close(self.ticker_symbol)
            price = round(Decimal(price_string[0][0]),4)
            return price, date
        else:
            price_string = self.rh.adjusted_previous_close(self.ticker_symbol)
            price = round(Decimal(price_string[0][0]),4)
            return price, date
