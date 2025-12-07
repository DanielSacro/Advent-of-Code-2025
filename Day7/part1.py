# Laboratories

def getInput():
    file = open("Day7/input.txt", "r")
    input = file.read().split("\n")
   
    return input

def putOutput(output):
    file = open("Day7/output.txt", "a")
    file.write(output)

def clearOutput():
    file = open("Day7/output.txt", "w")
    file.write("")

def main():
    splitters = getInput()

    beams = set()
    splits = 0
    for i in range(0, len(splitters[0])):
        if splitters[0][i] == "S":
            beams.add(i)
            break

    clearOutput()
    for i in range(1, len(splitters)):
        if i % 2 == 1:
            # Each odd i has no splitters
            for i in range(0, len(splitters[0])):
                if i in beams:
                    putOutput("|")
                else:
                    putOutput(".")
            putOutput("\n")
            continue
        putOutput(splitters[i] + "\n")
        
        new_beams = set()
        split_beams = set()
        for b in beams:
            if splitters[i][b] == "^":
                splits += 1
                if b - 1 >= 0:
                    new_beams.add(b - 1)
                if b + 1 < len(splitters[0]):
                    new_beams.add(b + 1)
                split_beams.add(b)

        for b in split_beams:
            beams.remove(b)

        for b in new_beams:
            beams.add(b)
        
    print(splits)    

main()