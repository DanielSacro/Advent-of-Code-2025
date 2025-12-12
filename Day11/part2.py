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

def countPaths(curr, goal, connections, seen):
    # Recursive DFS w/ Memoization. Assumes no cycles between curr and goal
    if curr == goal:
        # There's only 1 path connecting the previous node and this node
        return 1
    elif curr == "out" and "out" != goal:
        # Reached a dead end - "out" has no outward connections
        return 0
    
    count = 0
    for next in connections[curr]:
        if next not in seen:
            # New path, need to traverse
            seen[next] = countPaths(next, goal, connections, seen)
        count += seen[next]
    
    return count

def main():
    connections = getInput()
    
    # Need a path between svr and out that travels through dac and fft in any order
    # Valid paths are: svr -> dac -> fft -> out, svr -> fft -> dac -> out
    # Count for first valid path is svr-dac paths * dac-fft paths * fft-out paths
    # Count for second valid path is svr-fft paths * fft-dac paths * dac-out paths

    svr_dac = countPaths("svr", "dac", connections, {})
    dac_fft = countPaths("dac", "fft", connections, {})
    fft_out = countPaths("fft", "out", connections, {})

    svr_fft = countPaths("svr", "fft", connections, {})
    fft_dac = countPaths("fft", "dac", connections, {})
    dac_out = countPaths ("dac", "out", connections, {})

    # Int values may be large, but we're on a 64-bit system so it's fine
    total = (svr_dac * dac_fft * fft_out) + (svr_fft * fft_dac * dac_out)
    print(total)

main()