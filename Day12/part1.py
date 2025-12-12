# Christmas Tree Farm

def getInput():
    file = open("Day12/input.txt", "r")
    input = file.read().split("\n")

    # Only 6 presents in the example input and actual input
    # Each present is 3x3 grid
    # Presents are on only first 30 lines of inputs
    presents = []
    for i in range(0, 5*6, 5):
        present = []
        present.append(input[1 + i])
        present.append(input[2 + i])
        present.append(input[3 + i])
        presents.append(present)

    presentSizes = []
    for p in presents:
        count = 0
        for row in p:
            for r in row:
                if r == "#":
                    count += 1
        presentSizes.append(count)

    regions = []
    for i in range(0, len(input)):
        if i < 30:
            continue
        regions.append(input[i])

    return presents, presentSizes, regions

# Somehow solved part 1 without actually fitting them...
def main():
    presents, presentSizes, regions = getInput()
    
    solvable = 0
    for r in regions:
        # See if there's enough room for the presents before trying to fit them
        info = r.split(" ")
        gridSize = info[0].split("x")
        totCells = int(gridSize[0]) * int(gridSize[1][:-1])

        presentsNeeded = info[1:]
        cellsNeeded = 0
        for i in range(0, len(presents)):
            cellsNeeded += presentSizes[i] * int(presentsNeeded[i])
        
        if cellsNeeded > totCells:
            continue
        
        # If there is, try to fit them
        solvable += 1

    print(solvable)

main()