fs = require('fs')
data = fs.readFileSync(0, 'utf-8')
os = require('os')
nline = os.EOL

stacks = []

blocks = data.split(nline + nline)[0].split(nline).reverse()
size = blocks[0].split("  ").map((e) -> Number(e.trim())).reverse()[0]
blocks = blocks.slice(1)
data = data.split(nline + nline)[1]
    .replaceAll("move ", "")
    .replaceAll("from ", "")
    .replaceAll("to ", "")
    .split(nline).map(
        (f) -> f.split(" ").map((e) -> Number(e))
    )

for i in blocks
    i = i.replaceAll("    [", "[?] [").replaceAll("]    ", "] [?]").replaceAll("    ", "[?] ")
    stackCount = 0
    for j in i.split(" ")
        if !stacks[stackCount]
            stacks[stackCount] = []
        if j != "[?]"
            stacks[stackCount].push(j.replace("[", "").replace("]", ""))
        stackCount++

for x in data
    count = x[0]
    fr = x[1]
    to = x[2]

    for y in [0...count]
        val = stacks[fr - 1].pop()
        stacks[to - 1].push(val)

ans = ""

for z in stacks
    ans += z.pop()
    
console.log(ans)

