a, b = map(int, input().split())
print((bool(a)and bool(not b)) or (bool(b) and bool(not a)))