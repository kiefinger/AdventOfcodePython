import * as fs from 'fs';

let sum = 0;
var maxValues =  { "red": 12, "blue": 14, "green": 13 }

const allContents = fs.readFileSync('day02-1.txt', 'utf-8');

allContents.split(/\r?\n/).forEach((line) => {
    var game = parseInt(line.substring(5));
    var invalid =  { "red": false, "blue": false, "green": false }
    var startIndex = line.indexOf(':');
    line.substr(startIndex+1).split(/;/).forEach( ( bag) => {
        bag.split(/,/).forEach( (item) => {
            var anz = item.trim().split(/ /);
            if ( anz[0] > maxValues[anz[1]] ) {
                invalid[anz[1]] = true;
            }
        });
    });
    if ( !invalid["red"]   &&  !invalid["green"]   &&  !invalid["blue"]) {        
        sum += game;
    }

});

console.log ("Part1: sum: " , sum );

sum = 0;
allContents.split(/\r?\n/).forEach((line) => {
    var game = parseInt(line.substring(5));
    var colorset = { "red": 0, "blue": 0, "green": 0 }
    var startIndex = line.indexOf(':');
    line.substr(startIndex+1).split(/;/).forEach( ( bag) => {
        bag.split(/,/).forEach( (item) => {
            var anz = item.trim().split(/ /);
            colorset[anz[1]] = Math.max( colorset[anz[1]] , Number(anz[0]) );
        });
    });
    var pow = colorset["red"] * colorset["blue"] * colorset["green"] ;
    sum += pow;
});

console.log ("Part2: sum: " , sum );