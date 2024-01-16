from bisect import bisect_right, bisect_left
import sys

def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

arr.sort()
count = [0] * M  # M개의 수에 대한 개수를 담을 리스트 초기화

for i in range(M):
    count[i] = count_by_range(arr, arr2[i], arr2[i])

for num in count:
    print(num, end=" ")
