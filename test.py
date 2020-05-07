import __init__
from session import begin_robinhood_session, end_robinhood_session
from instrument import Instrument


creds = open("credentials").readlines()
email = creds[0].strip()
password = creds[1].strip()


def test_quote():
	begin_robinhood_session(email, password)
	ins = Instrument(Instrument.Type.STOCK, "GOOG")
	print(ins.quote())
	end_robinhood_session()

def test_something_else():
	pass

if __name__ == "__main__":
	test_quote()
	test_something_else()