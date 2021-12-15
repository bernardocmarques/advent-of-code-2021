import queue


def print_grid(g):
    print()
    for line in g:
        print("".join([str(e) for e in line]))
    print()


def dijkstra(graph, start, end=None):
    dist = {}
    prev = {}

    dist[start] = 0

    Q = queue.PriorityQueue()

    for v in graph.keys():
        if v != start:
            dist[v] = float('inf')
            prev[v] = None

        Q.put((dist[v], v))

    while not Q.empty():
        u = Q.get()[1]

        for v in graph[u].keys():
            alt = dist[u] + graph[u][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                Q.put((alt, v))
            if end and v == end:
                print("Cost:", dist[end])
                exit()
    return dist, prev
