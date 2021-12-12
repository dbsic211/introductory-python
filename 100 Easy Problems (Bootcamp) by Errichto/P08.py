n, L, c = map(int, input().split())
t = [0] * (n+1)
l = [0] * (n+1)
v = []
v.append((L, 0))
v.append((0, 0))
for i in range(1, n+1):
    t[i], l[i] = map(int, input().split())
    v.append((t[i], 1))
    v.append((t[i] + l[i], -1))
v.sort()
sum = 0
prev = 0
ans = 0
ok = 0
for a, b in v:
    sum = sum + b
    if ok == 1:
        ok = 0
        ans = ans + (a - prev) // c
    if sum == 0:
        ok = 1
    prev = a
print(ans)
