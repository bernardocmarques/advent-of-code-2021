from utils import *

with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]

grid = [[int(l) for l in e] for e in lines]

print_grid(grid)

local_lows = []
sum_lows = 0

i_size = len(grid)
j_size = len(grid[0])

flash_count = 0

step_count = 0

loop = True
while loop:
    loop = False
    print(f"Step {step_count + 1}")
    step_count += 1
    to_flash = []
    for i in range(i_size):
        for j in range(j_size):
            grid[i][j] += 1

            if grid[i][j] > 9:
                to_flash.append((i, j))


    # print_grid(grid)

    while to_flash:
        flash_count += 1
        i, j = to_flash.pop(0)
        v = grid[i][j]

        # print(i, j)
        to_do = [
            (i - 1, j - 1),
            (i - 1, j),
            (i - 1, j + 1),
            (i, j - 1),
            (i, j + 1),
            (i + 1, j - 1),
            (i + 1, j),
            (i + 1, j + 1)
        ]

        if i == 0:
            if (i - 1, j - 1) in to_do: to_do.remove((i - 1, j - 1))
            if (i - 1, j) in to_do: to_do.remove((i - 1, j))
            if (i - 1, j + 1) in to_do: to_do.remove((i - 1, j + 1))
        elif i == i_size - 1:
            if (i + 1, j - 1) in to_do: to_do.remove((i + 1, j - 1))
            if (i + 1, j) in to_do: to_do.remove((i + 1, j))
            if (i + 1, j + 1) in to_do: to_do.remove((i + 1, j + 1))

        if j == 0:
            if (i - 1, j - 1) in to_do: to_do.remove((i - 1, j - 1))
            if (i, j - 1) in to_do: to_do.remove((i, j - 1))
            if (i + 1, j - 1) in to_do: to_do.remove((i + 1, j - 1))
        elif j == j_size - 1:
            if (i - 1, j + 1) in to_do: to_do.remove((i - 1, j + 1))
            if (i, j + 1) in to_do: to_do.remove((i, j + 1))
            if (i + 1, j + 1) in to_do: to_do.remove((i + 1, j + 1))

        for x, y in to_do:
            grid[x][y] += 1

            if grid[x][y] == 10:  # right
                to_flash.append((x, y))

        # print_grid(grid)
        # print(to_flash)

    for i in range(i_size):
        for j in range(j_size):

            if grid[i][j] > 9:
                grid[i][j] = 0

    for i in range(i_size):
        for j in range(j_size):

            if grid[i][j] == 0:
                continue
            else:
                loop = True
                break
        if loop:
            break

    print_grid(grid)

print(step_count)
