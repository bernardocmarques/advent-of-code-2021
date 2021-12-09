from utils import *

with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]

heatmap = [[int(l) for l in e] for e in lines]

print_heatmap(heatmap)

local_lows = []
sum_lows = 0

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

        print(v, (i,j))
        sum_lows += (v+1)

print(sum_lows)