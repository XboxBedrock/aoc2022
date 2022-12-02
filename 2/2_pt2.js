const charCodeSubX = (a) => a.charCodeAt(0)-'X'.charCodeAt(0)+1;
const charCodeSubA = (a) => a.charCodeAt(0)-'A'.charCodeAt(0)+1;

const fs = require('fs');
const data = fs.readFileSync(0, 'utf-8');
let count = 0;

function win(a, b) {
    let total = (b-1)*3
    if (b == 3) {
        if (a == 1) {
            total += 2
        }
        if (a == 2) {
            total += 3
        }
        if (a == 3) {
            total += 1
        }
    }
    if ( b == 2 ) total += a
    if ( b == 1)  {
        if (a == 1) {
            total += 3
        }
        if (a == 2) {
            total += 1
        }
        if (a == 3) {
            total += 2
        }
    }
    return total
}

let res = data.split("\n").map((e) => {
    e = e.trim().split(" ")
    let a = charCodeSubA(e[0])
    let b = charCodeSubX(e[1])
    return win(a, b)
}).reduce((a, b) => a+b)

console.log(res)