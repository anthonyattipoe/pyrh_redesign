from enum import Enum
from pyrh import Robinhood


class Order:
    """An order which a user can place."""

    rh = Robinhood()

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
                 quantity: int = None, price: float = None):
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

    def __str__(self) -> str:
        """Custom pretty print function for an Order"""
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

        Returns:
            An OrderStatus object outlining the status of the current order.

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
