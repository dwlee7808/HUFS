from collections import deque

n, k = map(int, input().split())

MAX = 10**5 #최대값 100,000
visited = [0]*(MAX + 1) #방문 표기. 초기값 0. 0~100,000
check = [0]*(MAX +1)

def path(d):
    list = []
    temp = d
    for _ in range(visited[d] + 1):
        list.append(temp)
        temp = check[temp]
    return list[::-1]
    
    
    

def bfs(s): # 시작점 s
    q = deque() #큐 초기화
    q.append(s) 
    while q:
        cur = q.popleft() #cur 꺼내기
        if cur == k: # 목표지점 k라면
            return visited[k] # 반환
        for i in (cur +1, cur -1, cur * 2): #이동방법 3가지 
            if 0 <= i <= MAX and not visited[i]: #범위 내
                visited[i] = visited[cur] + 1 #방문 표시, 이동 횟수 +1
                check[i] = cur
                q.append(i) #해당 위치 추가
                
print(bfs(n))
print(' '.join(map(str, path(k))))