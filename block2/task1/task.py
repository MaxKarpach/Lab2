class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed
    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
n = open('input.txt').readline()
f = open('input.txt').readlines()[1:]
numbers = []
stack = Stack()
for i in range(len(f)):
    if f[i].find('-'):
        stack.push(int(f[i][1:-1]))
    else:
        numbers.append(stack.peek())
        stack.pop()
r = open('output.txt', 'w')
for i in range(len(numbers)):
    r.write(str(numbers[i]) + '\n')
r.close()