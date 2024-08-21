
def solution(array, commands):
    answer = []

    for command in commands:
        a=command[0]
        b = command[1]
        c = command[2]
        temp = array[a-1:b]
        temp.sort()
        answer.append(temp[c - 1])


    return answer

solution([1, 5, 2, 6, 3, 7, 4],	[[2, 5, 3], [4, 4, 1], [1, 7, 3]])