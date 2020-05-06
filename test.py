from __init__ import begin_robinhood_session, end_robinhood_session, SessionToken
import sys


def main(argv):
	begin_robinhood_session(argv[1],argv[2])

	end_robinhood_session()

main(sys.argv)