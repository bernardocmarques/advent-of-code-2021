from utils import *
import copy

with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]
lines = ["be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"]
usp_list = [e.split(" | ")[0] for e in lines]
fdos_list = [e.split(" | ")[1] for e in lines]

all_list = [e for e in usp_list + fdos_list]

c = 0

original = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'],
    1: ['c', 'f'],
    2: ['a', 'c', 'd', 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'],
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}

decoder = {
    'a': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'b': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'c': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'd': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'e': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'f': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'g': ['a', 'b', 'c', 'd', 'e', 'f', 'g']
}

print(all_list)
for w in all_list:
    for output in w.split(" "):
        s = len(output)

        # if s == 2:  # 1
        #     for letter in original[1]:
        #         decoder[letter] = [e for e in decoder[letter] if e in output]
        # if s == 4:  # 4
        #     for letter in original[4]:
        #         decoder[letter] = [e for e in decoder[letter] if e in output]
        # if s == 3:  # 7
        #     for letter in original[7]:
        #         decoder[letter] = [e for e in decoder[letter] if e in output]

        if s == 2:  # 1
            for letter in output:
                decoder[letter] = [e for e in decoder[letter] if e in original[1]]
        if s == 4:  # 4
            for letter in output:
                decoder[letter] = [e for e in decoder[letter] if e in original[4]]
        if s == 3:  # 7
            for letter in output:
                decoder[letter] = [e for e in decoder[letter] if e in original[7]]
print()
print()
for k, v in decoder.items():
    print(f"{k}: {v}")

changed = 1
g_list = []

while changed:
    changed = 0

    min_s = 8
    group_to_remove = []

    for _, g in decoder.items():
        s = len(g)

        if s < min_s and g not in g_list:
            g_list.append([e for e in g])
            group_to_remove = [e for e in g]
            min_s = s
            break

    for letter in decoder:
        s = len(decoder[letter])
        if s > min_s:
            prev = [e for e in decoder[letter]]

            decoder[letter] = [e for e in decoder[letter] if e not in group_to_remove]
        for _, y in decoder.items():
            if len(y) > 2:
                changed = 1
                break

print()
print("Depois de reduzir")
for k, v in decoder.items():
    print(f"{k}: {v}")

o_decoder = copy.deepcopy(decoder)
choice_mask = [0, 0, 0]

print()
print()
loop = 1
while loop:
    decoder = copy.deepcopy(o_decoder)

    loop = 0
    i = 0
    print(f'mask = {choice_mask}')
    for letter in decoder:
        if len(decoder[letter]) == 1:
            choice = decoder[letter][0]
        else:
            choice = o_decoder[letter][choice_mask[i]]
            i += 1
        decoder[letter] = [choice]
        for l2 in decoder:
            if decoder[letter] == decoder[l2]:
                continue

            if choice in decoder[l2]:
                decoder[l2].remove(choice)

    print()
    print("decoder:")
    for k, v in decoder.items():
        print(f"{k}: {v}")

    print()
    for a in all_list:
        for w in a.split(" "):
            s = len(w)
            if s == 5:
                t = translate(w, decoder)
                print(w, t, is_valid(t))
                if not is_valid(t):
                    loop = 1

                    r = 1
                    for i in range(len(choice_mask) - 1, -1, -1):
                        choice_mask[i] += r

                        if choice_mask[i] == 2:
                            choice_mask[i] = 0
                            r = 1
                        else:
                            r = 0
                    break
        if loop == 1:
            break
    if loop == 1 and choice_mask == [0, 0, 0]:
        print("Loop infinito")
        exit()

if loop == 0:
    print()
    print()
    for k, v in decoder.items():
        print(f"{k}: {v}")

    number_list = []
    for fdos in fdos_list:

        n = ""
        for output in fdos.split(" "):
            t = translate(output, decoder)
            word = [e for e in t]
            word.sort()

            for number, code in original.items():
                if word == code:
                    n += str(number)
                    break
        if n != '':
            number_list.append(int(n))

    print(number_list)
