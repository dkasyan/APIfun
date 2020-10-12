import requests
import csv
import json


def data_structure():
    with open('curency.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar=';', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['currency', 'code', 'bid', 'ask'])

def outputing_data(currency, code, bid, ask):
    with open('curency.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar=';', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([currency, code, bid, ask])
 

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()[0]
new_data = data['rates']
print(type(new_data))
#print(new_data)

data_structure()
for i in new_data:
    outputing_data(i["currency"], i["code"], i["bid"], i["ask"])


### To do zapisu
#with open('curency.csv', 'w', newline='') as csvfile:
#    spamwriter = csv.writer(csvfile, delimiter=' ',
#                            quotechar=';', quoting=csv.QUOTE_MINIMAL)
#    spamwriter.writerow(['currency', 'code', 'bid', 'ask'])

