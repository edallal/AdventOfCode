def getNextNumLoc(s, index):
    indStart = -1
    for i in range(index, len(s)):
        if s[i] in ['[', ']', ',']:
            if indStart == -1:
                continue
            return indStart, i
        if indStart == -1:
            indStart = i
    return -1, -1

def getPrevNumLoc(s, index):
    indStart = -1
    for i in range(index, -1, -1):
        if s[i] in ['[', ']', ',']:
            if indStart == -1:
                continue
            return i+1, indStart+1
        if indStart == -1:
            indStart = i
    return -1, -1

def explode(s, index):
    rvs, rve = getPrevNumLoc(s, index)
    rv = int(s[rvs:rve])
    lvs, lve = getPrevNumLoc(s, rvs-1)
    lv = int(s[lvs:lve])
    nrvs, nrve = getNextNumLoc(s, index)
    nlvs, nlve = getPrevNumLoc(s, lvs-1)
    snext = ''
    if nlvs == -1:
        snext += s[:lvs-1]
    else:
        snext += s[:nlvs]
        snext += str(int(s[nlvs:nlve])+lv)
        snext += s[nlve:lvs-1]
    snext += '0'
    if nrvs == -1:
        snext += s[index+1:]
    else:
        snext += s[index+1:nrvs]
        snext += str(int(s[nrvs:nrve])+rv)
        snext += s[nrve:]
    return snext
    
def split(s, istart, iend):
    val = int(s[istart:iend])
    snext = s[:istart] + '['
    snext += str(val//2)
    snext += ','
    snext += str(val - (val//2))
    snext += ']'
    snext += s[iend:]
    return snext

def reduce(s):
    while True:
        # Try explode
        depth = 0
        didExplode = False
        didSplit = False
        for i in range(len(s)):
            if s[i] == '[':
                depth += 1
            elif s[i] == ']':
                depth -= 1
            if s[i] == ']' and depth >= 4:
                didExplode = True
                s = explode(s, i)
                break
        if didExplode:
            continue
        indStart = -1
        for i in range(len(s)):
            if s[i] in ['[', ']', ',']:
                if indStart == -1:
                    continue
                if i - indStart == 1:
                    indStart = -1
                else:
                    didSplit = True
                    s = split(s, indStart, i)
                    break
            elif indStart == -1:
                indStart = i
        if didSplit:
            continue
        break
    return s

def add(s1, s2):
    s = '[' + s1 +',' + s2 + ']'
    return reduce(s)

def getMagnitude(s):
    if len(s) == 1:
        return int(s)
    depth = 0
    for i in range(len(s)):
        if s[i] == '[':
            depth += 1
        elif s[i] == ']':
            depth -= 1
        elif s[i] == ',' and depth == 1:
            return 3*getMagnitude(s[1:i]) + 2*getMagnitude(s[i+1:-1])

def main():
    ans = ''
    with open('Data.txt', 'r') as file:
        for line in file:
            s = line
            if s[-1] == '\n':
                s = s[:-1]
            if ans == '':
                ans = s
            else:
                ans = add(ans, s)
    print(ans)
    print(getMagnitude(ans))
            
if __name__ == "__main__":
    main()
    
