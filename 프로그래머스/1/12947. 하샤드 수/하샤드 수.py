def solution(x):
    answer = True
    
    arr = [int(digit) for digit in str(x)]
    
    if x % sum(arr) == 0:
        return True
    else: 
        return False
