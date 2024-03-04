import json
import Stock

def stock_info(stock):
    stock_infos = Stock.StockInfos(stock) 
    address_info = stock_infos.address_infos()
    corporate_info = stock_infos.corporate_infos()
    financial_info = stock_infos.financial_infos()
    risk_info = stock_infos.risk_infos()
    price_dividend_info = stock_infos.price_and_dividend_infos()
    
    dict_json = {
        'address_info': address_info,
        'corporate_info': corporate_info,
        'financial_info': financial_info,
        'risk_info': risk_info,
        'price_dividend_info': price_dividend_info
    }
    
    json_str = json.dumps(dict_json, indent=4)
    return json_str
