f = open("2021/day-03/day-03-input")

numberOfLines = 0
numberOfOnes = [0,0,0,0,0,0,0,0,0,0,0,0]

for line in f:
    numberOfLines += 1
    charCount = 0
    for char in line:
        if char == "1":
            numberOfOnes[charCount] += 1
        charCount += 1

gamma = ""
epsilon = ""
for num in numberOfOnes:
    if num > numberOfLines/2:
        gamma += "1"
    else:
        gamma += "0"

for num in numberOfOnes:
    if num < numberOfLines/2:
        epsilon += "1"
    else:
        epsilon += "0"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma * epsilon)