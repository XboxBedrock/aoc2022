
lines = open(0).readlines()

mixymix = []

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    def mix(self, sz):
        i = self.val % (sz - 1)
        if i:
            p = self
            
            for k in range(i):
                p = p.next
            
            self.prev.attach(self.next)
            n = p.next
            p.attach(self)
            self.attach(n)

    def attach(self, n):
        self.next = n
        n.prev = self
    
    def find(self, num, sz):
        num = num % sz
        e = self
        for i in range(num):
            e = e.next
        return e.val
                

for i in lines:
    mixymix.append(Node(int(i.rstrip('\n'))))
    
thezero = None

for i in range(0, len(mixymix)-1):
    if mixymix[i].val == 0:
        thezero = mixymix[i]
    mixymix[i].next = mixymix[i+1]
    mixymix[i].prev = mixymix[i-1]

mixymix[-1].next = mixymix[0]
mixymix[-1].prev = mixymix[-2]

e = mixymix[0]



for x in range(len(mixymix)):
    mixymix[x].mix(len(mixymix))

res = thezero.find(1000, len(mixymix)) + thezero.find(2000, len(mixymix)) + thezero.find(3000, len(mixymix))
print(res)


