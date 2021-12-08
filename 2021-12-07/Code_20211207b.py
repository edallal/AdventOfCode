def EvalFuel(values, pos):
    fuel = 0
    for v in values:
        fuel = fuel + abs(v - pos)*(abs(v - pos) + 1)/2
    return fuel

def TriSearch(values, low, high):
    if high - low <= 2.5:
        fuelL = EvalFuel(values, low)
        fuelM = EvalFuel(values, (low + high)//2)
        fuelH = EvalFuel(values, high)
        return min(fuelL, fuelM, fuelH)
    medL = (2*low + high)//3
    medH = (low + 2*high)//3
    fuelL = EvalFuel(values, medL)
    fuelH = EvalFuel(values, medH)
    if fuelL < fuelH:
        return TriSearch(values, low, medH)
    return TriSearch(values, medL, high)

def main():
    values = []
    with open('Data.txt', 'r') as file:
        for line in file:
            for v in line.split(','):
                values.append(int(v))
    print(TriSearch(values, min(values), max(values)))
            
if __name__ == "__main__":
    main()
