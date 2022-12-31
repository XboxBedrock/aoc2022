from collections import deque
from operator import itemgetter

def find_exposed_sides(coords):
    exposed_sides = 0
    for coord in coords:
        exposed_sides += 6
        x, y, z = coord
        if (x, y+1, z) in coords: exposed_sides -= 1
        if (x, y-1, z) in coords: exposed_sides -= 1
        if (x+1, y, z) in coords: exposed_sides -= 1
        if (x-1, y, z) in coords: exposed_sides -= 1
        if (x, y, z+1) in coords: exposed_sides -= 1
        if (x, y, z-1) in coords: exposed_sides -= 1

    return exposed_sides


lines = [*map(lambda x: tuple(map(int, x.split(","))), open(0).read().split("\n"))]

maxx = max(lines, key=itemgetter(0))[0] + 2
maxz = max(lines, key=itemgetter(2))[2] + 2
maxy = max(lines, key=itemgetter(1))[1] + 2
minx = min(lines, key=itemgetter(0))[0] - 1
miny = min(lines, key=itemgetter(1))[1] - 1
minz = min(lines, key=itemgetter(2))[2] - 1

dfs = deque([(minx, miny, minz)])
visited = set()
sides = 0

while dfs:
    x, y, z = dfs.pop()
    if (x, y, z) not in visited:
        visited.add((x,y,z))
        
        for next_x, next_y, next_z in [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]:
            if (minx <= next_x <= maxx and miny <= next_y <= maxy and minz <= next_z <= maxz):
                if (next_x, next_y, next_z) in lines:
                    sides += 1
                else:
                    dfs.append((next_x, next_y, next_z))
print(sides)