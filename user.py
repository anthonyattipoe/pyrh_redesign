from portfolio import Portfolio
import __init__


class User:
    """An existing Robinhood User."""

    def __init__(self):
        """Creates a new object which is used to access the current Users portfolio and orders.

                Returns:
                    An user object.
        """

        self.rh = __init__.session_token.rh
        self.portfolio = Portfolio()


    def order_history(self, orderId=None):
        """Wrapper for portfolios
        Optional Args: add an order ID to retrieve information about a single order.
        Returns:
            (:obj:`dict`): JSON dict from getting orders
        """
        
        return self.rh.order_history(orderId)
        

    def get_open_orders(self):
        """Returns all currently open (cancellable) orders.
        If not orders are currently open, `None` is returned.
        TODO: Is there a way to get these from the API endpoint without stepping through
            order history?
        """

        return self.rh.get_open_orders()

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