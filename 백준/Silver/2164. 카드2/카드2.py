import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque([i for i in range(1, n+1)])

while len(queue) > 1:
    queue.popleft()  # 첫 번째 카드를 버림
    queue.append(queue.popleft())  # 두 번째 카드를 맨 뒤로 보냄

print(queue[0])  # 마지막 남은 한 장의 카드를 출력