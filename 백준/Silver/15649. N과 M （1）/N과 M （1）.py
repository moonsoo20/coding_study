

N,M=map(int,input().split())
visited=[False]*(N+1)
arr=[]

def btk(depth):
    if depth==M:
        print(' '.join(map(str,arr)))
        return

    for i in range(1,N+1):
        if not visited[i]:
            arr.append(i)
            visited[i]=True
            btk(depth+1)
            arr.pop()
            visited[i] = False

btk(0)