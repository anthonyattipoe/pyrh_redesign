from pyrh.pyrh import urls
from pyrh.pyrh.models import PortfolioSchema
from session import begin_robinhood_session, end_robinhood_session

class User:
    """An existing Robinhood User."""

    def __init__(self):
        """ Returns an existing Robinhood User."""
        self.rh = __init__.session_token.rh
        self.portfolio = Portfolio()
        self.name = self.rh.User()

    def _str_(self):
        """Prints User Data In the Form:
            User: Name
            Portfolio: Portfolio            
        """
        return 'User(name='+self.name+', portfolio='+str(self.portfolio) + ')'

    def portfolio(self):
        """Returns the user's portfolio."""
        return self.portfolio

    def order_history(self, orderId):
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



###### CLIENT CODE ######
if __name__ == "__main__":
    begin_robinhood_session("", "")
    user = User()
    print("Testing: __str__()")
    print(str(user))

    print("Testing: portfolio()")
    portfolio = user.portfolio()
    print(str(portfolio))

    print("Testing: order_history()")
    print(user.order_history())

    print("Testing: get_open_orders()")
    print(user.get_open_orders())
    end_robinhood_session()