# Get integer fuel value from an integer mass.
def getFuel(mass):
    fuel = mass
    fuel = int(fuel / 3)
    fuel = fuel - 2

    return fuel

# print(getFuel(12))
# print(getFuel(14))
# print(getFuel(1969))
# print(getFuel(100756))

# Get integer fuel value from file input.
def getFuelFromFileInput(fileName):
    inputFile = open(fileName, "r")

    # Start with zero fuel
    fuelSum = 0
    # Iterate through all of the masses and add the fuel value to the fuel sum
    for line in inputFile:
        fuelSum = fuelSum + getFuel(int(line))

    return fuelSum

# Get integer fuel value from file input.
def getTotalFuelFromFileInput(fileName):
    inputFile = open(fileName, "r")

    # Start with zero fuel
    fuelSum = 0
    # Iterate through all of the masses and add the fuel value to the fuel sum
    for line in inputFile:
        fuel = getFuel(int(line))
        fuelSum = fuelSum + fuel + getExtraFuel(fuel)

    return fuelSum

# Get integer fuel from integer fuel.
def getExtraFuel(fuel):
    subFuel = getFuel(fuel)
    if subFuel <= 0:
        return 0
    else:
        return subFuel + getExtraFuel(subFuel)


part1Fuel = getFuelFromFileInput("input_day_1.txt")
print("Part One Answer:", part1Fuel)
part2Fuel = getTotalFuelFromFileInput("input_day_1.txt")
print("Part Two Answer:", part2Fuel)

# print(getFuel(100756))
# print(getExtraFuel(getFuel(100756)))
# print(getFuel(100756) + getExtraFuel(getFuel(100756)))
#
# print(getFuel(3266516))
# print(getExtraFuel(getFuel(3266516)))
# print(getFuel(3266516) + getExtraFuel(getFuel(3266516)))
