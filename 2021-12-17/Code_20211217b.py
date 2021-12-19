import math

def GetVelRanges(txmin, txmax, tymin, tymax):
    vxmin = math.ceil((math.sqrt(1+8*txmin)-1)/2)
    vxmax = txmax
    vymin = tymin
    vymax = -1-tymin
    return vxmin, vxmax, vymin, vymax

def CheckSol(txmin, txmax, tymin, tymax, vx, vy):
    x = 0
    y = 0
    while True:
        if x >= txmin and x <= txmax and y >= tymin and y <= tymax:
            return True
        if x > txmax:
            return False
        if y < tymin:
            return False
        x += vx
        y += vy
        vx = max(vx - 1, 0)
        vy -= 1

def GetNumSol(txmin, txmax, tymin, tymax):
    vxmin, vxmax, vymin, vymax = GetVelRanges(txmin, txmax, tymin, tymax)
    numSol = 0
    for vx in range(vxmin, vxmax+1):
        for vy in range(vymin, vymax+1):
            if CheckSol(txmin, txmax, tymin, tymax, vx, vy):
                numSol += 1
    return numSol

def main():
    with open('Data.txt', 'r') as file:
        for line in file:
            s = line[15:]
            if s[-1] == '\n':
                s = s[:-1]
            toks = s.split(', y=')
            xtoks = toks[0].split('..')
            ytoks = toks[1].split('..')
            txmin = int(xtoks[0])
            txmax = int(xtoks[1])
            tymin = int(ytoks[0])
            tymax = int(ytoks[1])
    print(GetNumSol(txmin, txmax, tymin, tymax))
            
if __name__ == "__main__":
    main()
    
