import math

nums = open(0).read().split('\n')

dmap = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    "=": -2,
    -2: "=",
    -1: "-",
    0: "0",
    1: "1",
    2: "2"
}
tsum = 0
for i in nums:
    l = list(i)
    l.reverse()
    power = 0
    tot = 0
    for j in l:
        tot += 5**power * dmap[j]
        power += 1
    tsum += tot
    
def to_snafu(num):
    snafu = ""
    while num != 0:
        snafu += dmap[(num + 2)%5 - 2]
        num = (num - ((num+2)%5 - 2)) // 5
        
    return snafu[::-1]

print(to_snafu(tsum))