import sys
from collections import deque

dq=deque()

N= int(sys.stdin.readline())

for _ in range(N):
    comment= list(sys.stdin.readline().split())
    if comment[0]=="push_front":
        dq.appendleft(comment[1])
    elif comment[0] == "push_back":
        dq.append(comment[1])
    elif comment[0] == "pop_front":
        if len(dq) >= 1:
            pop_num = dq.popleft()
            print(pop_num)
        else:
            print(-1)
    elif comment[0] == "pop_back":
        if len(dq) >= 1:
            pop_num = dq.pop()
            print(pop_num)
        else:
            print(-1)
    elif comment[0] == "size":
        print(len(dq))
    elif comment[0] == "empty":
        if len(dq)>=1:
            print(0)
        else:
            print(1)
    elif comment[0] == "front":
        if len(dq) >= 1:
            print(dq[0])
        else:
            print(-1)
    elif comment[0] == "back":
        if len(dq) >= 1:
            print(dq[-1])
        else:
            print(-1)