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
            dial += int(r[1:])
        else:
            dial -= int(r[1:])
        
        dial %= 100
        
        if dial == 0:
            count += 1
    
    print(count)

main()