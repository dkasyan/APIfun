const fs = require('fs');

let names = "";
try {
    names = fs.readFileSync('imiona.txt', 'utf8');
} catch (err) {
    names = false
}
console.log(names);

//WRITEFILE APPENDFILE
