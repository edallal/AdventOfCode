def step(curCounts):
    nextCounts = {}
    for i in range(0, 9):
        nextCounts[i] = 0
    for k,v in curCounts.items():
        if k == 0:
            nextCounts[6] = nextCounts[6] + v
            nextCounts[8] = nextCounts[8] + v
        else:
            nextCounts[k-1] = nextCounts[k-1] + v
    return nextCounts

def main():
    curCounts = {}
    for i in range(0, 9):
        curCounts[i] = 0
    with open('Data.txt', 'r') as file:
        for line in file:
            for v in line.split(','):
                curCounts[int(v)] = curCounts[int(v)] + 1
    for i in range(0, 80):
        curCounts = step(curCounts)
    nfish = 0
    for k,v in curCounts.items():
        nfish = nfish + v
    print(nfish)
            
if __name__ == "__main__":
    main()
        
