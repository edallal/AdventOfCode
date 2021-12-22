def Inc(pos, cur):
    return (pos + 3*cur + 2) % 10 + 1

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
    cur = 1
    while True:
        pos1 = Inc(pos1, cur)
        score1 += pos1
        cur += 3
        if score1 >= 1000:
            print((cur-1)*score2)
            break
        pos2 = Inc(pos2, cur)
        score2 += pos2
        cur += 3
        if score2 >= 1000:
            print((cur-1)*score1)
            break
            
if __name__ == "__main__":
    main()
    
