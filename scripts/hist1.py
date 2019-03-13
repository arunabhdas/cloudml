import requests,json,numpy as np,pandas as pd
#https://api.coinranking.com/v1/public/coin/:coin_id/history/:timeframe
#https://docs.coinranking.com/
def hist_price_dl(coin_id=1335,timeframe = "5y",currency = "USD"):
    '''It accepts coin_id, timeframe, and currency parameters to clean the historic coin data taken from COINRANKING.COM
    It returns a Pandas Series with daily mean values of the selected coin in which the date is set as the index'''
    r = requests.get("https://api.coinranking.com/v1/public/coin/"+str(coin_id)+"/history/"+timeframe+"?base="+currency)
    coin = json.loads(r.text)['data']['history'] #Reading in json and cleaning the irrelevant parts
    df = pd.DataFrame(coin)
    df['price'] = pd.to_numeric(df['price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'],unit='ms').dt.date
    return df.groupby('timestamp').mean()['price']
