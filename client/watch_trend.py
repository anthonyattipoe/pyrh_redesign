from pyrh_redesign.instrument import Instrument


def make_trend_graph(ticker_symbol):
    ins = Instrument(Instrument.Type.STOCK, ticker_symbol)

