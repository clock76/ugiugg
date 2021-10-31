class Stack:
    def __init__(self):
        self.value = []

    def push(self, item):
        self.value.append(item)

    def pop(self):
        if len(self.value):
            return self.value.pop()
        else:
            print('Empty Stack')

    def peek(self):
        if len(self.value):
            return self.value[-1]
        else:
            print('Empty Stack')
            return None

    def is_empty(self):
        if len(self.value) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.value)

aboba = Stack()
aboba.peek()
print(aboba.is_empty())
aboba.push('cat')
aboba.push('dog')
print(aboba.peek())
aboba.push(True)
print(aboba.size())
print(aboba.is_empty())
aboba.push(777)
print(aboba.pop())
print(aboba.pop())
print(aboba.size())