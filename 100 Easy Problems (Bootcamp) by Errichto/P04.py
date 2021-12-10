s = list(input())
t = list(input())
for i in range(0, len(s)):
    if s[i] >= 'a':
        s[i] = chr(ord(s[i]) ^ 32)
for i in range(0, len(t)):
    if t[i] >= 'a':
        t[i] = chr(ord(t[i]) ^ 32)
if s < t:
    print(-1)
elif s == t:
    print(0)
else:
    print(1)
#char to ascii: ord
#ascii to char: chr
#convert strings to lists
