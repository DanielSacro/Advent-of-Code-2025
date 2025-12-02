# Gift Shop

def getInput():
    file = open("Day2/input.txt", "r")
    input = file.read()
    return input.split(",")

def isValid(id):
    sequenceFound = False
    for i in range(1, len(id) // 2 + 1):
        sequenceFound = True
        for c in id.split(id[0:i]):
            if c != "":
                sequenceFound = False
                break
        if sequenceFound:
            return True
    return False

def main():
    ranges = getInput()

    invalids = []
    for r in ranges:
        bounds = r.split("-")
        for id_val in range(int(bounds[0]), int(bounds[1]) + 1):
            if isValid(str(id_val)):
                invalids.append(id_val)

    print(sum(invalids))

main()