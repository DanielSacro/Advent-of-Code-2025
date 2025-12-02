# Gift Shop

def getInput():
    file = open("Day2/input.txt", "r")
    input = file.read()
    return input.split(",")

def isValid(id):
    for i in range(0, len(id) // 2):
        if id[i] != id[i + len(id) // 2]:
            return True
    return False   

def main():
    ranges = getInput()

    invalids = []
    for r in ranges:
        bounds = r.split("-")
        for id_val in range(int(bounds[0]), int(bounds[1]) + 1):
            id = str(id_val)
            if len(id) % 2 == 0 and not isValid(id):
                invalids.append(id_val)

    print(sum(invalids))

main()