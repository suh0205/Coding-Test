def solution(arr):
    if 1 <= len(arr) and len(arr) <=200:
        answer = ''
        for i in range(len(arr)):
            answer += arr[i]
        return answer