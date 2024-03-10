import sys

input = sys.stdin.readline

N = int(input())

# A와 B 리스트를 각각 숫자의 리스트로 저장하기 위해 map 함수를 사용하여 변환합니다.
A = list(map(int, input().split()))
B = list(map(int, input().split()))


sorted_a = sorted(A, reverse=True)
sorted_b = sorted(B)

s = 0
for i in range(N):
    s += sorted_a[i] * sorted_b[i]

print(s)


