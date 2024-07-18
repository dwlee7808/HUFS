n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
s = []

def dfs(start):
    if len(s) == m:
        print(*s)
        return
    for i in range(start, n):
        if num[i] not in s:
            s.append(num[i])
            dfs(i+1)
            s.pop()

dfs(0)