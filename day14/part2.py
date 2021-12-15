from utils import *
import re,datetime

with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]
start = datetime.datetime.now()

polymer = lines[0]

rules = []
for line in lines[2:]:
    rules.append(tuple(line.split(" -> ")))

# new_rules = {e[0]: e[0] for e in rules}
new_rules = {e[0]: e[0][0] + e[1] + e[0][1] for e in rules}
# rules = {e[0]: e[1] for e in rules}
rules = {e[0]: e[0][0] + e[1] + e[0][1] for e in rules}
print(rules)

step = 1
steps_to_add = 1
while step < 5:
    for k, v in new_rules.items():
        n = apply_rules(v, rules)
        new_rules[k] = n

    step += steps_to_add
    print(f"After step {step}:")

step = 0
while step < 3:
    for k, v in rules.items():
        n = apply_rules(v, new_rules)
        rules[k] = n

    step += steps_to_add
    print(f"After step {step}:")


for k, v in new_rules.items():
    print(f"{k}: {v}")
print()
for k, v in rules.items():
    print(f"{k}: {v}")


for step in range(2):
    polymer = apply_rules(polymer, rules)
    print(f"After step {step+1}:")


char_count = {}
for char in polymer:
    if char not in char_count.keys():
        char_count[char] = 1
    else:
        char_count[char] += 1

char_count = sorted(list(char_count.items()), key=lambda x: x[1])

print((char_count[-1][1] - char_count[0][1]))

print(datetime.datetime.now() - start)