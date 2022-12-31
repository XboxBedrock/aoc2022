lines = [line.rstrip("\n") for line in open(0).readlines()]
#bois imaginary number time



for line in lines*len(lines):
    humn = 1j
    execify = line.replace(":", "=")
    splitline = line.replace(":", "").split()
    if splitline[0] == "root":
        execify  = f'{splitline[0]} = ( {splitline[3]} - {splitline[1]}.real ) / {splitline[1]}.imag '
    try:
        exec(execify)
        #ignore the decimal when you submit
        print(int(root))
        break
    except:
        pass