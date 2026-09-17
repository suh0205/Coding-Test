
while True:
    str, n = input().strip().split(' ')
    n = int(n)
    if str != " " and 1 <= len(str) <= 10 and 1 <= n <= 5:
        for i in range (0, n):
                 print(str, end = "")
        break
    else:
        continue