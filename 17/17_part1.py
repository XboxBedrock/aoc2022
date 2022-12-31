tape = list(input())
tape_fix = tape.copy()
tapelen = len(tape)
pattern_order = [0, 1, 2, 3, 4]

def get_next_move():
    global tape
    val = tape.pop(0)
    if len(tape) == 1:
        tape.extend(tape_fix.copy())
    
    return val

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

for i in range(2022):
    shape = get_next_pattern()
    shapes[shape].move()
    #print(heights)

res = 0

#l = [*map(lambda x: ''.join(map(str,x)).replace('0',".").replace('1','#'), heights)]
#l.reverse()
#print('\n'.join(l))

for i in heights:
    if i != 0:
        res += 1

print (res-1)
