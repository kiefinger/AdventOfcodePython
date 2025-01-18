import * as fs from 'fs';


let myMap = [] =  [
    { "name": "null", "value" :  0},
    { "name": "one", "value" :  1},
    { "name": "two", "value" :  2},
    { "name": "three", "value" :  3},
    { "name": "four", "value" :  4},
    { "name": "five", "value" :  5},
    { "name": "six", "value" :  6},
    { "name": "seven", "value" :  7},
    { "name": "eight", "value" :  8},
    { "name": "nine", "value" :  9},
];

let myMap2 = [] =  [
    { "name": "null"},
    { "name": "one"},
    { "name": "two"},
    { "name": "three"},
    { "name": "four"},
    { "name": "five"},
    { "name": "six"},
    { "name": "seven"},
    { "name": "eight"},
    { "name": "nine"},
];
for ( let e = 0; e < myMap2.length; e++ ) {
    console.log ( myMap2[e].name);
}

let sum = 0;
const allContents = fs.readFileSync('day01-2.txt', 'utf-8');
allContents.split(/\r?\n/).forEach((line) => {

//  could also work with a ordanary for loop
//  let content = allContents.split(/\r?\n/);
//  for ( let line of content ) {    

    console.log('line: ', line);

    let l = -1;
    let h = -1;
    for (let i = 0; i < line.length; i++) {
            let a = parseInt(line[i]);
            for ( let e = 0; e < myMap2.length; e++ ) {
                if ( line.indexOf ( myMap2[e].name, i ) === i) {
                    a = e
                    break;
                }
            }
            if ( a>=0 && a <= 9 && l==-1 ) {
                l = a;
            }
            if ( a>=0 && a <= 9 && l!==-1 ) {
                h = a;
            }
        };
    sum += l*10+h;
    });

console.log(sum);
