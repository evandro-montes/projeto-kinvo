import yfinance as yf
import json
from Stock import StockInfos


def stock_search(stock):
    stock = yf.Ticker(stock)
    stock_infos = stock.info
    


if __name__ == '__main__':
    stock = 'MSFT'
    infos = stock_search(stock)

