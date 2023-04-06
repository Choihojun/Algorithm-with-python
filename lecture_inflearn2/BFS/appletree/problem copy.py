# 직접 풀어보기
# BFS는 시작점에서 쫙 퍼지는 느낌이다 -> 시작점을 잘 선정하는게 중요하다

from collections import deque
N = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

a = [list(map(int, input().split())) for _ in range(N)]
ch = [[0] * N for _ in range(N)]
ch[N//2][N//2] = 1
sum = 0
sum = sum + a[N//2][N//2]


dQ = deque()
dQ.append((N//2, N//2))
L = 0  # Level

while True:
    if L == N//2:
        break
    size = len(dQ)  # 1이겠지
    for i in range(size):  # Level 탐색
        tmp = dQ.popleft()  # 여기서 하나가 나오면 무조건 4개를 돌아야함
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] != 1:
                sum = sum + a[x][y]
                ch[x][y] = 1
                dQ.append((x, y))
    L = L + 1
print(sum)
