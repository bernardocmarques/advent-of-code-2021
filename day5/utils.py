def print_grid(grid):

    n_lines = 0
    n_rows = 0
    for k, v in grid.items():
        n_lines = max(n_lines, int(k))
        n_rows = max([n_rows] + [int(k) for k, _ in v.items()])

    for l in range(n_lines+1):
        line = ""
        for r in range(n_rows+1):
            if grid.get(l) and grid[l].get(r):
                line += str(grid[l][r])
            else:
                line += "."
        print(line)