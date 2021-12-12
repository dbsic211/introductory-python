N, Q = map(int,input().split())
row = {}
column = {}
dia45 = {}
dia225 = {}
for i in range(-2*N, 2*N+1):
    row[i] = 0
    column[i] = 0
    dia45[i] = 0
    dia225[i] = 0
for i in range(0, Q):
    X, Y = map(int,input().split())
    if row[X] == 1 or column[Y] == 1 or dia45[X - Y] == 1 or dia225[X + Y] == 1:
        print("NO")
    else:
        print("YES")
        row[X] = 1
        column[Y] = 1
        dia45[X - Y] = 1
        dia225[X + Y] = 1
