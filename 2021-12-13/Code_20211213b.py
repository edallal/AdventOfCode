def printMat(mat, xsize, ysize):
    for j in range(ysize):
        for i in range(xsize):
            if mat[i][j] > 0:
                print('.', end = '')
            else:
                print(' ', end = '')
        print('')

def countDots(mat, xsize, ysize):
    dots = 0
    for i in range(xsize):
        for j in range(ysize):
            if mat[i][j] > 0:
                dots += 1
    return dots

def makeFold(mat, xsize, ysize, axis, value):
    if axis == 'x':
        for x in range(value + 1, xsize):
            for y in range(ysize):
                mat[2*value - x][y] += mat[x][y]
    else:
        for x in range(xsize):
            for y in range(value + 1, ysize):
                mat[x][2*value - y] += mat[x][y]

def makeMat(point_list):
    xmax = 0
    ymax = 0
    for p in point_list:
        xmax = max(xmax, p[0])
        ymax = max(ymax, p[1])
    mat = []
    for i in range(xmax+1):
        mat.append([0]*(ymax+1))
    for p in point_list:
        mat[p[0]][p[1]] = 1
    return mat

def main():
    point_list = []
    fold_list = []
    reading_points = True
    with open('Data.txt', 'r') as file:
        for line in file:
            s = line
            if s[-1] == '\n':
                s = s[:-1]
            if s == "":
                reading_points = False
                continue
            if reading_points:
                p = s.split(',')
                point_list.append((int(p[0]), int(p[1])))
            else:
                fold_list.append((s[11], int(s[13:])))
    mat = makeMat(point_list)
    xsize = len(mat)
    ysize = len(mat[0])
    for fold in fold_list:
        makeFold(mat, xsize, ysize, fold[0], fold[1])
        if fold[0] == 'x':
            xsize = fold[1]
        else:
            ysize = fold[1]
    printMat(mat, xsize, ysize)
            
if __name__ == "__main__":
    main()
    
