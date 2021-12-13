from utils import *
import time

with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]

graph = {}

for line in lines:
    n1 = line.split("-")[0]
    n2 = line.split("-")[1]

    if n1 == "start" or n2 == "end":
        if n1 in graph:
            graph[n1].append(n2)
        else:
            graph[n1] = [n2]
    else:
        if n1 in graph:
            graph[n1].append(n2)
        else:
            graph[n1] = [n2]

        if n2 in graph:
            graph[n2].append(n1)
        else:
            graph[n2] = [n1]


print(graph)

paths = []

part1(graph, "start", paths)

print(len(paths))