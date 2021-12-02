import pandas as pd

def main():
    data = pd.read_csv('data.txt', names=['Depth'])
    count = 0;
    for i in range(0, data.size - 3):
        if data.iloc[i+3, 0] > data.iloc[i, 0]:
            count = count + 1
    print(count)

if __name__ == "__main__":
    main()
