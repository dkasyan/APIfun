import requests
import csv
import json
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template

app = Flask(__name__)

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



@app.route('/', methods=['GET'])
def message():
    if request.method == "GET":
        data = request.form
        currency = data.get('currency')
        author = data.get("author")
        print(data)
        print(currency)
        print(author)

   # print(request.form)
    return render_template("cc_form.html")
   # return redirect('/cc_form.html')



### To do zapisu
#with open('curency.csv', 'w', newline='') as csvfile:
#    spamwriter = csv.writer(csvfile, delimiter=' ',
#                            quotechar=';', quoting=csv.QUOTE_MINIMAL)
#    spamwriter.writerow(['currency', 'code', 'bid', 'ask'])

