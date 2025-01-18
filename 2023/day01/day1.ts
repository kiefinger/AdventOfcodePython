import * as fs from 'fs';


let content: string[] = [];
let sum = 0;
const allContents = fs.readFileSync('day01-1.txt', 'utf-8');
allContents.split(/\r?\n/).forEach((line) => {
  console.log('line: ', line);

    let l = -1;
    let h = -1;
    for (let i = 0; i < line.length; i++) {
            let a = parseInt(line.charAt(i));
            if ( a>=0 && a <= 9 && l==-1 ) {
                l = a;
            }
            if ( a>=0 && a <= 9 && l!==-1 ) {
                h = a;
            }
        };
    console.log (l*10+h);
    sum += l*10+h;
    content.push(line)
    });

let message: string = 'Hello World';
console.log(content);
console.log(sum);