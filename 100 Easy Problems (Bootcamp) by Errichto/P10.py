n = int(input())
a = list(map(int, input().split()))[:n]
ans = 1
cur = 0
for i in range(0, n):
    if i == 0 or a[i] > a[i-1] * 2:
        cur = 1
    else:
        cur = cur + 1
    ans = max(ans, cur)
print(ans)
