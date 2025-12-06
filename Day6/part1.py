# Trash Compactor

def getInput():
    file = open("Day6/input.txt", "r")
    input = file.read().split("\n")

    rows = []
    for i in range(0, len(input) - 1):
        row = []
        for num in input[i].split(" "):
            if num != "":
                row.append(num)
        rows.append(row)

    ops = []
    for op in input[-1].split(" "):
        if op != "":
            ops.append(op)
    
    return rows, ops 

def main():
    # Just use int() since we're on 64-bit system... again
    rows, ops = getInput()
    total = 0
    for col in range(0, len(rows[0])):
        product = 1
        for row in rows:
            if ops[col] == "+":
                total += int(row[col])
            else:
                product *= int(row[col])
        
        if ops[col] == "*":
            total += product
    
    print(total)

main()