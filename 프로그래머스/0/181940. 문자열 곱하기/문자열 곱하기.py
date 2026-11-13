def solution(my_string, k):
    if 1 <= len(my_string) <= 100 and 1 <= k <= 100:
        answer = ''
        answer = my_string * k
    return answer