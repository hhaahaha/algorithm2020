import sys

input=sys.stdin.readline

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        if self.stack :
            out = self.stack.pop()
            return out
        else:
            return -1

    def size(self):
        return len(self.stack)

    def empty(self):
        if self.stack:
            return 0
        else:
            return 1

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1

    def command(self,comm):
        if comm == 'pop':
            return self.pop()
        elif comm == 'size':
            return self.size()
        elif comm == 'empty':
            return self.empty()
        elif comm == 'top':
            return self.top()

new = Stack()
n = int(input())
for _ in range(n):
    command = list(input().split())
    commander = command[0]
    if commander == 'push':
        new.push(command[1])
    else: print(new.command(commander))