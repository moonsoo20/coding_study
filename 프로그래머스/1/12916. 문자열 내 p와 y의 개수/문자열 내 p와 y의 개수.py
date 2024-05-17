def solution(s):
    p_num = 0
    y_num = 0
    
    for char in s:
        if char == 'p' or char == 'P':
            p_num += 1
        if char == 'y' or char == 'Y':
            y_num += 1
    
    return p_num == y_num
