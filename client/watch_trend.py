from pyrh_redesign.instrument import Instrument
import numpy as np
import matplotlib.pyplot as plt
from session import begin_robinhood_session, end_robinhood_session


def make_trend_graph(ticker_symbol):
    ins = Instrument(Instrument.Type.STOCK, ticker_symbol)
    historical_data = ins.historical_quotes("5minute", "week")
    open_prices = np.zeros(len(historical_data))
    close_prices = np.zeros(len(historical_data))

    for i in range(len(historical_data)):
        quote = historical_data[i]
        open_prices[i] = float(quote['open_price'])
        close_prices[i] = float(quote['close_price'])

    x = np.arange(len(historical_data))
    plt.clf()
    plt.plot(x, open_prices)
    plt.savefig("../results/open_prices_trend_" + ticker_symbol + ".jpg")
    plt.clf()
    plt.plot(x, close_prices)
    plt.savefig("../results/close_prices_trend_" + ticker_symbol + ".jpg")


if __name__ == "__main__":
    creds = open("../credentials").readlines()
    email = creds[0].strip()
    password = creds[1].strip()
    begin_robinhood_session(email, password)
    make_trend_graph("AMZN")
    make_trend_graph("AAPL")
    make_trend_graph("ANTM")
    end_robinhood_session()

