import os
import sys
import numpy as np
from numba import jit, njit
from numba.typed import List
from numba import prange

print("l")

@njit(parallel=True, fastmath=True)#'void(int64, int64, int64[:], int64[:], int64[:], int64, int64[:], int64[:])')
def call(xmin, xmax, sensorsx, sensorsy, sensorsr, l, interval, bound):
    g_y = l
    for i in prange(len(sensorsx)):
        sensorx = sensorsx[i]
        sensory = sensorsy[i]
        dist = sensorsr[i]
        ydist = abs(sensory - g_y)
        if ydist >= 0:
            for j in prange(sensorx - dist + ydist , sensorx + dist - ydist + 1):
                if j-xmin <= bound:
                    interval[j-xmin] = 1
    if 0 in interval:
        for p in range(len(interval)):
            if interval[p] == 0:
                return (p+xmin) * 4000000 + g_y 
        

lines = open(0).readlines()
sensorsx = List()
sensorsy = List()
sensorsr = List()

xmin = sys.maxsize
xmax = 0

ymin = sys.maxsize
ymax = 0

def mdist(a, b, c, d):
    return abs(a-c) + abs(b-d)

for i in lines:
    i = i.rstrip('\n').lstrip("Sensor at ").replace("x=", "").replace(", y=", " ").split(": closest beacon is at ")
    sensor = [*map(int, i[0].split(" "))]
    beacon = [*map(int, i[1].split(" "))]
    dist = mdist(sensor[0], sensor[1], beacon[0], beacon[1])
    sensorsx.append(sensor[0])
    sensorsy.append(sensor[1])
    sensorsr.append(dist)
    
    if sensor[0] + dist > xmax:
        xmax = sensor[0] + dist
    
    if sensor[0] - dist < xmin:
        xmin = sensor[0] - dist
    
    if sensor[1] + dist > ymax:
        ymax = sensor[1] + dist
    
    if sensor[1] - dist < ymin:
        ymin = sensor[1] - dist
        
bound = 4000000 

xmin = max(0, xmin)
ymin = max(0, ymin)
ymax = min(ymax, bound)
xmax = min(ymax, bound)

print(ymax+1)


for l in range(ymin, ymax+1):
    if l%1000 == 0:
        print(l)
    interval = np.zeros(xmax+1-xmin)
    x = call(xmin, xmax, sensorsx, sensorsy, sensorsr, l, interval, bound)
    if x != None:
        print(x)
        break
count = 0


