def getDigit(digit, backwardMap):
    decDig = []
    for c in digit:
        decDig.append(backwardMap[c])
    decDig.sort()
    decStr = "".join(decDig)
    seg2Num = {'abcefg':0, 'cf':1, 'acdeg':2, 'acdfg':3, 'bcdf':4,\
               'abdfg':5, 'abdefg':6, 'acf':7, 'abcdefg':8, 'abcdfg':9}
    if decStr not in seg2Num:
        print('Unknown digit: ', decStr)
    return seg2Num[decStr]

def decode(inp, out):
    print(inp, out)
    freq = {}
    for c in 'abcdefg':
        freq[c] = 0
    for digit in inp:
        for c in digit:
            freq[c] += 1
    acPoss = []
    dgPoss = []
    backwardMap = {}
    for c in 'abcdefg':
        if freq[c] == 4:
            backwardMap[c] = 'e'
        elif freq[c] == 6:
            backwardMap[c] = 'b'
        elif freq[c]== 7:
            dgPoss.append(c)
        elif freq[c] == 8:
            acPoss.append(c)
        elif freq[c] == 9:
            backwardMap[c] = 'f'
    for digit in inp:
        if len(digit) == 2:
            for c in acPoss:
                if c in digit:
                    backwardMap[c] = 'c'
                else:
                    backwardMap[c] = 'a'
        elif len(digit) == 4:
            for c in dgPoss:
                if c in digit:
                    backwardMap[c] = 'd'
                else:
                    backwardMap[c] = 'g'
    val = 0
    for digit in out:
        val *= 10
        val += getDigit(digit, backwardMap)
    print(val)
    return val

def main():
    inputs = []
    outputs = []
    with open('Data.txt', 'r') as file:
        for line in file:
            inout = line.split(' | ')
            inputs.append(inout[0].split())
            outputs.append(inout[1].split())
    valSum = 0
    for lineNum in range(len(inputs)):
        valSum += decode(inputs[lineNum], outputs[lineNum])
    print(valSum)
            
if __name__ == "__main__":
    main()
    
