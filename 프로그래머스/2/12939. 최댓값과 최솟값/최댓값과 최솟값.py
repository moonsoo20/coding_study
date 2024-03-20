def solution(s):
    answer = ''
    s = s.split(' ')
    s = [int(num) for num in s]
    s.sort()

    answer = ' '.join(map(str, [s[0], s[-1]]))

    return answer


