from utils import *
import datetime

# usar uma ideia de tree e links


with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]
start = datetime.datetime.now()

polymer = lines[0]

polymer_pairs = []

for i in range(len(polymer)-1):
    polymer_pairs.append(polymer[i:i+2])

rules = []
for line in lines[2:]:
    rules.append(tuple(line.split(" -> ")))

new_rules = {e[0]: e[0][0] + e[1] + e[0][1] for e in rules}
rules = {e[0]: e[0][0] + e[1] + e[0][1] for e in rules}
print(rules)

step = 1
steps_to_add = 1
while step < 16:
    next_rules = {}
    for pair in polymer_pairs:
        v = new_rules[pair]
        new_rules[pair] = apply_rules(v, rules)
    rules = {k: v for k, v in new_rules.items()}

    print(f"After step {step}:")
    step += step

for k, v in new_rules.items():
    print(f"{k}: {v}")
print()
# for k, v in rules.items():
#     print(f"{k}: {v}")

polymer = apply_rules(polymer, new_rules)

char_count = {}
for char in polymer:
    if char not in char_count.keys():
        char_count[char] = 1
    else:
        char_count[char] += 1

char_count = sorted(list(char_count.items()), key=lambda x: x[1])

print((char_count[-1][1] - char_count[0][1]))

print(datetime.datetime.now() - start)
