from collections import deque

#inspired by some odd mix of reddit comments
#total rewrite from one using floyd-warshall and bitmasking in order to solve
#heavy inspiration from https://github.com/juanplopes/advent-of-code-2022/blob/main/day16.py

lines = open(0).readlines()

data = {}

tunnels = {}
flow = {}
bitmasked = {}
time = {}

f = 0

for i in lines:
    i = i.rstrip("\n").replace("Valve ", "").replace("has flow rate=", "").replace(" tunnels lead to valves ", "").replace(" tunnel leads to valve ", "").split(";")
    k = i[0].split(" ")[0]
    v = (int(i[0].split(" ")[1]), i[1].split(", "))
    data[k] = v
    tunnels[k] = set(v[1])
    if v[0] != 0:
        flow[k] = v[0]
        bitmasked[k] = 1<<f
    f+=1

for x in tunnels:
    ydict = {}
    for y in tunnels:
        if y in tunnels[x]:
            ydict[y] = 1 
        else: ydict[y] = float('+inf')
    time[x] = ydict

for x in time:
    for y in time:
        for z in time:
            time[y][z] = min(time[y][z], time[y][x]+time[x][z])
            
def doit(tovis, mins, state, flowrate, correct):
    correct[state] = max(flowrate, correct.get(state, 0))
    
    for tun in flow:
        newmins = mins - time[tovis][tun] - 1
        if bitmasked[tun] & state or newmins <= 0:
            continue
        doit(tun, newmins, state | bitmasked[tun], flowrate + newmins * flow[tun], correct)
    
    return correct

p2 = doit('AA', 26, 0, 0, {})

findfrom = []

for key, val in p2.items():
    for seckey, secval in p2.items():
        if not key & seckey:
            findfrom.append(val+secval)

print(max(findfrom ))
    
    
    