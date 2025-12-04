# Lobby

def getInput():
    file = open("Day3/input.txt", "r")
    input = file.read()
    return input.split("\n")

def getLargestJoltage(bank):
    # Find largest digit in bank[0:len(bank) - 1]
    # If there are duplicates, choose the index i that appears first
    firstIndex = 0
    for i in range(0, len(bank) - 1):
        if int(bank[i]) > int(bank[firstIndex]):
            firstIndex = i

    # Find the next largest digit in bank[i:len(bank)]
    secondIndex = firstIndex + 1
    for i in range(secondIndex, len(bank)):
        if int(bank[i]) > int(bank[secondIndex]):
            secondIndex = i
    
    return int(bank[firstIndex] + bank[secondIndex])   

def main():
    banks = getInput()

    joltages = []
    for b in banks:
        joltages.append(getLargestJoltage(b))

    print(sum(joltages))

main()