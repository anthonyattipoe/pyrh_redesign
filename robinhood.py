from enum import Enum

###########################
#      Instruments
###########################

class Instrument(object):
    """A tradeable instrument on the Robinhood platform."""

    class Type(Enum):
        """The type of instrument in question."""
        STOCK  = 1
        BOND   = 2
        ETF    = 3
        CRYPTO = 4

    def __init__(self, type: Instrument.Type, symbol: str) -> Instrument:
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

##########################
#         Order
##########################

class OrderStatus(object):
    # TODO: Should this inherently be some type of promise
    # Perhaps return info immediately if trade occurs immediately or 
    # return an ID which can be used to fetch info if trade is async.
    """The status of an order."""
    pass

class Order(object):
    """An order which a user can place."""

    class Type(Enum):
        """The type of an order."""
        BUY                   = 1
        SELL                  = 2
        LIMIT_BUY_ORDER       = 3
        LIMIT_SELL_ORDER      = 4
        MARKET_BUY_ORDER      = 5
        MARKET_SELL_ORDER     = 6
        STOP_LIMIT_BUY_ORDER  = 7
        STOP_LIMIT_SELL_ORDER = 8
        STOP_LOSS_BUY_ORDER   = 9
        STOP_LOSS_SELL_ORDER  = 10
    
    class TimeInForce(Enum):
        """The time in force of an order. 
        This specifies how long an order lasts until it is executed or expires.
        """
        GFD = 1
        GTC = 2

    def __init__(self, instrument: Instrument, type: Order.Type, time_in_force: Order.TimeInForce,
                quantity: int = None, price: float = None) -> Order:
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

    def validate(self) -> None:
        """Validates the properties set on an order before it is placed.
        
        Raises:
            MalformedOrderError: If the combinations of properties set on the order are not compatible.
        """
        pass

    def place(self) -> OrderStatus:
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
#   User & Portfolio
##########################

class Portfolio(object):
    """A user's current portfolio of instruments they own."""
    pass


class User(object):
    """An existing Robinhood User."""
    
    def __init__(self, email: str, password: str) -> User:
        """Logs in an existing Robinhood user with the provided credentials.

        Args:
            email: the email used to register the Robinhood account.
            password: the password used to authenticate the user's account.

        Returns:
            A new Robinhood user object.
        
        Raises:
            InvalidLoginCredentialsError: If user credentials are invalid.
        """
        pass

    def portfolio(self) -> Portfolio:
        """Returns the portfolio of the current user."""
        pass
