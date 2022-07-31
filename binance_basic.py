import os
from binance.client import Client
import pandas as pd 

api_key = ''
api_secret = ''

binance_client = Client(api_key, api_secret)

for _ in range(1, 10):
    print(binance_client.futures_symbol_ticker(symbol='BTCUSDT'))


df = pd.DataFrame(binance_client.futures_historical_klines(
                                                            symbol='BTCUSDT',
                                                            interval='1d',
                                                            start_str='2016-06-01',
                                                            end_str='2021-06-30'
                                                            ))

#crop uncessary columns
df = df.iloc[:, :6]

# ascribe names to columns
df.columns = [  'date', 
                'open', 
                'high', 
                'low', 
                'close', 
                'volume']

# convert timestamp to date format and ensure ohlcv are all numeric
df['date'] = pd.to_datetime(df['date'], unit='ms')
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col])

df = pd.DataFrame(binance_client.futures_order_book(symbol='BTCUSDT'))

#create market order
binance_client.futures_create_order(
    symbol='BTCUSDT',
    type='MARKET',
    timeInForce='GTC',
    side='BUY',
    quantity=0.001
)