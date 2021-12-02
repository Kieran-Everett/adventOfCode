f = open("2021/day-02/day-02-input")
x = 0
y = 0

for line in f:
    movement = line.split()
    if movement[0] == "forward":
        x += int(movement[1])
    elif movement[0] == "down":
        y += int(movement[1])
    elif movement[0] == "up":
        y -= int(movement[1])

print(x*y)
f.close()


f = open("2021/day-02/day-02-input")
x = 0
y = 0
aim = 0

for line in f:
    movement = line.split()
    if movement[0] == "forward":
        x += int(movement[1])
        y += int(movement[1]) * aim
    elif movement[0] == "down":
        aim += int(movement[1])
    elif movement[0] == "up":
        aim -= int(movement[1])

print(x*y)
f.close()