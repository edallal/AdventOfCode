def main():
    cnt = 0
    with open('Data.txt', 'r') as file:
        for line in file:
            inout = line.split(' | ')
            for s in inout[1].split():
                if len(s) in [2, 3, 4, 7]:
                    cnt += 1
    print(cnt)
            
if __name__ == "__main__":
    main()
    
