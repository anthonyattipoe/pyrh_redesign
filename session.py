"""
    The following class, RobinHood_Object, allowing users to being and end Robinhood sessions.
"""

from __future__ import annotations
from pyrh.pyrh.robinhood import Robinhood
import __init__



class RobinHood_Object(object):
    """ Robinhood superclass  """

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
        self.rh = Robinhood(email, password)
        self.rh.login()

    def reauthorize(self, email, password):
        """ reauthorize Robinhood session using the Robinhood User credentials
            method called in case of session expiriy
        """
        self.rh.login(email, password)

    def end_session(self):
        """ logout of Robinhood session"""
        pass


def begin_robinhood_session(email: str, password: str) -> None:
    """ Starting a Robinhood session using the given email and password
        
        Args:
            email (string): email of Robinhood account
            password (string): password of Robinhood account

        Returns:
            None: only opens the session for the user to use
    """
    __init__.session_token = RobinHood_Object(email, password)


def end_robinhood_session():
    """ Ending a Robinhood session"""
    __init__.session_token.end_session()
    __init__.session_token = None


__all__ = [
    __init__.session_token,
    begin_robinhood_session,
    end_robinhood_session
]
