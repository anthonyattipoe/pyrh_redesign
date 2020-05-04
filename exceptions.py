class OrderCancellationError(Exception):
    """An exception raised when a user tries to cancel an order in one of the following states:
    * Already executed
    * Already cancelled
    """

    def __init__(self, order) -> OrderCancellationError:
        """Creates a new OrderCancellationError.
        
        Args:
            order: the malformed order.

        Returns:
            A new OrderCancellationError.
        """
        pass

    def __str__(self) -> str:
        """Returns a string description of the OrderCancellationError."""
        return 'An error occurred logging you in with the provided credentials.'


class MalformedOrderError(Exception):
    """An exception thrown when a malformed order is validated."""

    def __init__(self, order) -> MalformedOrderError:
        """Creates a new MalformedOrderError.

        Args:
            order: the malformed order.

        Returns:
            A new MalformedOrderError.
        """
        pass

    def __str__(self) -> str:
        """Returns a string description of the MalformedOrderError."""
        return 'The combination of properties set on your order are illegal.'


class MalformedInstrumentError(Exception):
    """An exception thrown when a user attempts to create an Instrument with an 
    invalid combination of symbol and instrument type."""

    def __init__(self, instrument) -> MalformedInstrumentError:
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

    def __init__(self) -> UnauthorizedUserError:
        """Creates a new UnauthorizedUserError."""
        pass

    def __str__(self) -> str:
        """Returns a string description of the UnauthorizedUserError."""
        return 'An error occurred authorizing your request. Please ensure you are logged in!'


class InvalidLoginCredentialsError(Exception):
    """An exception raised when a user tries to login to Robinhood with the wrong credentials."""

    def __init__(self) -> InvalidLoginCredentialsError:
        """Creates a new InvalidLoginCredentialsError."""
        pass

    def __str__(self) -> str:
        """Returns a string description of the InvalidLoginCredentialsError."""
        return 'An error occurred logging you in with the provided credentials.'
