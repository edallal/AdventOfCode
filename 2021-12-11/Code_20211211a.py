def tryAdj(mat, isVisited, x, y, dx, dy):
    if x + dx >= 0 and x + dx < 10 and y + dy >= 0 and y + dy < 10:
        if mat[x+dx][y+dy] < 10:
            mat[x+dx][y+dy] += 1
        if mat[x+dx][y+dy] == 10 and not isVisited[x+dx][y+dy]:
            doDFS(mat, isVisited, x+dx, y+dy)

def doDFS(mat, isVisited, x, y):
    isVisited[x][y] = True
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx != 0 or dy != 0:
                tryAdj(mat, isVisited, x, y, dx, dy)

def step(mat):
    isVisited = []
    for i in range(10):
        isVisited.append([False]*10)
    for i in range(10):
        for j in range(10):
            if mat[i][j] < 10:
                mat[i][j] += 1
            if mat[i][j] == 10 and not isVisited[i][j]:
                doDFS(mat, isVisited, i, j)
    numFlashes = 0
    for i in range(10):
        for j in range(10):
            if mat[i][j] == 10:
                mat[i][j] = 0
                numFlashes += 1
    return numFlashes

def main():
    mat = []
    numFlashes = 0
    with open('Data.txt', 'r') as file:
        for line in file:
            arr = []
            for c in line:
                if c != '\n':
                    arr.append(int(c))
            mat.append(arr)
    for s in range(100):
        numFlashes += step(mat)
    print(numFlashes)
            
if __name__ == "__main__":
    main()
    
