import requests
import csv
import json

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()[0]
data_dict = data.keys()
print(type(data))
print(data_dict)
#print(data_dict['rates'])
#print(data.dumps("\"table\currency")
#print(data.keys())

#print(data["currency"])



#data = {"data": {
#  "id": 1,
#  "name": "Something",
#  "colors": ["red", "blue"]
#  }
#}

#print(type(data))
# <class 'dict'>




### To do zapisu
#with open('curency.csv', 'w', newline='') as csvfile:
#    spamwriter = csv.writer(csvfile, delimiter=' ',
#                            quotechar=';', quoting=csv.QUOTE_MINIMAL)
#    spamwriter.writerow(['currency', 'code', 'bid', 'ask'])