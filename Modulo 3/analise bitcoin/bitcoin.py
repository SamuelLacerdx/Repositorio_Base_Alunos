import pandas as pd
import datetime

ds = pd.read_csv('btcusd_1-min_data.csv')

print(ds.head())
print(ds.tail())

x = ds["Timestamp"].apply(lambda h: datetime.datetime.fromtimestamp(h))
y = ds["High"]