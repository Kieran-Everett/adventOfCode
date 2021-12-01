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
f.close()


f = open("2021/day-01/day-01-input")
previous = 0
increases = 0
count = 0
array = []
firstSection = True

for number in f:
    array.append(int(number))
    if firstSection:
        if count > 2:
            firstSection = False
    else:
        previous = array[count-3] + array[count-2] + array[count-1]
        current = array[count-2] + array[count-1] + array[count]
        if current > previous:
            increases += 1

    count += 1

print(increases) # one below for some reason lol
f.close()