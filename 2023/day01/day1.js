"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
var content = [];
var sum = 0;
var allContents = fs.readFileSync('day01-1.txt', 'utf-8');
allContents.split(/\r?\n/).forEach(function (line) {
    console.log('line: ', line);
    var l = -1;
    var h = -1;
    for (var i = 0; i < line.length; i++) {
        var a = parseInt(line.charAt(i));
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
    content.push(line);
});
var message = 'Hello World';
console.log(content);
console.log(sum);
