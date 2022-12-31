import json

def tlist(e):
    if type(e) != list:
        return [e]
    return e

def compare(l, r):
    minl = min(len(l), len(r))
    if len(l) == 1 and len(r) == 1:
        if type(l[0]) == int and type(r[0]) == int:
            if (l[0] < r[0]): return True
            if (l[0] > r[0]): return False
            else: return "heh"
    for i in range(minl):
        a = l.pop(0)
        b = r.pop(0)
        c = compare(tlist(a), tlist(b))
        if c != "heh":
                return c
    
    if l == [] and r != []: return True
    elif r == [] and l != []: return False
    else: return "heh"
    

dat = open(0).read().split("\n\n")
idx = 1
tot = 0
for i in dat:
    l = json.loads(i.split()[0])
    r = json.loads(i.split()[1])
    c = compare(l, r)
    
    print(idx, c)
    
    if (c == True): 
        #print(idx)
        tot += idx
    idx += 1
    
print(tot)