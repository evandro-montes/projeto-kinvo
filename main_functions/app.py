from flask import Flask, request, jsonify
import Stock

app = Flask(__name__)

@app.route('/stock_info', methods=['POST'])
def get_stock_info():
    stock = request.json['stock']
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
    
    return jsonify(dict_json)

if __name__ == '__main__':
    app.run(debug=True)
