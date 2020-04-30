from enum import Enum


###########################
#      Instruments
###########################

class Instrument(object):
    """TODO"""

    class Type(Enum):
        """TODO"""
        STOCK = 1
        BOND  = 2
        ETF   = 3

    def __init__(self, type=Instrument.Type.STOCK):
        """TODO"""
        pass

##########################
#         Order
##########################

class Order(object):
    """TODO"""

    class Action(Enum):
        """TODO"""
        BUY  = 1
        SELL = 2
    
    def __init__(self, instrument=None, action=Order.Action.BUY):
        """TODO"""
        pass

    def place(self):
        """TODO"""
        pass
    

##########################
#   User & Portfolio
##########################

class Portfolio(object):
    """TODO"""
    pass


class User(object):
    """TODO"""
    def __init__(self, username, password):
        """TODO"""
        self.portfolio = Portfolio()



