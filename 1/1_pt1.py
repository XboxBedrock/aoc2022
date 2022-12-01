with open("1.in", "r") as f:
   lines = f.readlines()
   accum = 0
   greatest = 0
   for i in lines:
       if i == "\n":
           if (accum > greatest): greatest = accum
           accum = 0
       else:
           accum += int(i.rstrip('\n'))
   print(greatest)