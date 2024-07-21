import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) #재귀 최대 깊이 설정. 런타임 에러 해결

n, m, r = map(int,input().split()) #n, m, r 입력
link = [[] for _ in range(n+1)] #인접 리스트로 그래프 생성


for _ in range (m):
    a, b = map(int, input().split())
    link[a].append(b) 
    link[b].append(a) #입력받은 a, b 연결. 인접 리스트에 추가
    
visited = [0]*(n+1) #visited 리스트로 방문 순서 저장
visited[r] = 1 #
count = 1 #방문 순서


def dfs(v):
    global count
    link[v].sort(reverse = True) #내림차순으로 정렬
    for i in link[v]:
        if visited[i] == 0: #방문하지 않은 정점 
            count += 1 
            visited[i] = count
            dfs(i)
            
dfs(r) # 시작 정점 r

for i in range (1, n+1):
    print(visited[i])