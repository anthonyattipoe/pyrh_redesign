from pyrh.pyrh import urls
from pyrh.pyrh.models import PortfolioSchema

class User:
    """An existing Robinhood User."""
    
    def __init__(self):
        """ Returns an existing Robinhood User."""
        self.portfolio = self.get(urls.PORTFOLIOS, schema=PortfolioSchema())
        self.name = self.get(urls.USER)
       

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

        return self.get(urls.build_orders(orderId))
        

    def get_open_orders(self):
        """Returns all currently open (cancellable) orders.
        If not orders are currently open, `None` is returned.
        TODO: Is there a way to get these from the API endpoint without stepping through
            order history?
        """

        open_orders = []
        orders = self.order_history()
        for order in orders["results"]:
            if order["cancel"] is not None:
                open_orders.append(order)

        return open_orders
