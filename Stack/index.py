class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return -1
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return -1
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0


s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)


