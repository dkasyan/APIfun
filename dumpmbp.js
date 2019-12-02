const request = require('request');
const fs = require('fs');
const code = 'usd'
const validCodes = ['usd', 'eur', 'gbp', 'chf'];

const url = `http://api.nbp.pl/api/exchangerates/rates/a/${code}/`

request(url, {json: true}, (err, res, body) => {
    if (err) {
        return console.log("Blad: ", err);
    }        
    if (res.statusCode !== 200) {
        return console.log("Cos poszlo nie tak")  
    }
    
    const message = `Srednia cena ${body.currency} w dniu ${body.rates[0].effectiveDate} wynosi ${body.rates[0].mid}`
    console.log(message)
    
})