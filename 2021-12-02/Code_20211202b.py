def main():
    with open('Data.txt', 'r') as file:
        horz = 0
        vert = 0
        aim = 0
        for line in file:
            tokens = line.split()
            direction = tokens[0]
            amount = int(tokens[1])
            if direction == "forward":
                horz = horz + amount
                vert = vert + aim*amount
            elif direction == "down":
                aim = aim + amount
            elif direction == "up":
                aim = aim - amount
    print(horz*vert)

if __name__ == "__main__":
    main()
