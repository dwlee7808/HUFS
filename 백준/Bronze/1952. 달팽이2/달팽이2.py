m, n = map(int, input().split())
c = 0

x, y = 0, 0
dir_num = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 2차원 배열 생성
arr = [[0]*n for _ in range(m)]

for i in range(m * n-1):
    arr[y][x] = i + 1  # 전진
    nx, ny = x + dx[dir_num], y + dy[dir_num]

    if nx < 0 or nx >= n or ny < 0 or ny >= m or arr[ny][nx] != 0:  # 범위 벗어나거나 숫자가 있으면 회전
        dir_num = (dir_num + 1) % 4
        c += 1  # 카운트
        nx, ny = x + dx[dir_num], y + dy[dir_num]

    x, y = nx, ny

print(c)