def Convert2Index(mat):
    val = 0
    for i in range(3):
        for c in mat[i]:
            val *= 2
            if c == '#':
                val += 1
    return val

def AddPadding(mat, c):
    mat2 = []
    for i in range(len(mat)+4):
        row = ''
        for j in range(len(mat[0])+4):
            if i < 2 or j < 2 or i >= len(mat) + 2 or j >= len(mat[0]) + 2:
                row += c
            else:
                row += mat[i-2][j-2]
        mat2.append(row)
    return mat2

def ApplyFilter(mat, c, filt):
    mat2 = []
    for i in range(1, len(mat)-1):
        row = ''
        for j in range(1, len(mat[0])-1):
            row += filt[Convert2Index([mat[k][j-1:j+2] for k in range(i-1, i+2)])]
        mat2.append(row)
    if c == '.':
        return mat2, filt[0]
    return mat2, filt[511]

def Enhance(mat, c, filt):
    mat2 = AddPadding(mat, c)
    return ApplyFilter(mat2, c, filt)

def Count(mat):
    lit = 0
    for row in mat:
        for c in row:
            if c == '#':
                lit += 1
    return lit

def PrintMat(mat):
    for row in mat:
        print(row)
    print('')

def main():
    nrow = 0
    mat = []
    with open('Data.txt', 'r') as file:
        for line in file:
            nrow += 1
            s = line
            if s[-1] == '\n':
                s = s[:-1]
            if nrow == 1:
                filt = s
            elif nrow > 2:
                mat.append(s)
    c = '.'
    for i in range(50):
        mat, c = Enhance(mat, c, filt)
    print(Count(mat))
            
if __name__ == "__main__":
    main()
    
