import sys

input = sys.stdin.readline

N = int(input())
L = int(input())

graph = [[] for _ in range(N+1)]

visited = [False] * (N+1)

for _ in range(L):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = True
    for num in graph[v]:
        if not visited[num]:
            dfs(num)

dfs(1)
print(sum(visited) - 1)
