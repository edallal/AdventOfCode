import heapq
import pdb

def doDFS(mat, visitMap, i, j):
    visitMap[i][j] = True
    if i > 0 and mat[i-1][j] < 9 and (not visitMap[i-1][j]):
        doDFS(mat, visitMap, i-1, j)
    if i < len(mat) - 1 and mat[i+1][j] < 9 and (not visitMap[i+1][j]):
        doDFS(mat, visitMap, i+1, j)
    if j > 0 and mat[i][j-1] < 9 and (not visitMap[i][j-1]):
        doDFS(mat, visitMap, i, j-1)
    if j < len(mat[i]) - 1 and mat[i][j+1] < 9 and (not visitMap[i][j+1]):
        doDFS(mat, visitMap, i, j+1)

def getBasin(mat, x, y):
    visitMap = []
    for i in range(len(mat)):
        visitMap.append([False]*len(mat[i]))
    doDFS(mat, visitMap, x, y)
    cnt = 0
    for row in visitMap:
        for v in row:
            if v == True:
                cnt += 1
    return cnt

def toArr(s):
    arr = []
    for c in s:
        if c == '\n':
            continue
        arr.append(int(c))
    return arr

def main():
    mat = []
    H = [0,0,0]
    heapq.heapify(H)
    with open('Data.txt', 'r') as file:
        for line in file:
            mat.append(toArr(line))
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if j > 0 and mat[i][j] >= mat[i][j-1]:
                continue
            if j < len(mat[i]) - 1 and mat[i][j] >= mat[i][j+1]:
                continue
            if i > 0 and mat[i][j] >= mat[i-1][j]:
                continue
            if i < len(mat) - 1 and mat[i][j] >= mat[i+1][j]:
                continue
            bsize = getBasin(mat, i, j)
            print(i, j, bsize)
            if bsize > H[0]:
                heapq.heapreplace(H,bsize)
    print(H[0],H[1],H[2])
    print(H[0]*H[1]*H[2])
            
if __name__ == "__main__":
    main()
    
