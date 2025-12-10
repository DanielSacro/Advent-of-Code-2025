# Movie Theatre

def getInput():
    file = open("Day9/input.txt", "r")
    return file.read().split("\n")

def main():
    tiles = getInput()

    # Brute Force. O(n^2) is permissible for small n (input has n < 500)
    maxArea = 1
    for i in range(0, len(tiles) - 1):
        tile1 = tiles[i].split(",")
        for j in range(i + 1, len(tiles)):
            tile2 = tiles[j].split(",")

            # Exploit 64-bit system
            area = (abs(int(tile1[0]) - int(tile2[0])) + 1) * (abs(int(tile1[1]) - int(tile2[1])) + 1)
            if maxArea < area:
                maxArea = area
    
    print(maxArea)

main()