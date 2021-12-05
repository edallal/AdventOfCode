def GetSol(nums, valLocs, rowFillCnt, colFillCnt, boardSums):
    hasWon = {}
    for k in boardSums.keys():
        hasWon[k] = False
    numNotWon = len(hasWon)
    for val in nums:
        for t in valLocs[val]:
            rowFillCnt[t[0]][t[1]] = rowFillCnt[t[0]][t[1]] + 1
            colFillCnt[t[0]][t[2]] = colFillCnt[t[0]][t[2]] + 1
            boardSums[t[0]] = boardSums[t[0]] - val
            if rowFillCnt[t[0]][t[1]] == 5 or colFillCnt[t[0]][t[2]] == 5:
                if not hasWon[t[0]]:
                    hasWon[t[0]] = True
                    numNotWon = numNotWon - 1
                    if numNotWon == 0:
                        return val*boardSums[t[0]]

def main():
    nums = []
    boards = {}
    boardSums = {}
    valLocs = {}
    rowFillCnt = {}
    colFillCnt = {}
    with open('Data.txt', 'r') as file:
        lineNum = 0
        boardNum = -1
        row = 0
        for line in file:
            if lineNum == 0:
                nums = list(map(int, filter(None, line.split(','))))
            elif lineNum % 6 == 1:
                boardNum = boardNum + 1
                row = 0
            else:
                vals = list(map(int, filter(None, line.split(' '))))
                if row == 0:
                    boards[boardNum] = {}
                    boardSums[boardNum] = 0
                    rowFillCnt[boardNum] = {}
                    colFillCnt[boardNum] = {}
                    for i in range(0, 5):
                        rowFillCnt[boardNum][i] = 0
                        colFillCnt[boardNum][i] = 0
                boards[boardNum][row] = {}
                for col in range(0, len(vals)):
                    boards[boardNum][row][col] = vals[col]
                    boardSums[boardNum] = boardSums[boardNum] + vals[col]
                    if vals[col] not in valLocs:
                        valLocs[vals[col]] = []
                    valLocs[vals[col]].append((boardNum, row, col))
                row = row + 1
            lineNum = lineNum + 1
    print(GetSol(nums, valLocs, rowFillCnt, colFillCnt, boardSums))
                
if __name__ == "__main__":
    main()
        
