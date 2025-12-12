# Reactor

def getInput():
    file = open("Day11/input.txt", "r")
    connections = {}
    for line in file.read().split("\n"):
        nodes = line.split(" ")

        if nodes[0][0:-1] not in connections:
            connections[nodes[0][0:-1]] = set()

        for i in range(1, len(nodes)):
            connections[nodes[0][0:-1]].add(nodes[i])

    return connections

def countPaths(currNode, connections):
    # Recursive DFS. Assumes no cycles between "you" and "out"
    if currNode == "out":
        return 1
    
    count = 0
    for node in connections[currNode]:
        count += countPaths(node, connections)
    
    return count

def main():
    connections = getInput()
    print(countPaths("you", connections))

main()