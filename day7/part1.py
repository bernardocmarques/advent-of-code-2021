with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]

crabs = [int(e) for e in lines[0].split(",")]

options = list(range(max(crabs)))

min_cost = -1
min_pos = -1

while len(options) > 1:
    option = options.pop()
    cost = 0
    for crab in crabs:
        cost += abs(option - crab)
        if min_cost != -1 and cost > min_cost:
            cost = -1
            break
    if cost != -1:
        min_cost = cost
        min_pos = option

print(min_pos, min_cost)