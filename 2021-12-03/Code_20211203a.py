def main():
    values = []
    with open('Data.txt', 'r') as file:
        for line in file:
            values.append(int(line, 2))
    gamma = 0
    epsilon = 0
    maxVal = max(values)
    nbits = 0
    while maxVal > 0:
        maxVal = maxVal >> 1
        nbits = nbits + 1
    numOnes = {}
    for i in range(0, nbits):
        numOnes[i] = 0
    for v in values:
        for i in range(0, nbits):
            if (v & 1) == 1:
                numOnes[i] = numOnes[i] + 1
            v = v >> 1
    for i in range(0, nbits):
        if 2*numOnes[i] > len(values):
            gamma = gamma + (1 << i)
        else:
            epsilon = epsilon + (1 << i)
    print(gamma*epsilon)

if __name__ == "__main__":
    main()
        
