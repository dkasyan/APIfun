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



#response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
#data = response.json()[0]
#new_data = data['rates']
##print(type(new_data))
##print(new_data)

#data_structure()
#for i in new_data:
#    outputing_data(i["currency"], i["code"], i["bid"], i["ask"])



@app.route('/', methods=['GET', 'POST'])
def message():
    if request.method == "POST":
        print("dupa")
        datas = request.form
        currency = datas.get('currency')
        author = datas.get("author")
        print(datas)

    return render_template("cc_form.html")
     
