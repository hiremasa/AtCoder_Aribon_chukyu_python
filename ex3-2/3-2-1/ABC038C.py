N = int(input())
S = list(map(int, input().split()))

#====================TLE===============================
cnt = 0
for l in range(N):
    r = l + 1
    temp = S[l]
    while r < N and temp < S[r]:
        temp = S[r]
        cnt += 1
        r += 1

    if l==r:
        r += 1

print(cnt + N)

#====================AC===============================
N = int(input())
S = list(map(int, input().split()))

x = 0
ans = 0
temp = 0

for s in S:
    if s > temp:
        x += 1
    else:
        x = 1
    ans += x
    temp = s
print(ans)
