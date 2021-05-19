N = int(input())
Sum = 0
i = 0

while Sum < N :
    i += 1
    Sum += i
    if Sum >= N:
        print(i)