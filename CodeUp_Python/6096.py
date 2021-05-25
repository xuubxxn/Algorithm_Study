g = [list(map(int, input().split())) for i in range(19)]

n= int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        if g[j][y-1] == 0:
            g[j][y-1] = 1
        else :
            g[j][y-1] = 0

        if g[x-1][j] == 0 :
            g[x-1][j] = 1
        else :
            g[x-1][j] = 0

for i in g :
    for j in i:
        print(j, end=' ')
    print()