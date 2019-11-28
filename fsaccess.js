const fs = require('fs');

//ACESS method

fs.access('./names.txt', (err) => {
    console.log(err ? "plik nie istnieje" : "plik istnieje");
})

//Sprawdz czy do pliku mona pisać.
fs.access('./names.txt', fs.constants.W_OK, (err) => {
    console.log(err ? "pliku nie mozna zapisywac" : "plik mozna zapisywac")
})


//READDIR

fs.readdir('./', (err, files) => {
    if (err) return console.log("Blad", err);
    console.log("Blad: ", err);
    console.log("Zawartosc:", files)
})