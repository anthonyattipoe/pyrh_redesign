## ask_price

rh.ask_price("CRM")

[['161.940000', '']]

Says it returns: float

Actually returns: list[list[str,str]]

Possible fix: wrapper to access float(rh.ask_price("CRM")[0][0])

## ask_size

rh.ask_size("CRM")

ERROR: TypeError: unsupported operand type(s) for +: 'int' and 'str'

##### Fix to error: Robinhood.py
Original
```
434-445 under get_quote_list()
# Creates a tuple containing the information we want to retrieve
        def append_stock(stock):
            keys = key.split(",")
            myStr = ""
            for item in keys:
                myStr += stock[item] + ","

            return myStr.split(",")
```
Fixed Version
```
434-445 under get_quote_list()
# Creates a tuple containing the information we want to retrieve
        def append_stock(stock):

            keys = key.split(",")
            myStr = ""
            for item in keys:
                if isinstance(stock[item], str):
                    myStr += stock[item] + ","
                elif isinstance(stock[item], int):
                    myStr += str(stock[item]) + ","

            return myStr.split(",")
```

Says it returns: int

Actually returns: list[list[str,str]]

Possible fix: wrapper to access int(rh.ask_size("CRM")[0][0])

## bid_price
rh.bid_price("CRM")

[['155.000000', '']]

Says it returns: float

Actually returns: list[list[str,str]]

Possible fix: wrapper to access float(rh.bid_price("CRM")[0][0])

## bid_size
rh.bid_size("CRM")

[['30', '']]

Says it returns: int

Actually returns: list[list[str,str]]

Possible fix: wrapper to access int(rh.bid_size("CRM")[0][0])


## adjusted_equity_previous_close
rh.adjusted_equity_previous_close()

1000000.49

Accurately returns float value of equity value from user's account

Possible fix: Name is definitely confusing, it's the equity with market adjustments. Could be merged with equity_previous_close?

## adjusted_previous_close
rh.adjusted_previous_close("CRM")

[['161.950000', '']]

Says it returns: float

Actually returns: list[list[str,str]]

Possible fix: wrapper to access int(rh.adjusted_previous_close("CRM")[0][0])

## dividends
rh.dividends()

Says it returns JSON dict from getting dividends
Actual structure of return JSON (heavily redacted)
```
{'next': None, 
 'previous': None, 
 'results': [
	{'id': ID_NUMBER_AS_STR, 
	 'url': URL_AS_STR, 
	 'account': ACCOUNT_URL_AS_STR, 
	 'instrument': INSTRUMENT_URL_AS_STR, 
	 'amount': '0.36', 
	 'rate': '0.1200000000', 
	 'position': '3.00000000', 
	 'withholding': '0.00', 
	 'record_date': '2020-03-05', 
	 'payable_date': '2020-03-16', 
	 'paid_at': '2020-03-17T02:14:50Z', 
	 'state': 'paid', 
	 'nra_withholding': None, 
	 'drip_enabled': False
	}
        ]
}
```
Possible fix: Should be clearly laid out what everything is in return type. Not sure what next and previous are. keys within each dividend have some industry terminology I don't understand (e.g. drip_enabled?).


## equity
rh.equity()

1000000.49

Accurately returns float value of equity value from user's account

Possible fix: Nothing, but could be placed under our user model. Merge with other equity functions.

## equity_previous_close
rh.equity_previous_close()

1000000.49

Accurately returns float value of equity value of the previous close from user's account

Possible fix: Nothing, but could be placed under our user model. Merge with other equity functions.

## excess_margin
rh.excess_margin()

900000.49

Accurately returns float value of excess margin value from user's account

Possible fix: Nothing, but could be placed under our user model.


## extended_hours_equity
rh.extended_hours_equity()

1000000.49

Accurately returns float value of equity value of extended hours from user's account

Possible fix: Nothing, but could be placed under our user model. Merge with other equity functions.

## extended_hours_market_value
rh.extended_hours_market_value()

800000.49

Accurately returns float value of market value of extended hours from user's account

Possible fix: Nothing, but could be placed under our user model.

## fundamentals & get_fundamentals
fundamentals and get_fundamentals are the same exact function, can remove one for sure

rh.fundamentals('CRM')

