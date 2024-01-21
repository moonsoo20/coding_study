import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

start = 1
end = max(arr)  # 초기 end 값을 배열의 최댓값으로 설정

while start <= end:
    mid = (start + end) // 2
    result = 0

    for num in arr:
        if num > mid:
            result += mid
        else:
            result += num

    if result > M:
        end = mid - 1
    else:
        start = mid + 1

# 최댓값 출력
print(end)
