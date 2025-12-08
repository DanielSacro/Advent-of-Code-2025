# Playground

def getInput():
    file = open("Day8/input.txt", "r")
    return file.read().split("\n")

def getDistance(box1, box2):
    coords1 = box1.split(",")
    coords2 = box2.split(",")

    return ((int(coords1[0]) - int(coords2[0]))**2 + (int(coords1[1]) - int(coords2[1]))**2 + (int(coords1[2]) - int(coords2[2]))**2) ** 0.5

def combineGroups(ID1, ID2, circuits, connected):
    # Move all boxes from circuit ID1 into circuit ID2
    for box in circuits[ID1]:
        connected[box] = ID2
        circuits[ID2].append(box)
    
    # Circuit with ID1 should not exist anymore as it is part of circuit ID2 now
    circuits.pop(ID1)

def main():
    boxes = getInput()

    # Get distances via brute force -> O(n^2)
    distances = {}
    for i in range(0, len(boxes) - 1):
        for j in range(i + 1, len(boxes)):
            dist = getDistance(boxes[i], boxes[j])
            if dist not in distances:
                distances[dist] = [(boxes[i], boxes[j])]
            else:
                distances[dist].append((boxes[i], boxes[j]))
    
    # Sort n distances, connect first p pairs to form a circuit with some ID #, re-assign circuit IDs to combine circuits of b boxes if needed
    # -> O(nlog(n) + p*b)
    circuits = {} # Maps circuit IDs to boxes -> To track circuit sizes and make circuit ID re-assigning easier/faster
    connected = {} # Maps boxes to circuit IDs -> To check if we need to re-assign circuit IDs or not
    nextID = 0
    finalPair = None
    for d in sorted(distances):
        # In case more than 1 pair have the same distances
        for pair in distances[d]:
            if pair[0] not in connected and pair[1] not in connected:
                # New circuit
                circuits[nextID] = [pair[0], pair[1]]
                connected[pair[0]] = nextID
                connected[pair[1]] = nextID
                nextID += 1
            elif pair[0] in connected and pair[1] in connected:
                # May need to combine 2 circuits
                if connected[pair[0]] != connected[pair[1]]:
                    # Circuit IDs don't match, so combine circuits
                    combineGroups(connected[pair[0]], connected[pair[1]], circuits, connected)
                # Otherwise, boxes are already in the same circuit.
                # Note that a pair is still formed even if they're in the same circuit
            else:
                # Add unconnected box to connected box's circuit
                if pair[0] not in connected:
                    circuits[connected[pair[1]]].append(pair[0])
                    connected[pair[0]] = connected[pair[1]]
                elif pair[1] not in connected:
                    circuits[connected[pair[0]]].append(pair[1])
                    connected[pair[1]] = connected[pair[0]]
            
            if len(connected) == len(boxes):
                finalPair = pair
                break
        if len(connected) == len(boxes):
            break

    # Product of x values for final connection
    print(finalPair)
    x1 = int(finalPair[0].split(",")[0])
    x2 = int(finalPair[1].split(",")[0])
    print(x1, x2, x1 * x2)

main()