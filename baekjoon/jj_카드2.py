from collections import deque
import sys

sys.stdin = open('input.txt','r')


def card(n):
    if n == 1 :
        return n

    cards = deque([i for i in range(1,n+1)])

    while len(cards) > 1 :
        cards.popleft()
        cards.append(cards.popleft())

    return cards[0]


n = int(input())
print(card(n))