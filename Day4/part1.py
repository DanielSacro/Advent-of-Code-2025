# Printing Department

def getInput():
    file = open("Day4/input.txt", "r")
    input = file.read()
    return input.split("\n")

def isAccessible(grid, r, c):
    adjacent = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if r + i < 0 or r + i >= len(grid) or c + j < 0 or c + j >= len(grid):
                # Out of bounds
                continue
            elif not (i == j and i == 0):
                # Don't check [r][c]
                if grid[r + i][c + j] == "@":
                    adjacent += 1
            
            if adjacent >= 4:
                return False
    return True

def main():
    grid = getInput()
    
    count = 0
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            if grid[r][c] == "@" and isAccessible(grid, r, c):
                count += 1

    print(count)

main()