from __future__ import annotations
from enum import Enum

###########################
#  Robinhood 
###########################


class Robinhood(object):
    """ Robinhood superclass  """


    def __init__(self, email: str, password: str):
    """Logs in an existing Robinhood user with the provided credentials.

    Args:
        email: the email used to register the Robinhood account.
        password: the password used to authenticate the user's account.

    Returns:
        A new Robinhood object.
    
    Raises:
        InvalidLoginCredentialsError: If user credentials are invalid.
    """
        # authenticated = [true/false]
        pass


    def reauthorize():
        """ reauthorize Robinhood session using the Robinhood User credentials
            method called in case of session expiriy
        """
        pass

    def end_session():
        """ logout of Robinhood session"""
        pass




###########################
#      Instruments
###########################

class Instrument(Robinhood):
    """A tradeable instrument on the Robinhood platform."""

    class Type(Enum):
        """The type of instrument in question."""
        STOCK  = 1
        BOND   = 2
        ETF    = 3
        CRYPTO = 4

    def __init__(self, type: Instrument.Type, symbol: str):
        """Creates a new object which can be used to track
        updates about an instrument or be included in an order.

        Args:
            type: an enum delineating the type of instrument.
            symbol: the symbol corresponding with the desired instrument.
        
        Returns:
            An instrument object.

        Raises:
            MalformedInstrumentError: If an invalid combination of symbol and instrument type is provided.
        """
        pass

    def _str_(self):
        """Custom pretty print function for an Instrument"""
        """prints instrument data"""
        pass

    def symbol(self):
        pass

    def quote(self):
        pass

    def ask_info(self):
        # returns (price, size)
        pass

    def bid_info(self):
        # returns (price, size)
        pass

    def fundamental(self):
        pass

    def historical_quotes(self):
        pass

    def newsself(self):
        pass

    def chain_id(self):
        pass

    def market_data(self):
        pass

    def popularity(self):
        pass

    def tickers(self):
        pass

    def last_trade_price(self):
        pass

    def last_updated_at(self):
        pass

    def previous_close(self, adjusted=False):
        # return (price, date)
        pass

    @staticmethod
    def search(name) -> List(Instrument):
        pass



##########################
#         Order
##########################

class OrderStatus():
    # TODO: Should this inherently be some type of promise
    # Perhaps return info immediately if trade occurs immediately or 
    # return an ID which can be used to fetch info if trade is async.
    """The status of an order."""
    def __init__(self):
        pass

    def _str_(self):
        """Custom pretty print function for an Order status"""
        pass

class Order(Robinhood):
    """An order which a user can place."""

    class Type(Enum):
        """The type of an order."""
        BUY                   = 1
        SELL                  = 2
    
    class TimeInForce(Enum):
        """The time in force of an order. 
        This specifies how long an order lasts until it is executed or expires.
        """
        GFD = 1
        GTC = 2

    def __init__(self, instrument: Instrument, type: Order.Type, time_in_force: Order.TimeInForce,
                quantity: int = None, price: float = None) :
        """Creates a new order.
        
        Args:
            instrument: the instrument tied to the prospective order a user creates.
            type: an enum used to represent the type of order the user will like to place.
            time_in_force: how long an order lasts before it is executed or expires.
            quantity: a discrete number of instruments included in the current order.
            price: a price amount corresponding to the instrument included in the current order.
        
        Returns:
            a new Order object.
        """
        pass

    def _str_(self):
        """Custom pretty print function for an Order"""
        pass


    def validate(self) -> None:
        """Validates the properties set on an order before it is placed.
        
        Raises:
            MalformedOrderError: If the combinations of properties set on the order are not compatible.
        """
        pass

    def place(self, limit=None, stop=None) -> OrderStatus:
        """Place the current order. Calls validate() before the order is placed.
        This method is idempotent so calling place() after the order has already
        placed will have no effect.
        
        Raises:
            MalformedOrderError: If the combinations of properties set on the order are not compatible.
        """
        pass

    def cancel(self) -> None:
        """Cancels the current order after it has been placed but not yet executed.
        
        Raises:
            OrderCancellationError: If order has already been executed or terminated.
        """
        pass

    def status(self) -> OrderStatus:
        """Returns the status of the current order."""
        pass


##########################
#   User , Portfolio, Positions
##########################

class User(Robinhood):
    """An existing Robinhood User."""
    def __init__(self):
        pass

    def _str_(self):
        """Custom pretty print function for a User"""
        pass

    def portfolio(self) -> Portfolio:
        """Returns the portfolio of the current user."""
        """Consolidated portfolio() and options_owned() and investment_profile """

    def order_history(self) -> List(Order): #return type? 
        pass

    def get_open_orders(self) -> List(OrderStatus):
        """return all currently open(cancellabe) orders"""
        pass

class Portfolio():
    """A user's current portfolio of instruments they own.
       Includes info on securities and positions
    """

    class ValueType(Enum):
        """ The way to calculate the value of a user's holdings """
        EQUITY = 1
        MARKET_VALUE = 2

    def __init__(self):
        pass

    def _str_(self):
        """Custom pretty print function for a Portfolio"""
        pass

    def value(self, value_type):
        # value_type is of Portfolio.ValueType
        pass

    def dividends(self):
        pass

    def excess_margin(self):
        pass

    def extended_hours_value(self, value_type):
        # value_type is of Portfolio.ValueType
        pass

    def equity_previous_close(self, adjusted=False):
        pass

    def last_core_value(self, value_type):
        # value_type is of Portfolio.ValueType
        pass

