def appnded_():
    appnded = seven_days_ago_price.append(int(float(json_data['data'][-i]['priceUsd'])))
    return appnded
def average():
    a = (f"gor valu {sum(seven_days_ago_price)/(len(seven_days_ago_price))}")
    return a


import json
import requests

# url = "http://api.coincap.io/v2/assets/bitcoin/history?interval=d1&start=1664323200000&end=1664928000000"
url = "http://api.coincap.io/v2/assets/bitcoin/history?interval=d1"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

json_data = json.loads(response.text.encode('utf8'))

day = 1
seven_days_ago_price = []
for i in range(day, 8):
    appnded_()
gor_valu = average()
print(gor_valu)

day = 2
seven_days_ago_price = []
for i in range(day, 9):
    appnded_()
gor_valu = average()
print(gor_valu)


day = 3
seven_days_ago_price = []
for i in range(day, 9):
    appnded_()
gor_valu = average()
print(gor_valu)

