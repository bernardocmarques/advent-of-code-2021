from utils import *

with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]

lines = ["target area: x=20..30, y=-10..-5"]
target_x = [int(e) for e in lines[0].split(": ")[1].split(", ")[0].split("x=")[1].split("..")]
target_y = [int(e) for e in lines[0].split(": ")[1].split(", ")[1].split("y=")[1].split("..")]

print(target_x, target_y)
speed = [1, 1]
pos = [0, 0]

highest_on_target_speed = [0, 0]
highest_y = 0
highest_on_target_y = 0
on_target_count = 0

x = 0
max_x = 0
while sum(range(x)) < target_x[1]:
    max_x = x
    x += 1

stop_sim = False
on_target = False


while not stop_sim:
    on_target = False
    initial_speed = [e for e in speed]
    highest_y = 0

    while True:
        pos = [pos[0] + speed[0], pos[1] + speed[1]]
        speed[0] = max(speed[0] - 1, 0)
        speed[1] -= 1
        highest_y = max(pos[1], highest_y)

        if target_x[0] <= pos[0] <= target_x[1] and target_y[0] <= pos[1] <= target_y[1]:
            on_target = True
            break

        if pos[0] > target_x[1]:
            break

        if pos[1] < target_y[0]:
            break

    # print("speed:", initial_speed, max_x)
    # print("pos:", pos)
    # print(f"-- Q{q} | on_target: {on_target} | stop_sim: {stop_sim}")
    # input()

    pos = [0, 0]
    if initial_speed[0] < max_x:
        speed = [e for e in initial_speed]
        speed[0] += 1
    else:
        speed = [e for e in initial_speed]
        speed[0] = 1
        speed[1] += 1
    if on_target:
        # speed = [e for e in initial_speed]
        # speed[0] = 1
        # speed[1] += 1
        on_target_count += 1
        highest_on_target_speed = [e for e in initial_speed]
        highest_on_target_y = highest_y
        print(highest_on_target_speed)
        print(highest_on_target_y)
        # print(on_target_count)


