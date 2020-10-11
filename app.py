import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
print(data)

with open('curency.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar=';', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['currency', 'code', 'bid', 'ask'])