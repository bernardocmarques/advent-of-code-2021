def bin_to_dec(b):
    res = 0
    for i in range(len(b)):
        res += int(b[::-1][i]) * (2 ** i)

    return res


