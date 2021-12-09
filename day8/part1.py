with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]

usp_list = [e.split(" | ")[0] for e in lines]
fdos_list = [e.split(" | ")[1] for e in lines]

c = 0

for fdos in fdos_list:
    for output in fdos.split(" "):
        s = len(output)

        if s == 2 or s == 4 or s == 3 or s == 7:
            c += 1

print(c)