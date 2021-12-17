def applyRules(poly, rules):
    nextPoly = ''
    for i in range(0, len(poly) - 1, 1):
        nextPoly += poly[i]
        for rule in rules:
            if poly[i:i+2] == rule[0]:
                nextPoly += rule[1]
                continue
    nextPoly += poly[-1]
    return nextPoly

def getFreqDif(poly):
    counts = {}
    for c in poly:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
    minFreq = len(poly)
    maxFreq = 0
    for c in counts:
        minFreq = min(minFreq, counts[c])
        maxFreq = max(maxFreq, counts[c])
    return maxFreq - minFreq

def main():
    rules = []
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
            rules.append((rule[0], rule[1]))
    for i in range(10):
        poly = applyRules(poly, rules)
    print(getFreqDif(poly))
            
if __name__ == "__main__":
    main()
    
