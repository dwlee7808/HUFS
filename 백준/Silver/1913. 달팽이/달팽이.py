n = int(input())
target = int(input())

x, y = 0, 0
dir_num = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 2차원 배열 생성
arr = [[0]*n for _ in range(n)]

for i in range(n * n, 0, -1):
    arr[y][x] = i  # 현재 위치 숫자 입력
    nx, ny = x + dx[dir_num], y + dy[dir_num]

    if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[ny][nx] != 0:  # 범위 벗어나거나 숫자가 있으면 회전
        dir_num = (dir_num + 1) % 4
        nx, ny = x + dx[dir_num], y + dy[dir_num]


    x, y = nx, ny
    
for row in arr:
    print(" ".join(map(str, row)))
    
found = False
for i in range(n):
    for j in range(n):
        if arr[i][j] == target:
            print(i+1, j+1)
            found = True
            break