while True:
    a, b = map(int, input().strip().split(' '))
    if (-100000 <= a <= 100000) and (-100000 <= b <= 100000):
        print("a = %d"% a)
        print("b = %d"% b)
        break
    else:
        continue
    