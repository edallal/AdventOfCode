from collections import deque

class Stack:
    def __init__(self):
        """
        Initializing Stack.
        """
        self.stack = deque()

    def isEmpty(self) -> bool:
        return True if len(self.stack) == 0 else False

    def length(self) -> int:
        return len(self.stack)

    def top(self) -> int:
        return self.stack[-1]  

    def push(self, x: int) -> None:
        self.x = x
        self.stack.append(x)   

    def pop(self) -> None:
        self.stack.pop()

def scoreLine(s):
    scoreMap = {')':3, ']':57, '}':1197, '>':25137}
    closeOpenMap = {')':'(', ']':'[', '}':'{', '>':'<'}
    stack = Stack()
    for c in s:
        if c in ('(', '[', '{', '<'):
            stack.push(c)
        elif c in (')', ']', '}', '>'):
            if stack.top() == closeOpenMap[c]:
                stack.pop()
            else:
                return scoreMap[c]
    return 0

def main():
    score = 0
    with open('Data.txt', 'r') as file:
        for line in file:
            if line[-1] == '\n':
                score += scoreLine(line[:-1])
            else:
                score += scoreLine(line)
    print(score)
            
if __name__ == "__main__":
    main()
    
