import yfinance as yf
import json

stock = yf.Ticker("MSFT")
stock_infos = stock.info
print(json.dumps(stock_infos, indent=4))

hist = stock.history(period='1mo')

