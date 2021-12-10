s = input()
done = 0
cnt = [0] * 3
for i in range(0, len(s)):
    if s[i] == '1':
        cnt[0] = cnt[0] + 1
    elif s[i] == '2':
        cnt[1] = cnt[1] + 1
    elif s[i] == '3':
        cnt[2] = cnt[2] + 1
for i in range(0, 3):
    for j in range(0, cnt[i]):
        if done == 1:
            print('+', end = '')
        print(i+1, end = '')
        done = 1
