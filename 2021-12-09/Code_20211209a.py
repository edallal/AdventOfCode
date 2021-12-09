def toArr(s):
    arr = []
    for c in s:
        if c == '\n':
            continue
        arr.append(int(c))
    return arr

def main():
    mat = []
    risk = 0
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
            risk += (1 + mat[i][j])
    print(risk)
            
if __name__ == "__main__":
    main()
    
