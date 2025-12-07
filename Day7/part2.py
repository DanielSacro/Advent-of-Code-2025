# Laboratories

def getInput():
    file = open("Day7/input.txt", "r")
    input = file.read().split("\n")
   
    return input

def main():
    splitters = getInput()

    # Keep track of each beam position and how many beams are in a given position
    beams = {}
    for i in range(0, len(splitters[0])):
        if splitters[0][i] == "S":
            beams[i] = 1
            break

    for i in range(1, len(splitters)):
        print("Progress:", round(i / len(splitters) * 100, 2), "%")
        if i % 2 == 1:
            # Each odd i has no splitters
            continue
        
        new_beams = {}
        for b in beams:
            if splitters[i][b] == "^":
                if b - 1 >= 0:
                    if b - 1 not in new_beams:
                        new_beams[b - 1] = beams[b]
                    else:
                        # Overlapping beams, so note there's more than 1 beam in the same position
                        new_beams[b - 1] += beams[b]
                if b + 1 < len(splitters[0]):
                    if b + 1 not in new_beams:
                        new_beams[b + 1] = beams[b]
                    else:
                        new_beams[b + 1] += beams[b]
            else:
                if b not in new_beams:
                    new_beams[b] = beams[b]
                else:
                    new_beams[b] += beams[b]

        beams = new_beams
        
    paths = 0
    for b in beams:
        paths += beams[b]

    print(paths)

main()