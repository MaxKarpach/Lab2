class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.insert(0, item)

    def pop(self):
        if len(self.queue) == 0:
            return None
        removed = self.queue.pop()
        return removed
    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[-1]
n = open('input.txt').readline()
f = open('input.txt').readlines()[1:]
numbers = []
queue = Queue()
for i in range(len(f)):
    if f[i].find('-'):
        queue.push(int(f[i][1:-1]))
    else:
        numbers.append(queue.peek())
        queue.pop()
r = open('output.txt', 'w')
for i in range(len(numbers)):
    r.write(str(numbers[i]) + '\n')
r.close()