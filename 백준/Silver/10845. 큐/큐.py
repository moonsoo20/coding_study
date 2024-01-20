from collections import deque
import sys

N= int(sys.stdin.readline().strip())
dq = deque()

for _ in range(N):
    M=list(sys.stdin.readline().split())

    if M[0] == 'push':
        dq.append(M[1])
    elif M[0]== 'pop':
        if len(dq)< 1:
            print(-1)
        else:
            pop_number=dq.popleft()
            print(pop_number)
    elif M[0]=='size':
        print(len(dq))
    elif M[0]=='empty':
        if len(dq) < 1:
            print(1)
        else:
            print(0)
    elif M[0]=='front':
        if len(dq) < 1:
            print(-1)
        else:
            print(dq[0])

    elif M[0]=='back':
        if len(dq) < 1:
            print(-1)
        else:
            print(dq[-1])


