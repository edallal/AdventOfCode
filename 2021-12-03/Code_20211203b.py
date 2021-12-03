def Filter(values, mask, mostCommon, defVal):
    numOnes = 0
    for v in values:
        if (v & mask) > 0:
            numOnes = numOnes + 1
    choice = 0
    if mostCommon:
        if 2*numOnes > len(values):
            choice = 1
        elif 2*numOnes < len(values):
            choice = 0
        else:
            choice = defVal
    else:
        if 2*numOnes > len(values):
            choice = 0
        elif 2*numOnes < len(values):
            choice = 1
        else:
            choice = defVal
    if choice == 1:
        return list(filter(lambda x: x & mask > 0, values))
    return list(filter(lambda x: x & mask == 0, values))

def GetOGR(values, nbits):
    mask = 1 << (nbits - 1)
    while len(values) > 1:
        values = Filter(values, mask, True, 1)
        mask = mask >> 1
    return values[0]

def GetCO2(values, nbits):
    mask = 1 << (nbits - 1)
    while len(values) > 1:
        values = Filter(values, mask, False, 0)
        mask = mask >> 1
    return values[0]

def main():
    values = []
    with open('Data.txt', 'r') as file:
        for line in file:
            values.append(int(line, 2))
    maxVal = max(values)
    nbits = 0
    while maxVal > 0:
        maxVal = maxVal >> 1
        nbits = nbits + 1
    ocr = GetOGR(values, nbits)
    co2 = GetCO2(values, nbits)
    print(ocr*co2)

if __name__ == "__main__":
    main()
        
