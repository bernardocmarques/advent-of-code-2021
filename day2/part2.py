with open("input.txt", "r") as input_file:
    cmds = [e.replace("\n", "") for e in input_file.readlines()]


h = 0
d = 0
aim = 0

for cmd in cmds:

    cmd_sliced = cmd.split(" ")
    c = cmd_sliced[0]
    x = int(cmd_sliced[1])

    if c == "forward":
        h += x
        d += aim * x
    elif c == "down":
        aim += x
    elif c == "up":
        aim -= x

print(h, d, h*d)



