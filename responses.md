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

Says it returns: float

Actually returns: list[list[str,str]]

Possible fix: wrapper to access float(rh.ask_size("CRM")[0][0])
