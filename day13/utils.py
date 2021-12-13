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

    for x in range(len(g[y])):
        g[y][x] = "-"

    for j in range(len(g) - 1, y, -1):
        for i in range(len(g[y])):
            print((i, j))
    print_grid(g)


def _fold_x(g, x):
    pass
