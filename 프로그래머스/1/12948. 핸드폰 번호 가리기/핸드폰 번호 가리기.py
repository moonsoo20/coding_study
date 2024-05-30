def solution(phone_number):
    answer = ''
    answer1 = phone_number[-4:]
    
    for _ in range(len(phone_number)-4):
        answer+="*"
        
    answer+=answer1
    
    return answer