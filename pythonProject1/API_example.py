import requests
import datetime
r = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")
bitcoin =  r.json()
print(bitcoin)
print("last:" , bitcoin['last'])
print("bid:" , bitcoin['bid'])
print("ask:" , bitcoin['ask'])
print("volume:" , bitcoin['volume'])

timestamp = bitcoin['timestamp']
date = datetime.datetime.fromtimestamp(timestamp/1000)
print("date:", date)