```
{
 'open': '158.310000', 
 'high': '160.170000', 
 'low': '155.260000', 
 'volume': '4275536.000000', 
 'average_volume_2_weeks': '6414987.900000', 
 'average_volume': '6414987.900000', 
 'high_52_weeks': '195.720000', 
 'dividend_yield': None, 
 'float': '859278760.000000', 
 'low_52_weeks': '115.290000', 
 'market_cap': '139951150000.000000', 
 'pb_ratio': '4.120950', 
 'pe_ratio': '1055.130000', 
 'shares_outstanding': '895000000.000000', 
 'description': 'salesforce.com, inc. engages in the ... blah blah blah', 
 'instrument': 'https://api.robinhood.com/instruments/cf1d849d-06f7-4374-9e84-13129713d0c7/', 
 'ceo': 'Marc Russell Benioff', 
 'headquarters_city': 'San Francisco', 
 'headquarters_state': 'California', 
 'sector': 'Technology Services', 
 'industry': 'Packaged Software', 
 'num_employees': 49000, 'year_founded': 1999
 }
```

Possible fix: Don't think we need to change, just place in right spot. Define what will be returned in docs.

## get_account
rh.get_account

Returns the account information from the account endpoint
This what the endpoint currently returns (redacted)
```
{
'url': 'https://api.robinhood.com/accounts/ACCOUNT_NUMBER/', 
'portfolio_cash': '14321013.1900', 
'can_downgrade_to_cash': 'https://api.robinhood.com/accounts/ACCOUNT_NUMBER/can_downgrade_to_cash/', 
'user': 'api.robinhood.com/user/', 
'account_number': 'ACCOUNT_NUMBER', 
'type': 'margin', 
'created_at': '2019-07-31T23:53:57.197892Z', 
'updated_at': '2020-04-21T12:21:54.168775Z', 
'deactivated': False, 
'deposit_halted': False, 
'withdrawal_halted': False, 
'only_position_closing_trades': False, 
'buying_power': '14321013.1900', 
'cash_available_for_withdrawal': '14321013.1900', 
'cash': '14321013.1900', 
'cash_held_for_orders': '0.0000', 
'uncleared_deposits': '0.0000', 
'sma': '0', 
'sma_held_for_orders': '0', 
'unsettled_funds': '0.0000', 
'unsettled_debit': '0.0000', 
'crypto_buying_power': '14321013.1900', 
'max_ach_early_access_amount': '10000.00', 
'cash_balances': None, 
'margin_balances': {
	SOME_DICT_VALS
}, 
'sweep_enabled': False, 
'instant_eligibility': {
	SOME_DICT_VALS
	}, 
'option_level': None, 
'is_pinnacle_account': True, 
'rhs_account_number': ACCOUNT_NUMBER, 
'state': 'active', 
'active_subscription_id': None, 
'locked': False, 
'permanently_deactivated': False, 
'received_ach_debit_locked': False, 
'drip_enabled': False, 
'eligible_for_fractionals': False, 
'eligible_for_drip': False, 
'cash_management_enabled': False, 
'cash_held_for_options_collateral': '0.0000', 
'fractional_position_closing_only': False, 
'user_id': USER_ID
}
```

Possible fix: It's just an endpoint wrapper so it might change, but can still be placed within user.
## get_news
rh.get_news("GOOG")

Returns the news information from the news endpoint
This what the endpoint currently returns (shortened results)
```
{'count': 1, 
 'next': None, 
 'previous': None, 
 'results': [
 	{'api_source': 'reuters', 
 	 'author': '', 
 	 'num_clicks': 1199, 
 	 'preview_image_url': 'https://images.robinhood.com/dYW7Rpkz75W5olNy3uwSk64ViME/aHR0cHM6Ly9pbWFnZXMucm9iaW5ob29kLmNvb...', 
 	 'published_at': '2020-05-01T22:20:15Z', 
 	 'relay_url': 'https://news.robinhood.com/8a681d3e-ff0e-3cbd-bd2f-9e6c94b9777f/', 
 	 'source': 'Reuters', 
 	 'summary': '', 
 	 'title': 'Google travel data show lockdown fatigue in U.S., Australia; other countries stay home', 
 	 'updated_at': '2020-05-02T00:32:41.790799Z', 
 	 'url': 'https://www.reuters.com/article/us-health-coronavirus-google/google-travel-data-show-lockdown-fatigue-in-u-s-australia-other-countries-stay-home-idUSKBN22D6AX', 
 	 'uuid': '8a681d3e-ff0e-3cbd-bd2f-9e6c94b9777f', 
 	 'related_instruments': ['943c5009-a0bb-4665-8cf4-a95dab5874e4'], 
 	 'preview_text': 'OAKLAND, Calif. (Reuters) - More people stayed home in Brazil, Japan and Singapore in April as those countries’ novel coronavirus cases surged, while people in', 
 	 'currency_id': 'None'}, 
 ]
}
```

Possible fix: It's just an endpoint wrapper so it might change, but can still be placed somewhere else.

## get_open_orders

