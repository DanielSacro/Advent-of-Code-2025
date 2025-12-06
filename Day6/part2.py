# Trash Compactor - more of a parsing problem than anything

def getInput():
    file = open("Day6/input.txt", "r")
    input = file.read().split("\n")

    # Transpose input (numerical portion only)
    nums = []
    for i in range(0, len(input[0])):
        nums.append("")

    for i in range(0, len(input) - 1):
        for j in range(0, len(input[0])):
            if input[i][j] != " ":
                nums[j] += input[i][j]

    # Group numbers in the same equation together
    operands = []
    operand = []
    for n in nums:
        if n != "":
            operand.append(n)
        else:
            operands.append(operand)
            operand = []

    if operand != []:
        # Group final numbers together if needed
        operands.append(operand)

    operators = []
    for operator in input[-1].split(" "):
        if operator != "":
            operators.append(operator)
    
    return operands, operators

def main():
    # Just use int() since we're on 64-bit system... again
    operands, operators = getInput()

    total = 0
    for i in range(0, len(operands)):
        product = 1
        for n in operands[i]:
            if operators[i] == "+":
                total += int(n)
            else:
                product *= int(n)
        
        if operators[i] == "*":
            total += product

    print(total)

main()