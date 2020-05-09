import sys

sys.stdin = open('input.txt','r')
n = int(input())
stack = []

for _ in range(n):
    num = int(input())
    if num == 0:
        stack.pop(-1)
    else:
        stack.append(num)

print(sum(stack))
