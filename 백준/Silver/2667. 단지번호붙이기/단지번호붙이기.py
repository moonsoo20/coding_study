import sys

def bfs(x,y):
    q=[]
    q.append((x,y))
    v[x][y]=1
    cnt=1
    while q:
        nx,ny=q.pop(0)
        for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
            cx,cy=nx+dx,ny+dy
            if 0<=cx<N and 0<=cy<N and v[cx][cy]==0 and arr[cx][cy]==1:
                q.append((cx,cy))
                v[cx][cy]=1
                cnt+=1
    return cnt



input=sys.stdin.readline

N=int(input())
arr=[list(map(int,input().strip())) for _ in range(N)]
v=[[0]*(N) for _ in range(N)]
ans=[]

for i in range(N):
    for j in range(N):
        if arr[i][j]==1 and v[i][j]==0:
            ans.append(bfs(i,j))

ans.sort()
print(len(ans), *ans,sep='\n')