from collections import deque

#inspired by some odd mix of reddit comments

lines = open(0).readlines()

data = {}

for i in lines:
    i = i.rstrip("\n").replace("Valve ", "").replace("has flow rate=", "").replace(" tunnels lead to valves ", "").replace(" tunnel leads to valve ", "").split(";")
    k = i[0].split(" ")[0]
    v = (int(i[0].split(" ")[1]), i[1].split(", "))
    data[k] = v

queue = deque([("AA", 0, 0, ())])
visited = set()
pressure = 0

last = 0

while queue:
    val = queue.popleft()
    passed = val[2]
    accum = val[1]
    opened = val[3]
    valve = val[0]
    
    if passed == 30:
        pressure = max(pressure, accum)
        last = pressure
        continue

    if (opened, valve) in visited:
        continue
    
    visited.add((opened, valve))
    
    tempaccum = accum
    for i in opened:
        tempaccum += data[i][0]
    
    if data[valve][0] != 0:
        if valve not in opened:
            queue.append((valve, tempaccum, passed+1, tuple(list(opened)+[valve]))) 
    
    for i in data[valve][1]:
        queue.append((i, tempaccum, passed+1, opened))
        
print(last)