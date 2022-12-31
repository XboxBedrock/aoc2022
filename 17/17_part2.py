import math
from fractions import gcd

tape = list(input())
tape_fix = tape.copy()
tapelen = len(tape)
pattern_order = [0, 1, 2, 3, 4]
tapeidx = 0

def get_next_move():
    global tape
    global tapeidx
    val = tape.pop(0)
    tapeidx += 1
    if len(tape) == 1:
        tape.extend(tape_fix.copy())
    
    return val

def get_next_move_idx():
    global tapeidx
    return tapeidx % tapelen

def lcm(x, y):
    return x * y // gcd(x, y)

def get_next_pattern():
    global pattern_order
    val = pattern_order.pop(0)
    pattern_order.append(val)
    return val


def set_bit(v, index, x):
    mask = 1 << index   
    v &= ~mask         
    if x:
        v |= mask         
    return v 

def get_bit(v, pos):
    return (v >> pos) & 1

shapes_model = [
    [
        [1,1,1,1]
    ],
    [
        [0,1,0],
        [1,1,1],
        [0,1,0]
    ],
    [
        [0,0,1],
        [0,0,1],
        [1,1,1]
    ],
    [
        [1],
        [1],
        [1],
        [1]
    ],
    [
        [1,1],
        [1,1]
    ]
]

reps = 6

row = [0, 0, 0, 0, 0, 0, 0]


heights = [127]

currentH = 0

class Rock: 
    def __init__(self, shape):
        #print(shape)
        self.h = len(shape)
        self.w = max([len(x) for x in shape])
        self.x = 2
        self.y = 4
        self.shape = shape

    def move(self):
        self.x = 2
        global currentH
        #print("H", currentH)
        
        self.y = currentH + 4
        #print("Y", self.y)
        #print(self.y)
        global get_next_move
        while True:
            self.moveDir(get_next_move())
            if self.moveDown() == False:
                break
        for i in range(self.h):
            for j in range(self.w):
                if self.shape[i][j] == 0:
                    pass
                else:
                    col = j + self.x 
                    heights[self.y + (self.h-1-i)] = set_bit(heights[self.y + (self.h-1-i)], col, 1)
                    currentH = max(currentH, self.y + (self.h-1-i))
    
    def moveDown(self):
        if self.didCol(self.x, 1):
            return False
        self.y -= 1
    
    def didCol(self, dire, hoff):
        global heights
        posX = dire
        posH = self.y-hoff
        #print(self.h, self.w)
        #print(heights)
        for i in range(self.h):
            for j in range(self.w):
                if self.shape[i][j] == 0:
                    pass
                else:
                    #print("E", j)
                    col = j + posX
                    #print(self.x)
                    #print(posH + self.h-1-i)
                    #print(len(heights))
                    
                    
                    
                    if posH + self.h-1-i > len(heights)-1:
                        
                        heights.extend([0 for x in range(abs((posH + self.h-i)-len(heights)))])
                    
                    if 1 == get_bit(heights[posH + self.h-1-i], col):
                        return True
                        
        return False
    
    def moveDir(self, dire):
        #print(dire)
        #print(self.y)
        if dire == '<':
            if self.x-1 >= 0 and not self.didCol(self.x-1, 0):
               self.x -= 1 
        elif dire == '>':
            if self.x+self.w <= 6 and not self.didCol(self.x+1, 0):
                #print("e", self.x)
                self.x += 1

        
    def moveDirFake(self, off):
        global tape
        #print(dir)
        #print(self.y)
        dire = tape[0]
        if dir == '<':
            if self.x-1 >= 0 and not self.didCol(self.x-1, off):
               return self.x-1
        elif dire == '>':
            if self.x+self.w <= 6 and not self.didCol(self.x+1, off):
               return self.x+1
        return self.x
    
    

shapes = [Rock(x) for x in shapes_model]

plen = 2022
rterm = lcm(tapelen, len(shapes))


terms = plen/rterm

state_dict = {}


cycles = {}

f = 0

totrocks = 1000000000000

def getProfile():
    global get_bit
    global heights
    th = [*filter(lambda x: x != 0, heights)]
    n = [0, 0, 0, 0, 0, 0 ,0]
    h = 0
    for p in th:
        for q in range(7):
            ist = get_bit(p, q)
            if ist == 1:
                n[q] = max(n[q], h)
        h += 1
    min_n = min(n)
    n = tuple(map(lambda x: x - min_n, n))
    return n

skipped = 0

dur = 0

while f < totrocks:
    old = currentH
    shapeidx = get_next_move_idx()
    shape = get_next_pattern()
    shapes[shape].move()
    k = (currentH - old, shape, getProfile())
    v = (f, currentH)
    if k in cycles:
        #don't ask me why this is 300, i did a lot of trial and error
        if dur > 300:
            count, yy = cycles[k]
            deltaH = currentH - yy
            deltaN = f - count
            
            steps = (totrocks - f) // deltaN
            skipped += deltaH * steps
            f += deltaN * steps
        dur += 1
    else:
        cycles[k] = v
        
        
        
    
    f += 1


    

print(currentH + skipped)

res = 0
