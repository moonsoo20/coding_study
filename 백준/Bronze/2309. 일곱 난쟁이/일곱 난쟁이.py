

man=[int(input()) for _ in range(9)]
answer=[]

def bfs(start,depth):
    if depth==7:
        if sum(answer)==100:
            for j in sorted(answer):
                print(j)
            exit()
        else :
            return

    for i in range(start,len(man)):
        answer.append(man[i])
        bfs(i+1,depth+1)
        answer.pop()

bfs(0,0)

