# Create a function to read a file and pass input to our processInputs function.
def readFileAndProcess(inputFile):
    inputList = []
    puzzleInput = open(inputFile, "r")
    for line in puzzleInput:
        for num in line.split(","):
            inputList.append(int(num))

    processInputs(inputList)


# Create a function to consume a list of integer inputs.
def processInputs(inputList):
    # PART 1 ANSWER INPUT
    inputList[1] = 12  # noun
    # PART 1 ANSWER INPUT
    inputList[2] = 2  # verb

    # PART 2 ANSWER INPUT
    # inputList[1] = 38 # noun
    # PART 2 ANSWER INPUT
    # inputList[2] = 92 # verb

    print("Before\n", inputList)
    indexValue = 0
    while True:
        input = inputList[indexValue]
        if input == 1:
            # do 1 things, add position 1 and 2 and place into 3
            position1 = inputList[indexValue + 1]
            position2 = inputList[indexValue + 2]
            position3 = inputList[indexValue + 3]
            inputList[position3] = inputList[position1] + inputList[position2]
            indexValue += 4
        elif input == 2:
            # do 2 things, multiply position 1 and 2 and place into 3
            position1 = inputList[indexValue + 1]
            position2 = inputList[indexValue + 2]
            position3 = inputList[indexValue + 3]
            inputList[position3] = inputList[position1] * inputList[position2]
            indexValue += 4
        elif input == 99:
            # do 99 things, we are done
            break
        else:
            print("Something went wrong at index:", indexValue)
            break

    print("After\n", inputList)


readFileAndProcess("puzzleinput.txt")

"""
Part two was asking what inputs would create a result of 19690720 for address 0.
I figured this out by trial an error first by increasing the noun (12 initially) up until I got to 1969 for
the major numbers and that ended up being 38. Then I played with the verb (2 initially) up until I
got to 0720 for the minor number that ended up being 92.
"""
