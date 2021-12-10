n = int(input())
arr = list(map(int, input().split()))[:n]
l, r = map(int, input().split())
sum = 0
for i in range(l, r+1):
    sum = sum + arr[i]
print(sum)
