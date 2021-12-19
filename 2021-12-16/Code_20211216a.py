def hex2bin(sh):
    m = {"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100", \
         "5":"0101", "6":"0110", "7":"0111", "8":"1000", "9":"1001", \
         "A":"1010", "B":"1011", "C":"1100", "D":"1101", "E":"1110", \
         "F":"1111"}
    sb = ""
    for c in sh:
        sb += m[c]
    return sb

def bin2num(sb):
    num = 0
    for c in sb:
        num *= 2
        num += int(c)
    return num

class Node:
    def __init__(self):
        self.version = 0
        self.type = 0
        self.value = 0
        self.children = []

    def __str__(self):
        return "Version: " + str(self.version)\
               + ", Type: " + str(self.type)\
               + ", Value: " + str(self.value)

    def parse(self, packet):
        index = 0
        self.version = bin2num(packet[index:index+3])
        index += 3
        self.type = bin2num(packet[index:index+3])
        index += 3
        if self.type == 4:
            valstring = ""
            while True:
                valstring += packet[index+1:index+5]
                if packet[index] == '0':
                    self.value = bin2num(valstring)
                    index += 5
                    break
                index += 5
        else:
            if packet[index] == '0':
                index += 1
                numbits = bin2num(packet[index:index+15])
                index += 15
                while numbits > 0:
                    child = Node()
                    used = child.parse(packet[index:])
                    self.children.append(child)
                    numbits -= used
                    index += used
            else:
                index += 1
                numsub = bin2num(packet[index:index+11])
                index += 11
                while numsub > 0:
                    child = Node()
                    used = child.parse(packet[index:])
                    self.children.append(child)
                    index += used
                    numsub -= 1
            if self.type == 0:
                for child in self.children:
                    self.value += child.value
            elif self.type == 1:
                self.value = 1
                for child in self.children:
                    self.value *= child.value
            elif self.type == 2:
                self.value = -1
                for child in self.children:
                    if self.value == -1:
                        self.value = child.value
                    else:
                        self.value = min(self.value, child.value)
            elif self.type == 3:
                for child in self.children:
                    self.value = max(self.value, child.value)
            elif self.type == 5:
                if self.children[0].value > self.children[1].value:
                    self.value = 1
            elif self.type == 6:
                if self.children[0].value < self.children[1].value:
                    self.value = 1
            elif self.type == 7:
                if self.children[0].value == self.children[1].value:
                    self.value = 1
        return index

def PrintTree(nod, depth = 0):
    for i in range(depth):
        print('\t', end = '')
    print(nod)
    for n in nod.children:
        PrintTree(n, depth+1)

def GetVersionSum(nod):
    vs = nod.version
    for n in nod.children:
        vs += GetVersionSum(n)
    return vs

def main():
    mat = []
    with open('Data.txt', 'r') as file:
        for line in file:
            sh = line
            if sh[-1] == '\n':
                sh = sh[:-1]
            sb = hex2bin(sh)
            break
    nod = Node()
    nod.parse(sb)
    PrintTree(nod)
            
if __name__ == "__main__":
    main()
    
