from utils import *
import queue

with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]

grid = [[int(l) for l in e] for e in lines]

print_grid(grid)

i_size = len(grid)
j_size = len(grid[0])

graph = {}


all_nodes = {}

for i in range(i_size):
    for j in range(j_size):
        can_go = {}
        all_nodes[(i, j)] = grid[i][j]

        if i == 0:
            can_go[(i + 1, j)] = grid[i + 1][j]

        elif i == i_size - 1:
            can_go[(i - 1, j)] = grid[i - 1][j]
        else:
            can_go[(i + 1, j)] = grid[i + 1][j]
            can_go[(i - 1, j)] = grid[i - 1][j]

        if j == 0:
            can_go[(i, j + 1)] = grid[i][j + 1]
        elif j == j_size - 1:
            can_go[(i, j - 1)] = grid[i][j - 1]
        else:
            can_go[(i, j + 1)] = grid[i][j + 1]
            can_go[(i, j - 1)] = grid[i][j - 1]

        graph[(i, j)] = can_go

start = (0, 0)
end = (i_size-1, j_size-1)

dist, prev = dijkstra(graph, start, end)

key = (i_size-1, j_size-1)
print("Cost:", dist[key])
