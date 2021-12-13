path = []
on_path = []


def part1(g, n, paths):
    global on_path, path
    path.append(n)
    if n == n.lower():
        on_path.append(n)

    if n == "end":
        paths.append([e for e in path])
    else:
        for a in g[n]:
            if a not in on_path:
                part1(g, a, paths)

    path.pop()
    if n == n.lower():
        on_path.remove(n)


def part2(g, n, paths):
    global on_path, path
    path.append(n)
    if n == n.lower():
        on_path.append(n)

    if n == "end":
        paths.append([e for e in path])
    else:
        for a in g[n]:
            if a not in on_path:
                part2(g, a, paths)
            elif len(on_path) == len(set(on_path)) and a != 'end' and a != 'start':
                t = ''
                part2(g, a, paths)

    path.pop()
    if n == n.lower():
        on_path.remove(n)
