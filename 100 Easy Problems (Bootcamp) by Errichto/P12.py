n = int(input())
a = list(map(int, input().split()))[:n]
l = 1e9
r = 0
for i in range(0, n-1):
    if a[i] > a[i+1]:
        l = min(l, i)
        r = max(r, i+1)
if r > 0:
    for i in range(l, r):
        d = i-l
        d2 = r-d
        if(i < d2):
            a[i], a[d2] = a[d2], a[i]
for i in range(0, n-1):
    if a[i] > a[i+1]:
        print("no")
        exit(0)
print("yes")
if r == 0:
    print("1 1")
else:
    print(l+1, end = ' ')
    print(r+1)
