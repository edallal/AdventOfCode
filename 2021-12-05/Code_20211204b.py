def main():
    maxX = 0
    maxY = 0
    lines = []
    with open('Data.txt', 'r') as file:
        for line in file:
            toks = line.split(" -> ")
            p1 = toks[0].split(',')
            p2 = toks[1].split(',')
            x1 = int(p1[0])
            y1 = int(p1[1])
            x2 = int(p2[0])
            y2 = int(p2[1])
            lines.append((x1, y1, x2, y2))
            if x1 > maxX:
                maxX = x1
            if x2 > maxX:
                maxX = x2
            if y1 > maxY:
                maxY = y1
            if y2 > maxY:
                maxY = y2
    arr = [[0]*(maxY+1) for i in range(maxX+1)]
    for ln in lines:
        if ln[0] == ln[2]:
            for y in range(min(ln[1], ln[3]), max(ln[1], ln[3])+1):
                arr[ln[0]][y] = arr[ln[0]][y] + 1
        elif ln[1] == ln[3]:
            for x in range(min(ln[0], ln[2]), max(ln[0], ln[2])+1):
                arr[x][ln[1]] = arr[x][ln[1]] + 1
        else:
            dx = 0
            dy = 0
            if ln[2] > ln[0]:
                dx = 1
            else:
                dx = -1
            if ln[3] > ln[1]:
                dy = 1
            else:
                dy = -1
            x = ln[0]
            y = ln[1]
            for i in range(abs(ln[2]-ln[0])+1):
                arr[x][y] = arr[x][y] + 1
                x = x + dx
                y = y + dy
    cnt = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] > 1:
                cnt = cnt + 1
    print(cnt)
            
if __name__ == "__main__":
    main()
        
