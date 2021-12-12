n = int(input())
s = list(input())
a = []
cnt = 0
for i in range(0, n):
    if s[i] == '8':
        cnt = cnt + 1
    else:
        a.append(ord(s[i]) - 48)
ptr = 0
opp = n - cnt
ans = 0
while True:
    if cnt > 0 and ptr + 9 < opp:
        ans = ans + 1
        cnt = cnt - 1
        ptr = ptr + 10
    elif opp - ptr + cnt >= 11 and cnt > 0:
        ans = ans + 1
        cnt = cnt - (11 - (opp - ptr))
        ptr = opp
    else:
        print(ans)
        exit(0)
