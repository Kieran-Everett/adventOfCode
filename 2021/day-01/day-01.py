f = open("2021/day-01/day-01-input")
previous = 0
increases = 0
firstNumber = True

for number in f:
    if firstNumber:
        previous = int(number)
        firstNumber = False
    else:
        if int(number) > previous:
            increases += 1
        previous = int(number)

print(increases)