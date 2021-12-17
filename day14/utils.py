import re


def apply_rules(polymer, rules):
    to_add = []
    for pat, n in rules.items():
        found = True
        cut = 0
        while found:
            index = polymer[cut:].find(pat) + 1
            if index:
                to_add.append((n, index + cut))
                cut += index
            else:
                found = False

    to_add.sort(key=lambda x: x[1], reverse=True)
    for item, index in to_add:
        polymer = polymer[:index-1] + item + polymer[index+1:]
    return polymer


def apply_rules_p1(polymer, rules):
    to_add = []
    for rule in rules:
        found = True
        cut = 0
        while found:
            index = polymer[cut:].find(rule[0]) + 1
            if index:
                to_add.append((rule[1], index + cut))
                cut += index
            else:
                found = False

    to_add.sort(key=lambda x: x[1], reverse=True)
    for item, index in to_add:
        polymer = polymer[:index] + item + polymer[index:]
    return polymer


def apply_rules_p1_new(polymer, rules):
    i = 0
    while i < len(polymer):
        pair = polymer[i:i+2]
        if len(pair) != 2:
            break
        # print(pair)
        n = rules[pair]
        polymer = polymer[:i+1] + n + polymer[i+1:]
        i += len(n)+1

    return polymer