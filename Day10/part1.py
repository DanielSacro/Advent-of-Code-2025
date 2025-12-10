# Factory
from queue import Queue

def getInput():
    file = open("Day10/input.txt", "r")
    return file.read().split("\n")

def infoToBinary(info):
    target = 0
    for light in range(1, len(info[0]) - 1):
        target *= 2 # Left shift
        if info[0][light] == "#":
            target += 1 # LSB becomes 1
    
    buttons = []
    for button in info[1:-1]:
        lights = button[1:-1].split(",")
        b = 0
        for i in range(0, len(info[0]) - 2):
            b *= 2 # Left shift
            if str(i) in lights:
                b += 1
        buttons.append(b)
    
    return target, buttons

def findMinSolution(target, buttons):
    # Note that pressing a button twice is the same as not pressing it at all
    # The shortest solution will have its buttons pressed at most once (i.e. 1 press or 0 press)

    # Brute force BFS solution in polynomial time - O(b + (b-1)^2 + (b-2)^3 + ... + 1)
    # -> Permissible for small b (input has b < 15)

    # Need to track: state of lights, # of buttons pressed, last button pressed -> 3 ints
    searchSpace = Queue()
    for i in range(0, len(buttons)):
        searchSpace.put((buttons[i], 1, i))
    
    while not searchSpace.empty():
        # Combo = (Light State, # Buttons Pressed, # Last Button Pressed)
        combo = searchSpace.get()
        if combo[0] == target:
            return combo[1]

        # Generate more combos from this combo if possible
        if combo[2] == len(buttons) - 1:
            # No more buttons to add to this combo - already reached last button
            continue

        for i in range(combo[2] + 1, len(buttons)):
            searchSpace.put((combo[0] ^ buttons[i], combo[1] + 1, i))
    
    # No solution
    return 0

def main():
    robots = getInput()

    counts = []
    for r in robots:
        # Use binary representation (ints) to exploit bitwise XOR
        target, buttons = infoToBinary(r.split(" "))
        counts.append(findMinSolution(target, buttons))

    print(counts, sum(counts))

main()