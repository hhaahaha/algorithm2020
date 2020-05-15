# from collections import deque
import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

class Queue:
    def __init__(self):
        self.queue = list()
        self._top = 0
        self._end = 0

    def push(self,x):
        self.queue.append(x)
        self._end += 1

    def pop(self):
        if self._end == self._top:
            return -1

        else:
            ele = self.queue[self._top]
            self._top += 1
            return ele

    def size(self):
        return self._end - self._top

    def empty(self):
        if self._end == self._top : return 1
        else: return 0

    def front(self):
        if self._end == self._top: return -1
        else: return self.queue[self._top]

    def back(self):
        if self._end == self._top: return -1
        else: return self.queue[self._end-1]


new = Queue()
n = int(input())
for _ in range(n):
    command = list(input().split())
    commander = command[0]
    if commander == 'push':
        new.push(command[1])
    elif commander == 'pop':
        print(new.pop())
    elif commander == 'size':
        print(new.size())
    elif commander == 'empty':
        print(new.empty())
    elif commander == 'front':
        print(new.front())
    elif commander == 'back':
        print(new.back())

