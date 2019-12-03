def getFuel(mass):
    fuel = mass
    fuel = int(fuel / 3)
    fuel = fuel - 2

    return fuel

# print(getFuel(12))
# print(getFuel(14))
# print(getFuel(1969))
# print(getFuel(100756))

inputFile = open("input.txt", "r")
fuelSum = 0
for line in inputFile:
    fuelSum = fuelSum + getFuel(int(line))

print(fuelSum)