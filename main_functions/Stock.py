import yfinance as yf

class StockInfos:

    def __init__(self, stock):
        self.stock = yf.Ticker(stock)
        self.stock_infos = self.stock.info

    def address_infos(self):
        """Retorna informações de endereço da empresa."""
        address = self.stock_infos['address1']
        city = self.stock_infos['city']
        state = self.stock_infos['state']
        zip_code = self.stock_infos['zip']
        country = self.stock_infos['country']
        phone = self.stock_infos['phone']
        return {
            "address": address,
            "city": city,
            "state": state,
            "zip_code": zip_code,
            "country": country,
            "phone": phone
        }

    def corporate_infos(self):
        """Retorna informações corporativas básicas."""
        name = self.stock_infos['shortName']
        website = self.stock_infos['website']
        industry = self.stock_infos['industry']
        sector = self.stock_infos['sector']
        full_time_employees = self.stock_infos['fullTimeEmployees']
        ceo = self.stock_infos['companyOfficers'][0]['name'] if self.stock_infos['companyOfficers'] else 'N/A'
        long_business_summary = self.stock_infos['longBusinessSummary']
        return {
            "name": name,
            "website": website,
            "industry": industry,
            "sector": sector,
            "full_time_employees": full_time_employees,
            "ceo": ceo,
            "long_business_summary": long_business_summary
        }

    def financial_infos(self):
        """Retorna métricas financeiras principais."""
        market_cap = self.stock_infos['marketCap']
        volume = self.stock_infos['volume']
        dividend_rate = self.stock_infos['dividendRate']
        dividend_yield = self.stock_infos['dividendYield']
        payout_ratio = self.stock_infos['payoutRatio']
        beta = self.stock_infos['beta']
        trailing_pe = self.stock_infos.get('trailingPE', 'N/A')  # Usa get para evitar KeyErrors
        forward_pe = self.stock_infos.get('forwardPE', 'N/A')
        book_value = self.stock_infos['bookValue']
        price_to_book = self.stock_infos['priceToBook']
        return {
            "market_cap": market_cap,
            "volume": volume,
            "dividend_rate": dividend_rate,
            "dividend_yield": dividend_yield,
            "payout_ratio": payout_ratio,
            "beta": beta,
            "trailing_pe": trailing_pe,
            "forward_pe": forward_pe,
            "book_value": book_value,
            "price_to_book": price_to_book
        }

    def risk_infos(self):
        """Retorna informações sobre os riscos associados à empresa."""
        audit_risk = self.stock_infos['auditRisk']
        board_risk = self.stock_infos['boardRisk']
        compensation_risk = self.stock_infos['compensationRisk']
        shareholder_rights_risk = self.stock_infos['shareHolderRightsRisk']
        overall_risk = self.stock_infos['overallRisk']
        return {
            "audit_risk": audit_risk,
            "board_risk": board_risk,
            "compensation_risk": compensation_risk,
            "shareholder_rights_risk": shareholder_rights_risk,
            "overall_risk": overall_risk
        }

    def price_and_dividend_infos(self):
        """Retorna informações sobre preços e dividendos."""
        previous_close = self.stock_infos['previousClose']
        open_price = self.stock_infos['open']
        day_low = self.stock_infos['dayLow']
        day_high = self.stock_infos['dayHigh']
        fifty_two_week_low = self.stock_infos['fiftyTwoWeekLow']
        fifty_two_week_high = self.stock_infos['fiftyTwoWeekHigh']
        return {
            "previous_close": previous_close,
            "open": open_price,
            "day_low": day_low,
            "day_high": day_high,
            "fifty_two_week_low": fifty_two_week_low,
            "fifty_two_week_high": fifty_two_week_high
        }

class StockHistorical:

    def __init__(self, stock, period):
        self.stock = yf.Ticker(stock)
        self.stock_historical_data = self.stock.history(period=period)



ticker = 'MSFT'
stock_infos = StockInfos(ticker)
period = '1mo'
stock_historical_data = StockHistorical(ticker, period)
