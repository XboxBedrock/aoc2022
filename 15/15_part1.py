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

g_y = 2000000

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
    
for i in range(len(sensorsx)):
    sensor = [sensorsx[i], sensorsy[i]]
    dist = sensorsr[i]
    ydist = abs(sensor[1] - g_y)
    
    for j in range(sensor[0] - dist + ydist , sensor[0] + dist - ydist + 1):
        if [j, g_y] not in beacons:
            interval[j-xmin] = 1
        
        
        
count = 0


print(sum(interval ))


