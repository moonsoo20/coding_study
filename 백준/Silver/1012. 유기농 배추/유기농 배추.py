import sys
from collections import deque

input = sys.stdin.readline

def bfs(tx, ty):
    dq = deque()
    dq.append((tx, ty))
    v[tx][ty] = 1
    cnt = 0
    while dq:
        mx, my = dq.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rx, ry = mx + dx, my + dy
            if 0 <= rx < N and 0 <= ry < M and v[rx][ry] == 0 and arr[rx][ry] == 1:
                dq.append((rx, ry))
                v[rx][ry] = 1
    cnt += 1
    return cnt

T = int(input())
ans = []

for _ in range(T):
    M, N, K = map(int, input().split())

    arr = [[0] * M for _ in range(N)]
    v = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    result = 0
    for i in range(N):
        for j in range(M):
            if v[i][j] == 0 and arr[i][j] == 1:
                result += bfs(i, j)

    ans.append(result)

print(*ans, sep=' ')
