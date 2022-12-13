
from queue import Queue


class Node:
    def __init__(self, pos, height):
        self.pos = pos
        self.height = height
        self.paths = []
    def add_path(self, new_path):
        if new_path not in self.paths:
            self.paths.append(new_path)
    def generate_paths(self, map_c):
        my_x, my_y = self.pos
        p_paths = [(my_x, my_y + 1), (my_x, my_y - 1), (my_x - 1, my_y), (my_x + 1, my_y)]
        for p in p_paths:
            if p in map_c:
                if map_c[p].height <= self.height + 1:
                    self.paths.append(p)
                    
                    
def get_shortest_path(hmap, s, g):
    # BFS https://www.redblobgames.com/pathfinding/a-star/introduction.html

    frontier = Queue()
    frontier.put(s)
    came_from = dict()
    came_from[s] = None
    while not frontier.empty():
        current_position = frontier.get()

        if current_position == g:
            break

        for next_position in hmap[current_position].paths:
            if next_position not in came_from:
                frontier.put(next_position)
                came_from[next_position] = current_position
    current_position = g
    path = []
    while current_position != s:
        path.append(current_position)
        try:
            current_position = came_from[current_position]
        except KeyError as e:
            return False, came_from
    return True, len(path)

def intIfy(x):
    return ord(x) - ord('a')

def f(_):
    return False

dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]


lines = open(0).read()
arr = [*map(lambda x: list(x) ,lines.split('\n'))]

mapofh = {}

tx = 0
ty = 0
pos = (0, 0)

posa = []

for i in arr:
    for j in i:
        h = intIfy(j)
        if (j == 'a'): 
            posa.append((ty, tx))
        if (j == 'E'): 
            pos = (ty, tx)
            h = 25
        mapofh[(ty, tx)] = Node((ty, tx), h)
        ty += 1
    tx += 1
    ty = 0

for i in mapofh:
    mapofh[i].generate_paths(mapofh)

import sys 
least = sys.maxsize

for i in posa:
    c = get_shortest_path(mapofh, i, pos)
    if (c[0] and c[1] < least): least = c[1]
print(least)


