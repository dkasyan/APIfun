const fetch = require('node-fetch')


planetNumber = 5;

fetch(`https://swapi.co/api/planets/${planetNumber}/`) //Wystawienie aplikacji do fetcha
    .then(response => response.json())                  //
    .then(data => console.log(data.climate))
    .catch(err => console.log("Eror", err))


    