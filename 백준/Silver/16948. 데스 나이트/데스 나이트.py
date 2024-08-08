import sys
from collections import deque

n = int(sys.stdin.readline()) #격자 크기 입력
r1, c1, r2, c2 = map(int, sys.stdin.readline().split()) #r1, c1 : 시작점 행,렬 r2, c2 : 출발점 행, 렬
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1] #말이 이동할 수 있는 방향 6가지
visited = [[-1] * n for _ in range(n)] #방문 표시. 2차원 배열로

def bfs():
    q = deque() #큐로 bfs 구현
    q.append((r1, c1)) #시작점을 추가
    visited[r1][c1] = 0 #방문 표시
    while q:
        r, c = q.popleft() #현재 위치를 꺼내고
        for i in range(6):
            nr = r + dx[i]
            nc = c + dy[i] #새로운 위치 탐색
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == -1: #nr,nc가 범위 내& 탐색 x라면
                q.append((nr, nc)) #추가
                visited[nr][nc] = visited[r][c] + 1 #횟수 기록
                if nr == r2 and nc == c2:
                    return visited[r2][c2] #방문 횟수 반환
    return -1 #목표 지점 도달 못하는 경우 불가능
print(bfs())