## get_option_market_data

## get_options

Function does not return anything - wrong inputs?

rh.get_options("AAPL","2021-05-30",'put')

## get_popularity

rh.get_popularity("GOOG")

Returns int
27216

## get_quote

rh.get_quote("GOOG")

Returns dict
```
{'ask_price': '1369.000000', 
 'ask_size': 150, 
 'bid_price': '1310.000000', 
 'bid_size': 50, 
 'last_trade_price': '1320.610000', 
 'last_extended_hours_trade_price': '1320.610000', 
 'previous_close': '1348.660000', 
 'adjusted_previous_close': '1348.660000', 
 'previous_close_date': '2020-04-30', 
 'symbol': 'GOOG', 
 'trading_halted': False, 
 'has_traded': True, 
 'last_trade_price_source': 'consolidated', 
 'updated_at': '2020-05-02T00:00:00Z', 
 'instrument': 'https://api.robinhood.com/instruments/943c5009-a0bb-4665-8cf4-a95dab5874e4/'}
```

## get_quote_list
rh.get_quote_list("GOOG,AAPL")

Currently broken - can't parse?

## get_tickers_by_tag
 rh.get_tickers_by_tag("top-movers")
 
 ```
['CODX', 'SM', 'CEQP', 'GPOR', 'CAR', 'ARCT', 'PBF', 'WY', 'OII', 'IMXI', 'DISCB', 'CURO', 'CAPL', 'LBTYB', 'OPCH', 'LBTYK', 'ASGN', 'LBTYA', 'SHEN', 'VRTS']
```

## get_url

rh.get_url('')

This is to be used for making requests while being logged in. idk if we should keep it

## instrument

rh.instrument("943c5009-a0bb-4665-8cf4-a95dab5874e4")

Might be broken? I'm not 100% sure what I'm supposed to use for the id

## instruments

rh.instruments("GOOG")

Acutally returns list of dict (shortened)
```
[
	{
	 'id': '943c5009-a0bb-4665-8cf4-a95dab5874e4', 
	 'url': 'https://api.robinhood.com/instruments/943c5009-a0bb-4665-8cf4-a95dab5874e4/', 
	 'quote': 'https://api.robinhood.com/quotes/GOOG/', 
	 'fundamentals': 'https://api.robinhood.com/fundamentals/GOOG/', 
	 'splits': 'https://api.robinhood.com/instruments/943c5009-a0bb-4665-8cf4-a95dab5874e4/splits/', 
	 'state': 'active', 
	 'market': 'https://api.robinhood.com/markets/XNAS/', 
	 'simple_name': 'Alphabet Class C', 
	 'name': 'Alphabet Inc. Class C Capital Stock', 
	 'tradeable': True, 
	 'tradability': 'tradable', 
	 'symbol': 'GOOG', 
	 'bloomberg_unique': 'EQ0000000044670269', 
	 'margin_initial_ratio': '0.5000', 
	 'maintenance_ratio': '0.2500', 
	 'country': 'US', 
	 'day_trade_ratio': '0.2500', 
	 'list_date': '2004-08-19', 
	 'min_tick_size': None, 
	 'type': 'stock', 
	 'tradable_chain_id': '9330028e-455f-4acf-9954-77f60b19151d', 
	 'rhs_tradability': 'tradable', 
	 'fractional_tradability': 'tradable', 
	 'default_collar_fraction': '0.05'}
]
```

## investment_profile

rh.investment_profile()
returns dict object (redacted)
```
{
 'user': 'api.robinhood.com/user/', 
 'total_net_worth': RANGE_RANGE_STR, 
 'annual_income': RANGE_RANGE_STR, 
 'source_of_funds': STR, 
 'investment_objective': 'income_invest_obj', 
 'investment_experience': STR, 
 'liquid_net_worth': RANGE_RANGE_STR, 
 'risk_tolerance': STR, 
 'tax_bracket': '', 
 'time_horizon': STR, 
 'liquidity_needs': STR, 
 'investment_experience_collected': BOOL, 
 'suitability_verified': BOOL, 
 'option_trading_experience': '', 
 'professional_trader': None, 
 'understand_option_spreads': BOOL, 
 'interested_in_options': None, 
 'updated_at': '2019-08-01T16:18:26.996458Z'
 }
```

## last_core_equity

rh.last_core_equity()

100001.98

correctly returns float value

## last_core_market_value


rh.last_core_market_value()

90001.98

correctly returns float value

## last_trade_price

rh.last_trade_price("FB")

[['202.270000', '']]

## last_updated_at

rh.last_updated_at("FB")

Currently broken:
KeyError: 'last_updated_at'

