"""
    The following class, Portoflio, is used to represent an existing Robinhod user's portfolio.  The portfolio comprises
    of the instrument the user owns along with securities and positions.
"""

from enum import Enum
from instrument import Instrument
import __init__


class Portfolio:
    """ An existing Robinhood User's Portfolio."""
    
    class ValueType(Enum):
        """ The way to calculate the value of a user's holdings """
        EQUITY       = 1
        MARKET_VALUE = 2

    def __init__(self):
        """ Creates a new Portfolio object."""
        self.rh = __init__.session_token.rh 

    def __str__(self) -> str:
        """Prints contents of Portfolio"""
        portfolio = self.rh.portfolio()
        attr = vars(portfolio)
        string = "Portfolio \n"
        for item in attr:
            string = string + "{}: {}\n".format(item, str(attr[item])) 
        return string

    def value(self, value_type: ValueType) -> float:
        """Returns portfolio equity or market value.
        
        Args:
            value_type: the value type {EQUITY or MARKET_VALUE}

        Returns:
            Float representing the value.
        """
        if value_type == Portfolio.ValueType.EQUITY:
            return self.rh.equity()
        else:
            return self.rh.market_value()
        
    def contains_instrument(self, instrument: Instrument, quantity: float = 0.0):
        """Determines of current portfolio contains the given instrument."""
        for position in self.positions():
            if position['symbol'] == instrument.ticker_symbol and position['shares_held_for_sells'] >= quantity:
                return True
        return False

    def excess_margin(self) -> float:
        """Returns the excess margin portfolio"""
        return self.rh.excess_margin()

    def extended_hours_value(self, value_type: ValueType) -> float:
        """ Returns portfolio extended_hours equity or market value.
        
            Args:
                value_type: the value type {EQUITY or MARKET_VALUE}
        """
        if value_type == Portfolio.ValueType.EQUITY:
            return self.rh.extended_hours_equity()
        else:
            return self.rh.extended_hours_market_value()

    def equity_previous_close(self, adjusted: bool = False) -> float:
        """ Returns portfolio equity_previous_close

            Args:
                adjusted: flag to determine standard or adjusted previous_close
        """
        if adjusted:
            return self.rh.adjusted_equity_previous_close()
        else:
            return self.rh.equity_previous_close()

    def last_core_value(self, value_type) -> float:
        """ Returns portfolio last core value
        
            Args:
                value_type: the value type {EQUITY or MARKET_VALUE}
        """
        if value_type == Portfolio.ValueType.EQUITY:
            return self.rh.last_core_equity()
        else:
            return self.rh.last_core_market_value()

    def dividends(self) -> list:
        """Returns the dividends for a portfolio

        Returns:
            List of dividends, where each dividend represented by single dict

            example dividend: { 'id': ID_NUMBER_AS_STR,
                                'url': URL_AS_STR,
                                'account': ACCOUNT_URL_AS_STR,
                                'instrument': INSTRUMENT_URL_AS_STR,
                                'amount': '0.36',
                                'rate': '0.1200000000',
                                'position': '3.00000000',
                                'withholding': '0.00',
                                'record_date': '2020-03-05',
                                'payable_date': '2020-03-16',
                                'paid_at': '2020-03-17T02:14:50Z',
                                'state': 'paid',
                                'nra_withholding': None,
                                'drip_enabled': False
                               }
        """

        return self.rh.dividends()["results"]


    def positions(self, previously_held=False) -> list:
        """Returns the positions for a user's portfolio
        
        Args:
            previously_held: bool. include positions where the user has 0 quantity

        Returns:
            dict representation of a position

            example position: {  'url': 'https://api.robinhood.com/positions/ACCOUNT_NUMBER/ID_NUMBER/', 
                                 'instrument': 'https://api.robinhood.com/instruments/ID_NUMBER/', 
                                 'account': 'https://api.robinhood.com/accounts/ACCOUNT_NUMBER/', 
                                 'account_number': 'ACCOUNT_NUMBER', 
                                 'average_buy_price': PRICE_STR_FLT, 
                                 'pending_average_buy_price': PRICE_STR_FLT, 
                                 'quantity': QUANTITY_STR_FLT, 
                                 'intraday_average_buy_price': '0.0000', 
                                 'intraday_quantity': '0.00000000', 
                                 'shares_held_for_buys': '0.00000000', 
                                 'shares_held_for_sells': '2.00000000', 
                                 'shares_held_for_stock_grants': '0.00000000', 
                                 'shares_held_for_options_collateral': '0.00000000', 
                                 'shares_held_for_options_events': '0.00000000', 
                                 'shares_pending_from_options_events': '0.00000000', 
                                 'updated_at': '2020-05-02T20:11:41.491656Z', 
                                 'created_at': '2019-07-31T23:57:07.494746Z',
                                 'symbol': "GOOG"
                             }
        """
        positions = self.rh.positions()["results"]
        mod_positions = []
        for position in positions:
            if (float(position["quantity"]) == 0 and not previously_held):
                continue
            symbol = self.rh.get(position["instrument"])["symbol"]
            position["symbol"] = symbol
            mod_positions += [position]
        return mod_positions


