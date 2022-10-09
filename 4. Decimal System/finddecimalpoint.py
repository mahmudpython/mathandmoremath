"""
Gather possible decimal point
Market Forcats : https://coincap.io/assets/bitcoin
Api Documentation : https://docs.coincap.io/
"""

import json

import requests

# url = "http://api.coincap.io/v2/assets/bitcoin/history?interval=d1&start=1664323200000&end=1664928000000"
url = "http://api.coincap.io/v2/assets/bitcoin/history?interval=d1"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

json_data = json.loads(response.text.encode('utf8'))


previous_days = 7

seven_days_ago_price = json_data['data'][-previous_days]['priceUsd']
print(f"Seven Days Ago Price : {seven_days_ago_price}")

today_price = json_data['data'][-1]['priceUsd']
print(f"Today Price : {today_price}")

print("Write your code below 'VVVVVV'")

seven_days_ago_price = float(seven_days_ago_price)
today_price = float(today_price)
price = today_price-seven_days_ago_price
increage = price/seven_days_ago_price
persantace_incrage = increage*100
print(persantace_incrage)

'''
90 days ago price from 10 days ago price how Persantace Updown?
'''

previous_days = 90


ninty_days_ago_price = json_data['data'][-previous_days]['priceUsd']
print(ninty_days_ago_price)
ten_days_ago_price = json_data['data'][-11]['priceUsd']
print(ten_days_ago_price)
ninty_days_ago_price = float(ninty_days_ago_price)
ten_days_ago_price = float(ten_days_ago_price)
price = (ninty_days_ago_price-ten_days_ago_price)
increage = price/ninty_days_ago_price
persantace_incrage = increage*100
print(persantace_incrage)

'''
last ten days value arrange
'''

last_one = ten_days_ago_price = json_data['data'][-1]['priceUsd']
last_two = ten_days_ago_price = json_data['data'][-2]['priceUsd']
last_three = ten_days_ago_price = json_data['data'][-3]['priceUsd']
last_four = ten_days_ago_price = json_data['data'][-4]['priceUsd']
last_five = ten_days_ago_price = json_data['data'][-5]['priceUsd']
last_six = ten_days_ago_price = json_data['data'][-5]['priceUsd']
last_seven = ten_days_ago_price = json_data['data'][-6]['priceUsd']
last_eight = ten_days_ago_price = json_data['data'][-7]['priceUsd']
last_nine = ten_days_ago_price = json_data['data'][-8]['priceUsd']
last_tem = ten_days_ago_price = json_data['data'][-9]['priceUsd']

avarage = (last_one+last_two+last_three+last_four+last_five+last_six+last_seven+ \
           last_eight+last_nine+last_tem/10)

