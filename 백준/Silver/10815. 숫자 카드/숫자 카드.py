import sys
from bisect import bisect_right, bisect_left

def count_by_find(a, value):
    right_index = bisect_right(a, value)
    left_index = bisect_left(a, value)

    return 1 if right_index - left_index > 0 else 0

m = int(sys.stdin.readline())
arr = sorted(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

answer = [count_by_find(arr, value) for value in arr2]

print(" ".join(map(str, answer)))
