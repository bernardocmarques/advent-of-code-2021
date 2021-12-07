with open("input.txt", "r") as input_file:
    cmds = [e.replace("\n", "") for e in input_file.readlines()]


h = 0
d = 0

for cmd in cmds:

    cmd_sliced = cmd.split(" ")
    c = cmd_sliced[0]
    x = int(cmd_sliced[1])

    if c == "forward":
        h += x
    elif c == "down":
        d += x
    elif c == "up":
        d -= x

print(h, d, h*d)



