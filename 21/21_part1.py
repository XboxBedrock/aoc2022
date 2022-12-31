lines = [line.rstrip("\n") for line in open(0).readlines()]

for line in lines*len(lines):
    execify = line.replace(":", "=")
    try:
        exec(execify)
        print(root)
        break
    except:
        pass