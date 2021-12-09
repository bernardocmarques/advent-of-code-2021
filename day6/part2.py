from utils import *

with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]

fish_list = [int(e) for e in lines[0].split(",")]

school = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}

for fish in fish_list:
    school[fish] += 1


print(f"Inicial state: {school}")

for d in range(256):
    new_school = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}
    for i in range(9):
        prev = int(school[i])
        if i > 0:
            new_school[i-1] += prev

        if i == 0:
            new_school[8] = prev
            new_school[6] += prev
    school = new_school



    print(f"After {str(d+1).zfill(2)} days")

c = 0
for i in range(9):
    c += school[i]
print(c)