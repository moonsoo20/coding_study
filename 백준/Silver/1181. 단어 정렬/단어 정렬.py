import sys

N= int(sys.stdin.readline())

arr=[]

for i in range(N):
    arr.append(sys.stdin.readline().strip())
    
set_list=list(set(arr))

set_list.sort()
set_list.sort(key=len)

for i in set_list:
    print(i)