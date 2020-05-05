class User:
    """An existing Robinhood User."""
    def __init__(self):
        pass

    def _str_(self):
        """Custom pretty print function for a User"""
        pass

    def portfolio(self):
        """Returns the portfolio of the current user."""
        """Consolidated portfolio() and options_owned() and investment_profile """

    def order_history(self) -> List(Order): #return type?
        pass

    def get_open_orders(self) -> List(OrderStatus):
        """return all currently open(cancellabe) orders"""
        pass