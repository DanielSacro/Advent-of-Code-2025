# Cafeteria

def getInput():
    file = open("Day5/input.txt", "r")
    input = file.read().split("\n")
    ranges = {}
    for i in input:
        if i == "":
            break

        bounds = i.split("-")

        # Exploit 64-bit system using int()
        bounds[0] = int(bounds[0])
        bounds[1] = int(bounds[1])

        if bounds[0] not in ranges or ranges[bounds[0]] < bounds[1]:
            # Add the bounds if it doesn't exist or update the bounds to increase its range
            ranges[bounds[0]] = bounds[1]
    
    return ranges

def main():
    ranges = getInput()
    
    # Combine ranges
    lowerBounds = list(ranges)
    lowerBounds.sort() # Simplifies bound checking
    combinedRanges = {} # Stores ranges as key-value pairs, keys = lower bound, values = upper bounds
    prevLowerBound = None
    for currLowerBound in lowerBounds:
        if len(combinedRanges) == 0 or not (prevLowerBound <= currLowerBound and currLowerBound <= combinedRanges[prevLowerBound]):
            # No combined ranges yet or we can't combine previous range and current range
            combinedRanges[currLowerBound] = ranges[currLowerBound]
            prevLowerBound = currLowerBound
        else:
            # Current lower bound is inside previous range
            if combinedRanges[prevLowerBound] < ranges[currLowerBound]:
                # Upper bound of previous range can be extended/updated
                combinedRanges[prevLowerBound] = ranges[currLowerBound]

    # Use range bounds to count # of valid IDs
    count = 0
    for cr in combinedRanges:
        count += combinedRanges[cr] - cr + 1
    
    print(count)

main()