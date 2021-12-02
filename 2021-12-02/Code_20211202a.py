def main():
    with open('Data.txt', 'r') as file:
        horz = 0
        vert = 0
        for line in file:
            tokens = line.split()
            direction = tokens[0]
            amount = int(tokens[1])
            if direction == "forward":
                horz = horz + amount
            elif direction == "down":
                vert = vert + amount
            elif direction == "up":
                vert = vert - amount
    print(horz*vert)

if __name__ == "__main__":
    main()
