import sys

n= int(sys.stdin.readline())
arr1= set(map(int,sys.stdin.readline().split()))

m= int(sys.stdin.readline())
arr2=list(map(int,sys.stdin.readline().split()))

for num in arr2:
    if num in arr1:
        print(1)
    else: 
        print(0)