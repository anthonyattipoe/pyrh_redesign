from __future__ import annotations
from pyrh.pyrh.robinhood import Robinhood


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
        self.rh.logout()


session_token = None


def begin_robinhood_session(email, password):
    global session_token
    session_token = RobinHood_Object(email, password)


def end_robinhood_session():
    global session_token
    session_token.end_session()
    session_token = None


__all__ = [
    session_token
]

# unit testing
if __name__ == "__main__":
    begin_robinhood_session("evangelinehliu@hotmail.com", "APIsAreGreat!!1")
    end_robinhood_session()
