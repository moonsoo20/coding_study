
N=int(input())
M=int(input())

graph=[[] for _ in range(N+1)]
visited=[False]*(N+1)


for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v]=True
    count=1
    for neighbor in graph[v]:
        if not visited[neighbor]:
            count+=dfs(neighbor)
    return count

result = dfs(1) - 1
print(result)
