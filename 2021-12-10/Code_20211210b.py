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
    scoreMap = {'(':1, '[':2, '{':3, '<':4}
    closeOpenMap = {')':'(', ']':'[', '}':'{', '>':'<'}
    stack = Stack()
    for c in s:
        if c in ('(', '[', '{', '<'):
            stack.push(c)
        elif c in (')', ']', '}', '>'):
            if stack.top() == closeOpenMap[c]:
                stack.pop()
            else:
                return 0
    score = 0
    print(s)
    while not stack.isEmpty():
        score *= 5
        score += scoreMap[stack.top()]
        stack.pop()
    return score

def main():
    scores = []
    with open('Data.txt', 'r') as file:
        for line in file:
            if line[-1] == '\n':
                score = scoreLine(line[:-1])
                if score > 0:
                    print(score)
                    scores.append(score)
            else:
                score = scoreLine(line)
                if score > 0:
                    scores.append(score)
    scores.sort()
    print(scores)
    print(scores[(len(scores)-1)//2])
            
if __name__ == "__main__":
    main()
    
