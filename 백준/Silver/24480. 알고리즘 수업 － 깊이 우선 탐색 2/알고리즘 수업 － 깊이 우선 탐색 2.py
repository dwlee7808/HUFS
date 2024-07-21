import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, r = map(int,input().split())
link = [[] for _ in range(n+1)]


for _ in range (m):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)
    
visited = [0]*(n+1)
visited[r] = 1
count = 1


def dfs(v):
    global count
    link[v].sort(reverse = True)
    for i in link[v]:
        if visited[i] == 0:
            count += 1
            visited[i] = count
            dfs(i)
            
dfs(r)

for i in range (1, n+1):
    print(visited[i])