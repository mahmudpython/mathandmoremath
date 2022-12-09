"""
Gather possible decimal point
Market Forcats : https://coincap.io/assets/bitcoin
Api Documentation : https://docs.coincap.io/

"""

import json

import requests

# url = "http://api.coincap.io/v2/assets/bitcoin/history?interval=d1&start=1664323200000&end=1664928000000"
# url = "http://api.coincap.io/v2/assets/ethereum/history?interval=d1"
url = "http://api.coincap.io/v2/assets/bitcoin/history?interval=d1"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

json_data = json.loads(response.text.encode('utf8'))

# pprint(json_data['data'])

previous_days = 7

seven_days_ago_price = json_data['data'][-previous_days]['priceUsd']
# print(f"Seven Days Ago Price : {seven_days_ago_price}")

today_price = json_data['data'][-1]['priceUsd']
# print(f"Today Price : {today_price}")

# print("Write your code below 'VVVVVV'")
price_list = []
for price in json_data['data']:
    # print(price)
    # print(price['priceUsd'])
    price_list.append(int(float(price['priceUsd'])))

print(price_list)


# for btc_price in price_list:
#     # print(len(price_list))
#     print(price_list[len(price_list)-1])
#     # print(btc_price)



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

ten_days_data = []
for i in range (10):
    # print(-i)
    ten_days_data.append(int(float(json_data['data'][i+1]['priceUsd'])))

print(ten_days_data)
print(len(ten_days_data))
print(sum(ten_days_data)/(len(ten_days_data)))

fourteen_five_days_data = []
for i in range (45):
    # print(-i)
    fourteen_five_days_data.append((int(float(json_data['data'][-i]['priceUsd']))))
print(fourteen_five_days_data)
print(len(fourteen_five_days_data))
print(sum(fourteen_five_days_data)/len(fourteen_five_days_data))


