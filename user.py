from pyrh.pyrh import urls
from pyrh.pyrh.models import PortfolioSchema
from session import begin_robinhood_session, end_robinhood_session

class User:
    """An existing Robinhood User."""

    def __init__(self):
        """ Returns an existing Robinhood User."""
        self.rh = __init__.session_token.rh
        self.portfolio = self.rh.Portfolio()
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