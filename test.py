import __init__
from session import begin_robinhood_session, end_robinhood_session
from Instrument import *
import sys


def main(argv):
	begin_robinhood_session(argv[1],argv[2])
	ins = Instrument(Instrument.Type.STOCK, "GOOG")
	print(ins.quote())
	end_robinhood_session()

main(sys.argv)
