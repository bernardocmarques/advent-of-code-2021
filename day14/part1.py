from utils import *
import re, datetime

with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]

polymer = lines[0]

start = datetime.datetime.now()

rules = []
for line in lines[2:]:
    rules.append(tuple(line.split(" -> ")))

for step in range(20):
    polymer = apply_rules_p1(polymer, rules)

    print(f"After step {step+1}: {polymer}")

char_count = {}
for char in polymer:
    if char not in char_count.keys():
        char_count[char] = 1
    else:
        char_count[char] += 1

char_count = sorted(list(char_count.items()), key=lambda x: x[1])

print((char_count[-1][1] - char_count[0][1]))

print(datetime.datetime.now() - start)