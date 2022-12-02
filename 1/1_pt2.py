with open("1.in", "r") as f:
   lines = f.readlines()
   accum = 0
   greatest = []
   for i in lines:
       if i == "\n":
           greatest.append(accum)
           accum = 0
       else:
           accum += int(i.rstrip('\n'))
   greatest.sort()
   print(sum(greatest[-3:]))