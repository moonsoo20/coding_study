def solution(s):
    answer=0
    st=[]
    
    
    for i in range(len(s)):
        if len(st)==0:
            st.append(s[i])
        elif st[-1]==s[i]:
            st.pop()           
        else:
            st.append(s[i])
            
    if len(st)==0:
        return 1
    return answer
            
            
        

    return answer