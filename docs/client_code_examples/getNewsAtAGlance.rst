

Get News at a Glance Example Code
=================================

`Source Code Here <https://github.com/anthonyattipoe/pyrh_redesign/blob/master/client/get_news_at_a_glance.py>`_

.. code-block:: python

	from pyrh_redesign.instrument import Instrument
	from session import begin_robinhood_session, end_robinhood_session


	def get_news_headlines(ticker_symbol):
	    output_file = open('../results/headlines_' + ticker_symbol + '.txt', 'a+')
	    ins = Instrument(Instrument.Type.STOCK, ticker_symbol)
	    news = ins.news()

	    for headline in news:
	        output_file.write('From ' + headline['api_source'] + ': ')
	        output_file.write(headline['title'] + '\n')
	        output_file.write('For more info click on ' + headline['url'] + '\n')
	        output_file.write('----------------------------------------------------------------------------------\n')


	if __name__ == "__main__":
	    creds = open("../credentials").readlines()
	    email = creds[0].strip()
	    password = creds[1].strip()
	    begin_robinhood_session(email, password)
	    get_news_headlines("AMZN")
	    get_news_headlines("AAPL")
	    end_robinhood_session()
