s = list(input())
for i in range(0, len(s)):
    if s[i] >= 'A' and s[i] <= 'Z':
        s[i] = chr(ord(s[i]) ^ 32)
    if s[i] != 'a' and s[i] != 'o' and s[i] != 'y' and s[i] != 'e' and s[i] != 'u' and s[i] != 'i':
        print('.', end = '')
        print(s[i], end = '')
