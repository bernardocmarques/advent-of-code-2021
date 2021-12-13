def print_grid(g):
    print()
    for line in g:
        print("".join([str(e) for e in line]))
    print()


def fold(g, f):
    m = f[0]

    if m == 'y':
        _fold_y(g, int(f[1]))
    elif m == 'x':
        _fold_x(g, int(f[1]))


def _fold_y(g, y):
    n = 0

    for j in range(len(g) - 1, y, -1):
        for i in range(len(g[y])):
            if g[j][i] == '#':
                g[n][i] = '#'
        del g[j]
        n += 1
    del g[y]


def _fold_x(g, x):
    for j in range(len(g)):
        n = 0
        for i in range(len(g[j]) - 1, x - 1, -1):
            if i != x:
                if g[j][i] == '#':
                    g[j][n] = '#'
            del g[j][i]
            n += 1



