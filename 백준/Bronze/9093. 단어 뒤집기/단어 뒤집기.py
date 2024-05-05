
T=int(input())

for i in range(T):
    arr=input().split()
    for j in arr:
        print(j[::-1],end=' ')