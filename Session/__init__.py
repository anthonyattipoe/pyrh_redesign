from __future__ import annotations
from pyrh import Robinhood


class RobinHood(object):
    """ Robinhood superclass  """

    rh = Robinhood()

    def __init__(self, email, password):
        """Logs in an existing Robinhood user with the provided credentials.
        Args:
            email: the email used to register the Robinhood account.
            password: the password used to authenticate the user's account.
        Returns:
            A new Robinhood object.
        Raises:
            InvalidLoginCredentialsError: If user credentials are invalid.
        """
        self.rh.login(email, password)

    def reauthorize(self, email, password):
        """ reauthorize Robinhood session using the Robinhood User credentials
            method called in case of session expiriy
        """
        self.rh.login(email, password)

    def end_session(self):
        """ logout of Robinhood session"""
        self.rh.logout()


Session = None

def beginRobinhoodSession(email, password):
	Session =  RobinHood(email, password)

def endRobinhoodSession():
	Session.end_session()
	Session = None
