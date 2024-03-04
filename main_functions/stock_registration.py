class StockTransactions:

    def __init__(self, account, existing_stocks) -> None:
        self.account = account
        self.existing_stocks = existing_stocks

    def stock_buy(self, ticker, price, amount):
        if ticker in existing_stocks:
            stock_quantity = existing_stocks[ticker]
            new_quantity = stock_quantity + amount
            existing_stocks[ticker] = new_quantity
        else:
            existing_stocks[ticker] = amount

        return existing_stocks
    
    def stock_sell(self, ticker, price, amount):
        if ticker in existing_stocks:
            stock_quantity = existing_stocks[ticker]
            if stock_quantity > amount:
                new_quantity = stock_quantity - amount
                existing_stocks[ticker] = new_quantity
                return existing_stocks
            else:
                return f"You cannot sell more stocks than you have!\nTicker: {ticker}\nOwned: {stock_quantity}\nTrying to sell: {amount}"
        else:
            return f"{ticker} not found in your wallet"



if __name__ == '__main__':
    account = 123456
    existing_stocks = {
        'MSFT': 50,
        'TSLA': 20,
        'TROW': 30,
        'BRK.B': 25,
        'META': 10
    }

    print(existing_stocks)

    transactions = StockTransactions(account, existing_stocks)
    new_stock = 'META'
    price = 99.56
    amount = 15

    stocks_buy = transactions.stock_buy(new_stock, price, amount)
    print(stocks_buy)

    new_stock = 'TROW'
    price = 54.47
    amount = 40

    stocks_sell = transactions.stock_sell(new_stock, price, amount)
    print(stocks_sell)