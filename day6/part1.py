from utils import *

with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]

school = [int(e) for e in lines[0].split(",")]

print(f"Inicial state: {school}")
for d in range(80):
    for i in range(len(school)):
        school[i] -= 1
        if school[i] == -1:
            school[i] = 6
            school.append(8)
    print(f"After {str(d+1).zfill(2)} days: {school}")

print(len(school))