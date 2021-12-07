with open("input.txt", "r") as input_file:
    measurements = input_file.readlines()

last = int(measurements[0])
count = 0
for measurement in measurements[1:]:
    m = int(measurement)
    count += 1 if m > last else 0
    last = m

print(count)
