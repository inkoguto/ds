class Stack:
    top = -1
    stack = []
    max_size = 10

    def __init__(self):
        self.top = -1
        self.stack = []
        self.max_size = 10

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top + 1 == self.max_size

    def push(self, data):
        assert not self.is_full()
        self.top += 1
        self.stack.append(data)

    def pop(self):
        assert not self.is_empty()
        data = self.stack[self.top]
        self.top -= 1

        return data

    def peek(self):
        return self.stack[self.top]
