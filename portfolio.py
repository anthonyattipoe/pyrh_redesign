from enum import Enum
from Session import begin_robinhood_session, end_robinhood_session
import __init__


class Portfolio:
    """A user's current portfolio of instruments they own.
       Includes info on securities and positions
    """
    
    class ValueType(Enum):
        """ The way to calculate the value of a user's holdings """
        EQUITY = 1
        MARKET_VALUE = 2

    def __init__(self):
        self.rh = __init__.session_token.rh

    def _str_(self) -> str:
        """Custom pretty print function for a Portfolio"""


    def value(self, value_type : ValueType) -> float:
        """Returns portfolio equity or market value.
        
        Args:
            value_type: the value type {EQUITY or MARKET_VALUE}

        Returns:
            Float representing the value.
        """
        if value_type == ValueType.EQUITY: 
            return self.rh.equity()
        else:
            return self.rh.market_value()


    def excess_margin(self) -> float:
        """Returns the excess margin portfolio
        
        Args:
            None 

        Returns:
            Float representing value
        """
        return rh.excess_margin()

    def extended_hours_value(self, value_type : ValueType) -> float:
        """Returns portfolio extended_hours equity or market value.
        
        Args:
            value_type: the value type {EQUITY or MARKET_VALUE}

        Returns:
            Float representing the value.
        """
        if value_type == ValueType.EQUITY: 
            return self.rh.extended_hours_equity()
        else:
            return self.rh.extended_hours_market_value()

    def equity_previous_close(self, adjusted : bool = False) -> float:
        """Returns portfolio equity_previous_close
        
        Args:
            adjusted: flag to determine standard or adjusted previous_close 

        Returns:
            Float representing the value.
        """
        if adjusted:
            return rh.adjusted_equity_previous_close()
        else:
            return rh.equity_previous_close()

    def last_core_value(self, value_type) -> float:
        """Returns portfolio last core value
        
        Args:
            value_type: the value type {EQUITY or MARKET_VALUE}

        Returns:
            Float representing the value.
        """
        if value_type == ValueType.EQUITY: 
            return self.rh.last_core_equity()
        else:
            return self.rh.last_core_market_value()

    def dividends(self) -> list(dict):
        """Returns the dividends for a portfolio
        
        Args:
            None 

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

        json = rh.dividends()
        # TODO: convert json to map
        pass


    def investment_profile(self) -> dict:
        """Returns the investment profile for a users portfolio
        
        Args:
            None 

        Returns:
            dict represnation of investment profile 

            example  'user': 'api.robinhood.com/user/', 
                     'total_net_worth': RANGE_RANGE_STR, 
                     'annual_income': RANGE_RANGE_STR, 
                     'source_of_funds': STR, 
                     'investment_objective': 'income_invest_obj', 
                     'investment_experience': STR, 
                     'liquid_net_worth': RANGE_RANGE_STR, 
                     'risk_tolerance': STR, 
                     'tax_bracket': '', 
                     'time_horizon': STR, 
                     'liquidity_needs': STR, 
                     'investment_experience_collected': BOOL, 
                     'suitability_verified': BOOL, 
                     'option_trading_experience': '', 
                     'professional_trader': None, 
                     'understand_option_spreads': BOOL, 
                     'interested_in_options': None, 
                     'updated_at': '2019-08-01T16:18:26.996458Z'
        """

        return self.rh.investment_profile()


    def positions(self) -> dict:
        """Returns the positions for a user's portfolio
        
        Args:
            None 

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
                                 'created_at': '2019-07-31T23:57:07.494746Z'
                             }
        """
        json = self.rh.positions() 
        # TODO: convert json to map

        pass

        
