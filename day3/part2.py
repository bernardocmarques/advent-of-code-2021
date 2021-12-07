from utils import bin_to_dec

ogr = ""
csr = ""
with open("input.txt", "r") as input_file:
    codes_ogr = [e.replace("\n", "") for e in input_file.readlines()]
    codes_csr = [e for e in codes_ogr]

index = 0
keep = ""
while index + 1:
    b_count = [0, 0]
    for code in codes_ogr:
        b_count[int(code[index])] += 1


    keep += "1" if b_count[0] == b_count[1] else str(max(range(len(b_count)), key=b_count.__getitem__))

    codes_ogr = [e for e in codes_ogr if e.startswith(keep)]

    if len(codes_ogr) == 1:
        ogr = codes_ogr[0]
        index = -1
    else:
        index += 1

print(ogr, bin_to_dec(ogr))


index = 0
keep = ""
while index + 1:
    b_count = [0, 0]
    for code in codes_csr:
        b_count[int(code[index])] += 1

    keep += "0" if b_count[0] == b_count[1] else str(min(range(len(b_count)), key=b_count.__getitem__))

    codes_csr = [e for e in codes_csr if e.startswith(keep)]

    if len(codes_csr) == 1:
        csr = codes_csr[0]
        index = -1
    else:
        index += 1

print(csr, bin_to_dec(csr))


print(bin_to_dec(ogr) * bin_to_dec(csr))