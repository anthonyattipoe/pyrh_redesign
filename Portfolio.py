from enum import Enum
from .Session import Session


class Portfolio:
    """A user's current portfolio of instruments they own.
       Includes info on securities and positions
    """

    all_instruments = None  # each instrument is mapped to number of shares in this portfolio
    rh = None

    class ValueType(Enum):
        """ The way to calculate the value of a user's holdings """
        EQUITY = 1
        MARKET_VALUE = 2

    def __init__(self):
        self.all_instruments = {}
        self.rh = Session

    def _str_(self):
        """Custom pretty print function for a Portfolio"""


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