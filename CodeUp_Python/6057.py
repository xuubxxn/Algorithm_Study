a, b = map(int, input().split())
print((bool(a) and bool(b)) or (bool(not a) and bool(not b)))