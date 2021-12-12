def countPaths(adjList, cur, smallVisit):
    numPaths = 0
    for nxt in adjList[cur]:
        if nxt == 'end':
            numPaths += 1
            continue
        if nxt[0:1].islower():
            if smallVisit[nxt] == 0 or (smallVisit[nxt] == 1 and max(smallVisit.values()) == 1):
                smallVisit[nxt] += 1
                np = countPaths(adjList, nxt, smallVisit)
                smallVisit[nxt] -= 1
                numPaths += np
        else:
            np = countPaths(adjList, nxt, smallVisit)
            numPaths += np
    return numPaths

def countPathsInit(adjList):
    smallVisit = {}
    for s in adjList:
        if s == 'start' or s == 'end' or s[0:1].isupper():
            continue
        smallVisit[s] = 0
    return countPaths(adjList, 'start', smallVisit)

def main():
    adjList = {}
    with open('Data.txt', 'r') as file:
        for line in file:
            s = line
            if s[-1] == '\n':
                s = s[:-1]
            src_dest = s.split('-')
            src = src_dest[0]
            dest = src_dest[1]
            if not src in adjList:
                adjList[src] = []
            if not dest in adjList:
                adjList[dest] = []
            if src == 'start' or dest == 'end':
                adjList[src].append(dest)
                continue
            if src == 'end' or dest == 'start':
                adjList[dest].append(src)
                continue
            if src[0:1].isupper() and dest[0:1].isupper():
                continue
            adjList[src].append(dest)
            adjList[dest].append(src)
    numPaths = countPathsInit(adjList)
    print(numPaths)
            
if __name__ == "__main__":
    main()
    
