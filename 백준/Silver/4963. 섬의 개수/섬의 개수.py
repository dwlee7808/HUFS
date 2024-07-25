import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y): #dfs 재귀
  dx = [1, 1, -1, -1, 1, -1, 0, 0]
  dy = [0, 1, 0, 1, -1, -1, 1, -1] #대각선까지 8방향 

  field[x][y] = 0 #field 초기화. 0이면 바다 1이면 섬
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
      dfs(nx, ny)

while True: #부울로 무한 루프
  w, h = map(int, read().split()) #너비와 높이 입력
  if w == 0 and h == 0: #둘 다 0이면 탈출
        break
  field = []
  count = 0 #카운트 초기화
  for _ in range(h):
    field.append(list(map(int, read().split())))
  for i in range(h):
    for j in range(w):
      if field[i][j] == 1: #1이면 현재가 섬. 1일 때 dfs 호출
        dfs(i, j) 
        count += 1 #카운트 증가
  
  print(count)