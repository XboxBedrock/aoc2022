const charCodeSubX = (a) => a.charCodeAt(0)-'X'.charCodeAt(0)+1;
const charCodeSubA = (a) => a.charCodeAt(0)-'A'.charCodeAt(0)+1;

const fs = require('fs');
const data = fs.readFileSync(0, 'utf-8');
let count = 0;

function win(a, b) {
    if (a == 1 && b == 2) return 6
    if (a == 2 && b == 3) return 6
    if (a == 3 && b == 1) return 6
    if (a == b) return 3
    return 0
}

let res = data.split("\n").map((e) => {
    e = e.trim().split(" ")
    let a = charCodeSubA(e[0])
    let b = charCodeSubX(e[1])
    return win(a, b) + b
}).reduce((a, b) => a+b)

console.log(res)