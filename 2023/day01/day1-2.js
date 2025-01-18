"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
var myMap = [
    { "name": "null", "value": 0 },
    { "name": "one", "value": 1 },
    { "name": "two", "value": 2 },
    { "name": "three", "value": 3 },
    { "name": "four", "value": 4 },
    { "name": "five", "value": 5 },
    { "name": "six", "value": 6 },
    { "name": "seven", "value": 7 },
    { "name": "eight", "value": 8 },
    { "name": "nine", "value": 9 },
];
var myMap2 = [
    { "name": "null" },
    { "name": "one" },
    { "name": "two" },
    { "name": "three" },
    { "name": "four" },
    { "name": "five" },
    { "name": "six" },
    { "name": "seven" },
    { "name": "eight" },
    { "name": "nine" },
];
for (var e = 0; e < myMap2.length; e++) {
    console.log(myMap2[e].name);
}
var sum = 0;
var allContents = fs.readFileSync('day01-2.txt', 'utf-8');
allContents.split(/\r?\n/).forEach(function (line) {
    //  could also work with a ordanary for loop
    //  let content = allContents.split(/\r?\n/);
    //  for ( let line of content ) {    
    console.log('line: ', line);
    var l = -1;
    var h = -1;
    for (var i = 0; i < line.length; i++) {
        var a = parseInt(line[i]);
        console.log(i, line.substr(i));
        for (var e = 0; e < myMap2.length; e++) {
            if (line.indexOf(myMap2[e].name, i) === i) {
                console.log("in " + line + "inex: " + i + " found" + myMap[e].name + " add to index " + (myMap[e].name.length));
                a = e;
                break;
            }
        }
        if (a >= 0 && a <= 9 && l == -1) {
            l = a;
        }
        if (a >= 0 && a <= 9 && l !== -1) {
            h = a;
        }
    }
    ;
    console.log(l * 10 + h);
    sum += l * 10 + h;
});
var message = 'Hello World';
console.log(sum);
//54868    is too low
