class OrderCancellationError(Exception):
    """An exception raised when a user tries to cancel an order in one of the following states:
    * Already executed
    * Already cancelled
    """

    def __init__(self, error):
        """Creates a new OrderCancellationError.
        
        Args:
            error: an error string provided by the caller.

        Returns:
            A new OrderCancellationError.
        """
        self.error = error

    def __str__(self) -> str:
        """Returns a string description of the OrderCancellationError."""
        return self.error


class MalformedOrderError(Exception):
    """An exception thrown when a malformed order is validated."""

    def __init__(self, error):
        """Creates a new MalformedOrderError.

        Args:
            order: the malformed order.

        Returns:
            A new MalformedOrderError.
        """
        self.error = error

    def __str__(self) -> str:
        """Returns a string description of the MalformedOrderError."""
        return self.error


class MalformedInstrumentError(Exception):
    """An exception thrown when a user attempts to create an Instrument with an 
    invalid combination of symbol and instrument type."""

    def __init__(self, instrument):
        """Creates a new MalformedInstrumentError.

        Args:
            instrument: the malformed instrument.
        
        Returns:
            A new MalformedInstrumentError.
        """
        pass

    def __str__(self) -> str:
        """Returns a string description of the MalformedInstrumentError."""
        return 'The symbol and instrument type do not match. Please also ensure that the symbol is spelled correctly.'


class UnauthorizedUserError(Exception):
    """An exception raised when an unauthorized user tries to access Robinhood.
    This error may also be raised if a user's session expires.
    """

    def __init__(self):
        """Creates a new UnauthorizedUserError."""
        pass

    def __str__(self) -> str:
        """Returns a string description of the UnauthorizedUserError."""
        return 'An error occurred authorizing your request. Please ensure you are logged in!'


class InvalidLoginCredentialsError(Exception):
    """An exception raised when a user tries to login to Robinhood with the wrong credentials."""

    def __init__(self):
        """Creates a new InvalidLoginCredentialsError."""
        pass

    def __str__(self) -> str:
        """Returns a string description of the InvalidLoginCredentialsError."""
        return 'An error occurred logging you in with the provided credentials.'

class InsufficientFundsError(Exception):
    """An exception raised when a user tries to purchase an Instrument for which they don't have enough funds."""

    def __init__(self, symbol):
        """Creates a new InsufficientFundsError."""
        self.symbol = symbol

    def __str__(self):
        """Returns a string description of the InsufficientFundsError."""
        return 'You do not have suffiecient funds to purchase the desired number of shares of {}'.format(self.symbol)

class UnownedInstrumentError(Exception):
    """An exception raised when a user attempts to sell an Instrument they do not own."""

    def __init__(self, symbol):
        """Creates a new UnownedInstrumentError."""
        self.symbol = symbol
    
    def __str__(self):
        """Returns a string description of the UnownedInstrumentError."""
        return 'You currently do not own any shares of {}'.format(self.symbol)