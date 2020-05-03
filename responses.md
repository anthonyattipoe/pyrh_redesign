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
