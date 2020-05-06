import __init__
from Session import begin_robinhood_session, end_robinhood_session
import sys


def main(argv):
	begin_robinhood_session(argv[1],argv[2])
	print(__init__.SessionToken.rh.ask_size("GOOG"))

	end_robinhood_session()

main(sys.argv)
