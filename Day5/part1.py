# Cafeteria

def getInput():
    file = open("Day5/input.txt", "r")
    input = file.read().split("\n")
    ranges = []
    IDs = []
    getIDs = False
    for i in input:
        if getIDs:
            IDs.append(i)
        else:
            if i == "":
                getIDs = True
                continue
            
            ranges.append(i)

    return ranges, IDs

def isInBounds(ID, ID_range):
    bounds = ID_range.split("-")

    # Does # of digits make sense?
    if len(ID) < len(bounds[0]) or len(ID) > len(bounds[1]):
        return False

    # Lower bound check
    if len(ID) == len(bounds[0]):
        # if len(ID) > len(bounds[0]), it's already within range
        if ID == bounds[0]:
            # On the bound
            return True
        
        # Greater than lower bound?
        for i in range(0, len(ID)):
            if int(ID[i]) > int(bounds[0][i]):
                # Most significant non-matching digit of ID is greater than same digit in lower bound
                break
            elif int(ID[i]) == int(bounds[0][i]):
                # if digits match, need to check next digit
                continue
            elif int(ID[i]) < int(bounds[0][i]):
                return False

    # Upper bound check
    if len(ID) == len(bounds[1]):
        # if len(ID) < len(bounds[1]), it's already within range
        if ID == bounds[1]:
            return True

        # Lesser than upper bound?
        for i in range(0, len(ID)):
            if int(ID[i]) < int(bounds[1][i]):
                # Most significant non-matching digit of ID is lesser than same digit in upper bound
                break
            elif int(ID[i]) == int(bounds[1][i]):
                continue
            elif int(ID[i]) > int(bounds[1][i]):
                return False

    return True

def main():
    ranges, IDs = getInput()

    count = 0
    for i in IDs:
        for r in ranges:
            if isInBounds(i, r):
                count += 1
                break
    
    print(count)

main()