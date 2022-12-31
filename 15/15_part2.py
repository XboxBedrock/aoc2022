import os
import sys

lines = open(0).readlines()
sensorsx = []
sensorsy = []
sensorsr = []
beacons= []

xmin = sys.maxsize
xmax = 0

def mdist(a, b, c, d):
    return abs(a-c) + abs(b-d)

maxaxis = 4000000

for i in lines:
    i = i.rstrip('\n').lstrip("Sensor at ").replace("x=", "").replace(", y=", " ").split(": closest beacon is at ")
    sensor = [*map(int, i[0].split(" "))]
    beacon = [*map(int, i[1].split(" "))]
    dist = mdist(sensor[0], sensor[1], beacon[0], beacon[1])
    sensorsx.append(sensor[0])
    sensorsy.append(sensor[1])
    sensorsr.append(dist)
    beacons.append(beacon)
    
    if sensor[0] + dist > xmax:
        xmax = sensor[0] + dist
    
    if sensor[0] - dist < xmin:
        xmin = sensor[0] - dist
        
interval = [0 for x in range(xmin, xmax)]

def not_chillin(x, y):
    for i in range(len(sensorsx)):
        senx = sensorsx[i]
        seny = sensorsy[i]
        dist = sensorsr[i]
        if mdist(senx, seny, x, y) <= dist:
            return False
    return True
    
for i in range(len(sensorsx)):
    senx = sensorsx[i]
    seny = sensorsy[i]
    dist = sensorsr[i]
    for xrep in [-1, 1]:
        for yrep in [-1, 1]:
            for j in range(0, dist+2):
                ydist = dist + 1 - j
                x = senx + (j * xrep)
                y = seny + (ydist * yrep)
                if y >= 0 and x >= 0 and y <= maxaxis and x <= maxaxis and not_chillin(x, y):
                    print(x, y)
                    print(x*4000000+y)
                    sys.exit(0)

