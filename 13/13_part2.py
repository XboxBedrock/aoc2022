import json
from functools import cmp_to_key

def tlist(e):
    if type(e) != list:
        return [e]
    return e

def compare(l, r):
    minl = min(len(l), len(r))
    if len(l) == 1 and len(r) == 1:
        if type(l[0]) == int and type(r[0]) == int:
            if (l[0] < r[0]): return 1
            if (l[0] > r[0]): return -1
            else: return 0
    
    lpop = l.copy()
    rpop = r.copy()
    for i in range(minl):
        a = lpop.pop(0)
        b = rpop.pop(0)
        c = compare(tlist(a), tlist(b))
        if c != 0:
                return c
    
    if lpop == [] and rpop != []: return 1
    elif rpop == [] and lpop != []: return -1
    else: return 0
    

dat = open(0).read().split("\n\n")
tdat = [[[2]], [[6]]]
for i in dat:
    l = json.loads(i.split()[0])
    r = json.loads(i.split()[1])
    tdat.append(l)
    tdat.append(r)

tdat.sort(key=cmp_to_key(compare), reverse=True)
    
print((tdat.index([[2]])+1)*(tdat.index([[6]])+1))