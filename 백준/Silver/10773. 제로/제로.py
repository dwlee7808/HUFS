import sys
input = sys.stdin.readline

K = int(input())
stack = []

for i in range(K):
    X = int(input())
    if X == 0:
    
        top = stack.pop()
    else:
    
        stack.append(X)
    
print(sum(stack))