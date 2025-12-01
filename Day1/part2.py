# Secret Entrance

def getInput():
    file = open("Day1/input.txt", "r")
    input = file.read()
    return input.split("\n")

def main():
    rotations = getInput()
    dial = 50

    count = 0
    for r in rotations:
        if r[0] == "R":
            for i in range(0, int(r[1:])):
                dial += 1
                if dial % 100 == 0:
                    count += 1
        else:
            for i in range(0, int(r[1:])):
                dial -= 1
                if dial % 100 == 0:
                    count += 1
    
    print(count)

main()