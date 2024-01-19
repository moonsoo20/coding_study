import sys

n = int(sys.stdin.readline().strip())

stack = []

for _ in range(n):
    s = int(sys.stdin.readline().strip())

    if s != 0:
        stack.append(s)
    else:
        stack.pop()
sum=0

for i in range(len(stack)):
    sum+=stack[i]
print(sum)
