# Gift Shop

def getInput():
    file = open("Day3/input.txt", "r")
    input = file.read()
    return input.split("\n")

def getLargestJoltage(bank):
    largestJoltage = ""

    currDigitIndex = -1
    for i in range(11, -1, -1):
        currDigitIndex += 1
        for j in range(currDigitIndex, len(bank) - i):
            if int(bank[j]) > int(bank[currDigitIndex]):
                currDigitIndex = j
        
        largestJoltage += bank[currDigitIndex]
    
    return largestJoltage

# Personal computer can handle 64-bit ints, but try to compute sums as if we can only do 32-bit ints anyway
def computeSum(joltages):
    sum = "0" * 12
    for j in joltages:
        if len(sum) > len(j):
            # 0 padding
            j = "0" * (len(sum) - len(j)) + j

        newSum = ""
        carry = 0
        for i in range(len(sum) - 1, -1, -1):
            digitSum = int(sum[i]) + int(j[i]) + carry
            if digitSum > 9:
                carry = 1
                digitSum -= 10
            else:
                carry = 0
            newSum += str(digitSum)
        
        if carry:
            newSum += str(carry)
        
        sum = newSum[::-1]
    
    return sum

def main():
    banks = getInput()

    joltages = []
    for b in banks:
        joltages.append(getLargestJoltage(b))

    print(computeSum(joltages))

main()