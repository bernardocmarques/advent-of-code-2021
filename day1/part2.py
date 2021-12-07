with open("input.txt", "r") as input_file:
    ms = [int(e) for e in input_file.readlines()]

win = []
c = 0
s = len(ms)
for i in range(s):
    if s > i + 2:
        win.append(ms[i] + ms[i + 1] + ms[i + 2])
    elif s > i + 1:
        win.append(ms[i] + ms[i + 1])
    else:
        win.append(ms[i])

last = win[0]
count = 0
for m in win[1:]:
    count += 1 if m > last else 0
    last = m

print(count)

