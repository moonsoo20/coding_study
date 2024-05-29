def solution(arr):
    # 리스트가 비어있으면 [-1] 반환
    if not arr:
        return [-1]
    
    # 가장 작은 요소 찾기
    min_value = min(arr)
    
    # 가장 작은 요소 제거 (첫 번째 만나는 요소만 제거됨)
    arr.remove(min_value)
    
    # 리스트가 비어 있으면 [-1] 반환, 그렇지 않으면 리스트 반환
    return arr if arr else [-1]
