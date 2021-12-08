def main():
    values = []
    with open('Data.txt', 'r') as file:
        for line in file:
            for v in line.split(','):
                values.append(int(v))
    values.sort()
    median = values[len(values)//2]
    fuel = 0
    for v in values:
        fuel = fuel + abs(v - median)
    print(fuel)
            
if __name__ == "__main__":
    main()
        
