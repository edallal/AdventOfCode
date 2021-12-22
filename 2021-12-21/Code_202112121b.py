def SolveDP(sols):
    rollMultMap = {6:1, 5:3, 4:6, 3:7, 2:6, 1:3, 0:1}
    for tot in range(1, 42):
        for s1 in range(0, min(tot, 21)+1):
            s2 = tot - s1
            if s2 > 21:
                continue
            for p1 in range(1, min(s1, 10)+1):
                for r in rollMultMap:
                    for p2 in range(1, 11):
                        cur = (s1, s2, p1, p2, False)
                        if cur not in sols:
                            sols[cur] = 0
                        prev = (s1-p1, s2, (r+p1)%10+1, p2, True)
                        if prev in sols:
                            sols[cur] += (rollMultMap[r]*sols[prev])
                        if s1 == 21:
                            for pp1 in range(s1-p1+1, 21):
                                prev = (pp1, s2, (r+p1)%10+1, p2, True)
                                if prev in sols:
                                    sols[cur] += (rollMultMap[r]*sols[prev])
            for p2 in range(1, min(s2, 10)+1):
                for r in rollMultMap:
                    for p1 in range(1, 11):
                        cur = (s1, s2, p1, p2, True)
                        if cur not in sols:
                            sols[cur] = 0
                        prev = (s1, s2-p2, p1, (r+p2)%10+1, False)
                        if prev in sols:
                            sols[cur] += (rollMultMap[r]*sols[prev])
                        if s2 == 21:
                            for pp2 in range(s2-p2+1, 21):
                                prev = (s1, pp2, p1, (r+p2)%10+1, False)
                                if prev in sols:
                                    sols[cur] += (rollMultMap[r]*sols[prev])
                

def Solve(pos1, pos2):
    sols = {}
    for p1 in range(1, 11):
        for p2 in range(1, 11):
            sols[(0, 0, p1, p2, True)] = 0
            sols[(0, 0, p1, p2, False)] = 0
    sols[(0, 0, pos1, pos2, True)] = 1
    SolveDP(sols)
    win1num = 0
    win2num = 0
    for s2 in range(0, 21):
        for p1 in range(1, 11):
            for p2 in range(1, 11):
                win1num += sols[(21, s2, p1, p2, False)]
    for s1 in range(0, 21):
        for p1 in range(1, 11):
            for p2 in range(1, 11):
                win2num += sols[(s1, 21, p1, p2, True)]
    return max(win1num, win2num)

def main():
    score1 = 0
    score2 = 0
    linenum = 0
    with open('Data.txt', 'r') as file:
        for line in file:
            linenum += 1
            s = line
            if s[-1] == '\n':
                s = s[:-1]
            if linenum == 1:
                pos1 = int(s[28:])
            elif linenum == 2:
                pos2 = int(s[28:])
    print(Solve(pos1, pos2))
            
if __name__ == "__main__":
    main()
    
