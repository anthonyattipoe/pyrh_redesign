## ask_price

rh.ask_price("CRM")

[['161.940000', '']]

Says it returns: float

Actually returns: list[list[str,str]]

Possible fix: wrapper to access float(rh.ask_price("CRM")[0][0])
