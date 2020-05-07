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
                 quantity: int = None, price: float = None, stop_price: float = None):
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
        self.instrument = instrument
        self.type = type
        self.time_in_force = time_in_force
        self.quantity = quantity
        self.price = price
        self.stop_price = stop_price
        self.id = None

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

        switch (self.type) {
            case BUY:  
                    self.rh.place_buy_order(self.instrument.url, self.quantity, self.price) 
                    break;
            case SELL:  
                    self.rh.place_sell_order(self.instrument.url, self.quantity, self.price) 
                    break;
            case LIMIT_BUY_ORDER:  
                    self.rh.place_limit_buy_order(self.instrument.url, self.symbol, self.time_in_force, self.price, self.quantity) 
                    break;
            case LIMIT_SELL_ORDER:  
                    self.rh.place_limit_sell_order(self.instrument.url, self.symbol, self.time_in_force, self.price, self.quantity) 
                    break;
            case MARKET_BUY_ORDER:  
                    self.rh.place_market_buy_order(self.instrument.url, self.symbol, self.time_in_force, self.quantity) 
                    break;
            case MARKET_SELL_ORDER:  
                    self.rh.place_market_sell_order(self.instrument.url, self.symbol, self.time_in_force, self.quantity) 
                    break;
            case STOP_LIMIT_BUY_ORDER:  
                    self.rh.place_stop_limit_buy_order(self.instrument.url, self.symbol, self.time_in_force, self.price, self.stop_price, self.quantity) 
                    break;
            case STOP_LIMIT_SELL_ORDER:  
                    self.rh.place_stop_limit_sell_order(self.instrument.url, self.symbol, self.time_in_force, self.price, self.stop_price, self.quantity) 
                    break;
            case STOP_LOSS_BUY_ORDER:  
                    self.rh.place_stop_loss_buy_order(self.instrument.url, self.symbol, self.time_in_force, self.stop_price, self.quantity) 
                    break;
            case STOP_LOSS_SELL_ORDER: 
                    self.rh.place_stop_loss_sell_order(self.instrument.url, self.symbol, self.time_in_force, self.stop_price, self.quantity) 
                    break;
            default: 
                    raise(MalformedOrderError)
        }

    def cancel(self) -> None:
        """Cancels the current order after it has been placed but not yet executed.

        Raises:
            OrderCancellationError: If order has already been executed or terminated.
        """
        self.rh.canel_order(order_id)
        pass

    # TODO
    def status(self) -> OrderStatus:
        """Returns the status of the current order."""
        pass
