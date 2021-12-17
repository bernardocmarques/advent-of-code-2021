def bin_to_dec(b):
    res = 0
    for i in range(len(b)):
        res += int(b[::-1][i]) * (2 ** i)

    return res


hex_to_bin_dict = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


def hex_to_bin(hex_string):
    bin_string = ""

    for h in hex_string:
        bin_string += hex_to_bin_dict[h]

    return bin_string
