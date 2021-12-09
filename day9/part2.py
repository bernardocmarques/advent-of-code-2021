from utils import *

with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]

heatmap = [[int(l) for l in e] for e in lines]

# print_heatmap(heatmap)

local_lows = []

i_size = len(heatmap)
j_size = len(heatmap[0])

for i in range(i_size):
    for j in range(j_size):
        v = heatmap[i][j]

        if i == 0:
            if v >= heatmap[i+1][j]:  # right
                continue

        elif i == i_size - 1:
            if v >= heatmap[i-1][j]:  # left
                continue
        else:
            if v >= heatmap[i+1][j]:  # right
                continue

            if v >= heatmap[i-1][j]:  # left
                continue

        if j == 0:
            if v >= heatmap[i][j + 1]:  # down
                continue

        elif j == j_size - 1:
            if v >= heatmap[i][j - 1]:  # up
                continue
        else:
            if v >= heatmap[i][j + 1]:  # down
                continue

            if v >= heatmap[i][j - 1]:  # up
                continue

        local_lows.append((i, j))



basins = []

for local_low in local_lows:
    list_to_check = [local_low]
    basin = []
    while list_to_check:
        i, j = list_to_check.pop(0)

        if (i, j) in basin:
            continue

        v = heatmap[i][j]

        if v == 9:
            continue

        basin.append((i, j))

        if i == 0:
            if v < heatmap[i + 1][j]:  # right
                list_to_check.append((i + 1, j))



        elif i == i_size - 1:
            if v < heatmap[i - 1][j]:  # left
                list_to_check.append((i - 1, j))
        else:
            if v < heatmap[i + 1][j]:  # right
                list_to_check.append((i + 1, j))

            if v < heatmap[i - 1][j]:  # left
                list_to_check.append((i - 1, j))

        if j == 0:
            if v < heatmap[i][j + 1]:  # down
                list_to_check.append((i, j + 1))

        elif j == j_size - 1:
            if v < heatmap[i][j - 1]:  # up
                list_to_check.append((i, j - 1))
        else:
            if v < heatmap[i][j + 1]:  # down
                list_to_check.append((i, j + 1))

            if v < heatmap[i][j - 1]:  # up
                list_to_check.append((i, j - 1))


    basins.append(basin)



basins.sort(key=len, reverse=True)



res = 1
for basin in basins[:3]:
    res *= len(basin)

print(res)