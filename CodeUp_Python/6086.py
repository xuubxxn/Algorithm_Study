n = int(input())
Sum = 0
i = 0

while True:
    Sum += i
    i += 1
    if Sum >= n:
        break
print(Sum)
