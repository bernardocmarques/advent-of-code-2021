g = ""
e = ""
with open("input.txt", "r") as input_file:
    codes = [e.replace("\n", "") for e in input_file.readlines()]

b_count_list = []
for i in range(len(codes[0])):
    b_count_list.append([0, 0])
for code in codes:

    for i in range(len(code)):
        b_count_list[i][int(code[i])] += 1

for b_count in b_count_list:
    g += str(max(range(len(b_count)), key=b_count.__getitem__))
    e += str(min(range(len(b_count)), key=b_count.__getitem__))

g_d = 0
for i in range(len(g)):
    g_d += int(g[::-1][i]) * (2 ** i)

e_d = 0
for i in range(len(g)):
    e_d += int(e[::-1][i]) * (2 ** i)

print(g_d, e_d, g_d * e_d)