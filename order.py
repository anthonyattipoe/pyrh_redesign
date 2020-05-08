from enum import Enum

from exceptions import OrderCancellationError, MalformedOrderError, UnownedInstrumentError
from instrument import Instrument
from portfolio import Portfolio
import __init__

class OrderStatus(object):
    """The status of an order."""
    
    def __init__(self, order_response=None):
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

    def __init__(self, instrument: Instrument, order_type: Type, quantity: int,
                time_in_force: TimeInForce = TimeInForce.GFD, price: float = None, stop_price: float = None):
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
        self.order_type = order_type
        self.time_in_force = time_in_force
        self.quantity = quantity
        self.price = price
        self.stop_price = stop_price
        self.id = None
        self.status = OrderStatus()
        self.rh = __init__.session_token.rh

    def __str__(self) -> str:
        """Custom pretty print function for an Order"""
        pass

    def _validate(self) -> None:
        """Validates the properties set on an order before it is placed.

        Raises:
            MalformedOrderError: If the combinations of properties set on the order are not compatible.
        """
        if self.quantity <= 0:
            raise MalformedOrderError('The quantity must be greater than or equal to 1.')
            
        if self.price and self.price < 0:
            raise MalformedOrderError('The price must be greater than or equal to 0.')

        if self.stop_price and self.stop_price < 0:
            raise MalformedOrderError('The stop price must be greater than or equal to 0.')

        if (self.order_type in [Order.Type.STOP_LIMIT_BUY_ORDER, Order.Type.STOP_LIMIT_SELL_ORDER, 
            Order.Type.STOP_LOSS_BUY_ORDER,Order.Type.STOP_LOSS_SELL_ORDER] and self.stop_price == None):
            raise MalformedOrderError('You must include a stop_price with the current order.')

        if self.order_type in [Order.Type.STOP_LIMIT_BUY_ORDER, Order.Type.STOP_LIMIT_SELL_ORDER] and self.price == None:
            raise MalformedOrderError('You must include a price with the current order.')

        if (self.order_type in [Order.Type.SELL, Order.Type.LIMIT_SELL_ORDER, Order.Type.MARKET_SELL_ORDER, 
            Order.Type.STOP_LIMIT_SELL_ORDER, Order.Type.STOP_LOSS_SELL_ORDER]):
            if not Portfolio().contains_instrument(self.instrument):
                raise UnownedInstrumentError(self.instrument.ticker_symbol)


    def place(self) -> OrderStatus:
        """Place the current order. Calls validate() before the order is placed.
        This method is idempotent so calling place() after the order has already
        placed will have no effect.

        Returns:
            An OrderStatus object outlining the status of the current order.

        Raises:
            MalformedOrderError: If the combinations of properties set on the order are not compatible.
        """
        self._validate()
        response = None

        time_in_force = "GTC" if self.time_in_force == Order.TimeInForce.GTC else "GFD"

        if self.order_type == Order.Type.BUY:
            response = self.rh.place_buy_order(self.instrument.order_object(), self.quantity, self.price)
        elif self.order_type == Order.Type.SELL:
            response = self.rh.place_sell_order(self.instrument.order_object(), self.quantity, self.price)
        elif self.order_type == Order.Type.LIMIT_BUY_ORDER:
            response = self.rh.place_limit_buy_order(self.instrument.url, self.instrument.ticker_symbol, time_in_force, self.price, self.quantity)
        elif self.order_type == Order.Type.LIMIT_SELL_ORDER:
            response = self.rh.place_limit_sell_order(self.instrument.url, self.instrument.ticker_symbol, time_in_force, self.price, self.quantity)
        elif self.order_type == Order.Type.MARKET_BUY_ORDER:
            response = self.rh.place_market_buy_order(self.instrument.url, self.instrument.ticker_symbol, time_in_force, self.quantity)
        elif self.order_type == Order.Type.MARKET_SELL_ORDER:
            response = self.rh.place_market_sell_order(self.instrument.url, self.instrument.ticker_symbol, time_in_force, self.quantity)
        elif self.order_type == Order.Type.STOP_LIMIT_BUY_ORDER:
            response = self.rh.place_stop_limit_buy_order(self.instrument.url, self.instrument.ticker_symbol, time_in_force, self.price, self.stop_price, self.quantity)
        elif self.order_type == Order.Type.STOP_LIMIT_SELL_ORDER:
            response = self.rh.place_stop_limit_sell_order(self.instrument.url, self.instrument.ticker_symbol, time_in_force, self.price, self.stop_price, self.quantity)
        elif self.order_type == Order.Type.STOP_LOSS_BUY_ORDER:
            response = self.rh.place_stop_loss_buy_order(self.instrument.url, self.instrument.ticker_symbol, time_in_force, self.stop_price, self.quantity)
        elif self.order_type == Order.Type.STOP_LOSS_SELL_ORDER:
            response = self.rh.place_stop_loss_sell_order(self.instrument.url, self.instrument.ticker_symbol, time_in_force, self.stop_price, self.quantity)
        
        return response
        # self.status = OrderStatus(response)
        # return self.status


    def cancel(self) -> None:
        """Cancels the current order after it has been placed but not yet executed.

        Raises:
            OrderCancellationError: If order has already been executed or terminated.
        """
        # if self.status.is_executed() or self.status.is_terminated():
            # raise OrderCancellationError(self)
        # if self.status.is_placed() and self.status.is_pending():
            # self.rh.canel_order(order_id)
            # self.status = CANCELED
        pass


    def status(self) -> OrderStatus:
        """Returns the status of the current order."""
        return self.status
