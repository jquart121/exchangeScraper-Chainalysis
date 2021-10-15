#import os

#os.system("pip install python-binance") # Added these for convenience but commented them out just in case people would like to manually install python-binance and coinbase
#os.system("pip install coinbase")


#!pip install python-binance
#!pip install coinbase


from binance import Client as cb, ThreadedWebsocketManager, ThreadedDepthCacheManager # api for binance
from coinbase.wallet.client import Client as cc # api for coinbase
from bs4 import BeautifulSoup
import requests
import urllib3
import pandas as pd
from flask import Flask, redirect, url_for


clientb = cb("asasfasder","agegweghter") # filler strings for the client

clientc = cc("asasfasder", "agegweghter", )


prices = clientb.get_all_tickers()
btc = clientc.get_spot_price(currency_pair = 'BTC-USD').amount
eth = clientc.get_spot_price(currency_pair = 'ETH-USD').amount

bnc = pd.DataFrame(prices)

def get_price1B(): # Gets the price for Bitcoin on Binance
    
    #print(bnc[bnc['symbol'] == 'BTCUSDT']['price'].iloc[0])
    return (bnc[bnc['symbol'] == 'BTCUSDT']['price'].iloc[0])
        
def get_price1E(): # Gets the price for Ethereum on Binance
    
    #print(bnc[bnc['symbol'] == 'ETHUSDT']['price'].iloc[0])
    return (bnc[bnc['symbol'] == 'ETHUSDT']['price'].iloc[0])

def get_price2B(): # Gets the price for Bitcoin on Coinbase

    #print(btc)
    return btc


def get_price2E(): # Gets the price for Ethereum on Coinbase

    #print(eth)
    return eth

def recommendBTC(): # Gives the recommendation of whether to buy/sell on Binance or Coinbase for Bitcoin
    binbtc = get_price1B()
    if binbtc < eth:
        return "We recommend you Sell on Coinbase and Buy on Binance."
    else:
        return "We recommend you Sell on Binance and Buy on Coinbase."
    

def recommendETH(): # Gives the recommendation of whether to buy/sell on Binance or Coinbase for Ethereum
    bineth = get_price1E()
    if bineth < eth:
        return "We recommend you Sell on Coinbase and Buy on Binance."
    else:
        return "We recommend you Sell on Binance and Buy on Coinbase."

app = Flask(__name__)

@app.route("/")
def home(): # Wrote this quickly in one line, would normally write this in an html file instead
    str = "<h1>Bitcoin and Ethereum Prices on Binance and Coinbase<h1> <div> <table> <tr> <th>Exchange</th> <th> Bitcoin Price (USD)</th> <th> Ethereum Price (USD)</th> </tr> <tr>  <td>Binance</td> <td>$" + get_price1B() + "</td> <td>$" + get_price1E() + " </td> </tr> <tr> <td> Coinbase</td> <td>$" + get_price2B() + "</td> <td>$" + get_price2E() + " </td> </tr>  </table></div> <div> <h2>Recommendations:</h2> <p>Bitcoin:&emsp;" + recommendBTC() + "<br>Ethereum:&emsp;" + recommendETH() + " </p>  </div>"
    return str



if __name__ == "__main__":
    app.run()