## last_updated_at_datetime

rh.last_updated_at_datetime("FB")

Currently broken:
KeyError: 'last_updated_at'

## market_value

rh.market_value()
23828347.11

correctly returns float:

Can probably be merged with other market_value calls

## order_history

## place_buy_order

*****************
PLACING BUY ORDER
*****************

#### Buying ZOM

{'id': '7bc37f3d-c2b1-4945-916a-5cd55b4e7264', 'ref_id': None, 'url': 'https://api.robinhood.com/orders/7bc37f3d-c2b1-4945-916a-5cd55b4e7264/', 'account': 'https://api.robinhood.com/accounts/843657974/', 'position': 'https://api.robinhood.com/positions/843657974/6b016aac-a281-40a1-bc1c-390d286444a9/', 'cancel': 'https://api.robinhood.com/orders/7bc37f3d-c2b1-4945-916a-5cd55b4e7264/cancel/', 'instrument': 'https://api.robinhood.com/instruments/6b016aac-a281-40a1-bc1c-390d286444a9/', 'cumulative_quantity': '0.00000000', 'average_price': None, 'fees': '0.00', 'state': 'unconfirmed', 'type': 'market', 'side': 'buy', 'time_in_force': 'gfd', 'trigger': 'immediate', 'price': '0.24900000', 'stop_price': None, 'quantity': '3.00000000', 'reject_reason': None, 'created_at': '2020-05-08T17:20:19.182892Z', 'updated_at': '2020-05-08T17:20:19.230986Z', 'last_transaction_at': '2020-05-08T17:20:19.182892Z', 'executions': [], 'extended_hours': False, 'override_dtbp_checks': False, 'override_day_trade_checks': False, 'response_category': None, 'stop_triggered_at': None, 'last_trail_price': None, 'last_trail_price_updated_at': None, 'total_notional': {'amount': '0.75', 'currency_code': 'USD', 'currency_id': '1072fc76-1862-41ab-82c2-485837590762'}, 'executed_notional': None, 'investment_schedule_id': None}

## place_limit_buy_order

## place_limit_sell_order

## place_market_buy_order

## place_market_sell_order

## place_order

## place_sell_order

## place_stop_limit_buy_order

## place_stop_limit_sell_order

## place_stop_loss_buy_order

## place_stop_loss_sell_order

## portfolios

rh.portfoliios()

```
{'url': 'https://api.robinhood.com/portfolios/ACCOUNT_ID/', 
 'account': 'https://api.robinhood.com/accounts/ACCOUNT_ID/', 
 'start_date': '2019-07-31', 
 'market_value': FLOAT_AS_STR, 
 'equity': FLOAT_AS_STR, 
 'extended_hours_market_value': FLOAT_AS_STR, 
 'extended_hours_equity': FLOAT_AS_STR, 
 'extended_hours_portfolio_equity': FLOAT_AS_STR, 
 'last_core_market_value': FLOAT_AS_STR, 
 'last_core_equity': FLOAT_AS_STR, 
 'last_core_portfolio_equity': FLOAT_AS_STR, 
 'excess_margin': FLOAT_AS_STR, 
 'excess_maintenance': FLOAT_AS_STR, 
 'excess_margin_with_uncleared_deposits': FLOAT_AS_STR, 
 'excess_maintenance_with_uncleared_deposits': FLOAT_AS_STR, 
 'equity_previous_close': FLOAT_AS_STR, 
 'portfolio_equity_previous_close': FLOAT_AS_STR, 
 'adjusted_equity_previous_close': FLOAT_AS_STR, 
 'adjusted_portfolio_equity_previous_close': FLOAT_AS_STR, 
 'withdrawable_amount': FLOAT_AS_STR, 
 'unwithdrawable_deposits': FLOAT_AS_STR, 
 'unwithdrawable_grants': FLOAT_AS_STR
 }
```

## positions

rh.positions()

returns a dict (shortened results)
```
{'next': None, 
 'previous': None, 
 'results': [
	 {'url': 'https://api.robinhood.com/positions/ACCOUNT_NUMBER/ID_NUMBER/', 
	 'instrument': 'https://api.robinhood.com/instruments/ID_NUMBER/', 
	 'account': 'https://api.robinhood.com/accounts/ACCOUNT_NUMBER/', 
	 'account_number': 'ACCOUNT_NUMBER', 
	 'average_buy_price': PRICE_STR_FLT, 
	 'pending_average_buy_price': PRICE_STR_FLT, 
	 'quantity': QUANTITY_STR_FLT, 
	 'intraday_average_buy_price': '0.0000', 
	 'intraday_quantity': '0.00000000', 
	 'shares_held_for_buys': '0.00000000', 
	 'shares_held_for_sells': '2.00000000', 
	 'shares_held_for_stock_grants': '0.00000000', 
	 'shares_held_for_options_collateral': '0.00000000', 
	 'shares_held_for_options_events': '0.00000000', 
	 'shares_pending_from_options_events': '0.00000000', 
	 'updated_at': '2020-05-02T20:11:41.491656Z', 
	 'created_at': '2019-07-31T23:57:07.494746Z'
	 }
 ]}
```

