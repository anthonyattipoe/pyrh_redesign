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

## get_popularity

## get_quote

## get_quote_list

## get_tickers_by_tag

## get_url

## instrument

## instruments

## investment_profile

## last_core_equity

## last_core_market_value

## last_trade_price

## last_updated_at

## last_updated_at_datetime

## market_value

## order_history

## place_buy_order

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

## positions

## previous_close

## previous_close_date

## print_quote

## print_quotes

## quote_data

## quotes_data

## securities_owned

## submit_buy_order

## submit_sell_order

## symbol
