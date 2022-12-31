

totsnd = 0
maxy = 0
miny = 0
maxx = 0

inp = open(0).read().split("\n")

def step(val1, val2):
    if val1 <= val2:
        return 1
    else:
        return -1

for i in inp:
    subsplt = i.split(" -> ")
    for j in subsplt:
        evenmore = j.split(",")
        x = int(evenmore[0])
        y = int(evenmore[1])
        if miny == 0:
            miny = y
        elif y < miny:
            miny = y
        
        if x > maxx: maxx = x
        if y > maxy: maxy = y

zecave = [[0 for x in range(1000)] for z in range(500)]

for i in inp:
    subsplt = i.split(" -> ")
    tot = []
    for j in subsplt:
        evenmore = j.split(",")
        x = int(evenmore[0])
        y = int(evenmore[1])
        tot.append((x, y))
    for j in range(len(tot) - 1):
        a = tot[j]
        b = tot[j + 1]
        if a[0] == b[0]:
            for k in range(a[1], b[1] + step(a[1], b[1]), step(a[1], b[1])):
                zecave[k][a[0]] = 1
        if a[1] == b[1]:
            for k in range(a[0], b[0] + step(a[0], b[0]), step(a[0], b[0])):
                zecave[a[1]][k] = 1

floor = maxy + 2

while True:
    totsnd += 1
    cross = 500
    down = 0
    abort = False
    while True:
        if down >= floor-1:
            zecave[down][cross] = 2
            break
        elif (zecave[1][499] == 2 and zecave[1][501] == 2) and zecave[1][501] == 2:
            abort = True
            break
        elif zecave[down + 1][cross] == 0:
            down += 1
        elif zecave[down + 1][cross - 1] == 0:
            down += 1
            cross -= 1
        elif zecave[down + 1][cross + 1] == 0:
            down += 1
            cross += 1
        else:
            zecave[down][cross] = 2
            break
    
    if abort:
        break
    

#print('\n'.join(map(str, zecave)))
print(totsnd)

