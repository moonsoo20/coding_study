
def solution(A ,B):
    answer = 0

    arr1 =sorted(B)
    arr2 =sorted(A,reverse=True)

    answer =0

    for i in range(len(arr1)):
        answer+=arr1[i] * arr2[i]

    print(answer)

    return answer


solution([1, 4, 2],[5, 4, 4])