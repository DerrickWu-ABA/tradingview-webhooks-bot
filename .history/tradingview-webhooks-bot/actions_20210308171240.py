import ccxt
from binance.client import Client
import ast
import json
import time
def binance_client(account):
    while True:
        try:
            if account =='aba':
                with open('imtradegod.json','r') as token:
                    file = json.load(token)
                    api_key = file['APIKEY']
                    api_secret = file['PRIVATEKEY']
                    client = Client(api_key, api_secret)
                    return client
            elif account =='derrick':
                with open('derrickwu.json','r') as token:
                    file = json.load(token)
                    api_key = file['APIKEY']
                    api_secret = file['PRIVATEKEY']
                    client = Client(api_key, api_secret)
                    return client
        except:
            time.sleep(5)
            pass

def parse_webhook(webhook_data):

    """
    This function takes the string from tradingview and turns it into a python dict.
    :param webhook_data: POST data from tradingview, as a string.
    :return: Dictionary version of string.
    """

    data = ast.literal_eval(webhook_data)
    return data


def calc_price(given_price):

    """
    Will use this function to calculate the price for limit orders.
    :return: calculated limit price
    """

    if given_price == None:
        price = given_price
    else:
        price = given_price
    return price


def send_order(data):

    """
    This function sends the order to the exchange using ccxt.
    :param data: python dict, with keys as the API parameters.
    :return: the response from the exchange.
    """

    # Replace kraken with your exchange of choice.
    exchange = ccxt.binance({
        # Inset your API key and secrets for exchange in question.
        'apiKey': '',
        'secret': '',
        'enableRateLimit': True,
    })

    # Send the order to the exchange, using the values from the tradingview alert.
    print('Sending:', data['symbol'], data['type'], data['side'], data['amount'], calc_price(data['price']))
    exchange.
    order = exchange.futures_create_order(symbol=symbol,side=data['side'],type='MARKET',quantity=quantity)
    #order = exchange.futures_create_order(data['symbol'], data['type'], data['side'], data['amount'], calc_price(data['price']))
    # This is the last step, the response from the exchange will tell us if it made it and what errors pop up if not.
    print('Exchange Response:', order)

