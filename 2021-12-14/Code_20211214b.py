def applyRules(pairCounts, first, last, rules):
    nextPairCounts = {}
    for p in pairCounts:
        if p not in rules:
            if p not in nextPairCounts:
                nextPairCounts[p] = 0
            nextPairCounts[p] += pairCounts[p]
        else:
            p1 = p[0] + rules[p]
            p2 = rules[p] + p[1]
            if p1 not in nextPairCounts:
                nextPairCounts[p1] = 0
            nextPairCounts[p1] += pairCounts[p]
            if p2 not in nextPairCounts:
                nextPairCounts[p2] = 0
            nextPairCounts[p2] += pairCounts[p]
    if first in rules:
        first = first[0] + rules[first]
    if last in rules:
        last = rules[last] + last[1]
    return nextPairCounts, first, last

def getFreqDif(pairCounts, first, last):
    counts = {}
    for p in pairCounts:
        if p[0] not in counts:
            counts[p[0]] = 0
        counts[p[0]] += pairCounts[p]
        if p[1] not in counts:
            counts[p[1]] = 0
        counts[p[1]] += pairCounts[p]
    counts[first[0]] += 1
    counts[last[1]] += 1
    minFreq = -1
    maxFreq = 0
    for c in counts:
        if minFreq == -1:
            minFreq = counts[c]
        else:
            minFreq = min(minFreq, counts[c])
        maxFreq = max(maxFreq, counts[c])
    return (maxFreq - minFreq)//2

def getPairCounts(poly):
    pairCounts = {}
    for i in range(len(poly)-1):
        if poly[i:i+2] not in pairCounts:
            pairCounts[poly[i:i+2]] = 0
        pairCounts[poly[i:i+2]] += 1
    return pairCounts, poly[0:2], poly[-2:]

def main():
    rules = {}
    lineNum = 0
    with open('Data.txt', 'r') as file:
        for line in file:
            lineNum += 1
            if lineNum == 1:
                poly = line[:-1]
                continue
            if lineNum == 2:
                continue
            s = line
            if s[-1] == '\n':
                s = s[:-1]
            rule = s.split(' -> ')
            rules[rule[0]] = rule[1]
    pairCounts, first, last = getPairCounts(poly)
    for i in range(40):
        pairCounts, first, last = applyRules(pairCounts, first, last, rules)
    print(getFreqDif(pairCounts, first, last))
            
if __name__ == "__main__":
    main()
    