## previous_close

rh.previous_close("FB")
[['204.710000', '']]

## previous_close_date

rh.previous_close_date("FB")
[['2020-04-30', '']]

## print_quote

rh.print_quote("FB")
>> FB: $202.270000

## print_quotes

rh.print_quotes(["FB","GOOG"])
>> FB: $202.270000
>> GOOG: $1320.610000

## quote_data

rh.quote_data('FB')

```
{'ask_price': '240.000000', 
 'ask_size': 1750, 
 'bid_price': '185.000000', 
 'bid_size': 1500, 
 'last_trade_price': '202.270000', 
 'last_extended_hours_trade_price': '202.790000', 
 'previous_close': '204.710000', 
 'adjusted_previous_close': '204.710000', 
 'previous_close_date': '2020-04-30', 
 'symbol': 'FB', 
 'trading_halted': False, 
 'has_traded': True, 
 'last_trade_price_source': 'consolidated', 
 'updated_at': '2020-05-02T00:00:00Z', 
 'instrument': 'https://api.robinhood.com/instruments/ebab2398-028d-4939-9f1d-13bf38f81c50/'}
```
## quotes_data
rh.quotes_data(['FB','GOOG'])
```
[{
 'ask_price': '240.000000', 
 'ask_size': 1750, 
 'bid_price': '185.000000', 
 'bid_size': 1500, 
 'last_trade_price': '202.270000', 
 'last_extended_hours_trade_price': '202.790000', 
 'previous_close': '204.710000', 
 'adjusted_previous_close': '204.710000', 
 'previous_close_date': '2020-04-30', 
 'symbol': 'FB', 
 'trading_halted': False, 
 'has_traded': True, 
 'last_trade_price_source': 'consolidated', 
 'updated_at': '2020-05-02T00:00:00Z', 
 'instrument': 'https://api.robinhood.com/instruments/ebab2398-028d-4939-9f1d-13bf38f81c50/'
 }, 
 {
 'ask_price': '1369.000000', 
 'ask_size': 150, 
 'bid_price': '1310.000000', 
 'bid_size': 50, 
 'last_trade_price': '1320.610000', 
 'last_extended_hours_trade_price': '1320.610000', 
 'previous_close': '1348.660000', 
 'adjusted_previous_close': '1348.660000', 
 'previous_close_date': '2020-04-30', 
 'symbol': 'GOOG', 
 'trading_halted': False, 
 'has_traded': True, 
 'last_trade_price_source': 'consolidated', 
 'updated_at': '2020-05-02T00:00:00Z', 
 'instrument': 'https://api.robinhood.com/instruments/943c5009-a0bb-4665-8cf4-a95dab5874e4/'
 }
]
```

## securities_owned

rh.securities_owned()
returns this dict, results shortened
```
{'next': None, 
 'previous': None, 
 'results': [{
 'url': 'https://api.robinhood.com/positions/ACCOUNT_ID/INSTRUMENT_ID/', 
 'instrument': 'https://api.robinhood.com/instruments/INSTRUMENT_ID/', 
 'account': 'https://api.robinhood.com/accounts/ACCOUNT_ID/', 
 'account_number': 'ACCOUNT_ID', 
 'average_buy_price': FLT_STR, 
 'pending_average_buy_price': FLT_STR, 
 'quantity': FLT_STR, 
 'intraday_average_buy_price': '0.0000', 
 'intraday_quantity': '0.00000000', 
 'shares_held_for_buys': '0.00000000', 
 'shares_held_for_sells': '2.00000000', 
 'shares_held_for_stock_grants': '0.00000000', 
 'shares_held_for_options_collateral': '0.00000000', 
 'shares_held_for_options_events': '0.00000000', 
 'shares_pending_from_options_events': '0.00000000', 
 'updated_at': '2020-05-02T20:11:41.491656Z', 
 'created_at': '2019-07-31T23:57:07.494746Z'}
 ]
} 
```

## submit_buy_order

## submit_sell_order

## symbol

rh.symbol("FB")
[['FB', '']]

rh.symbol("fb")
pyrh.exceptions.InvalidTickerSymbol
