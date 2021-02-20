N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]

if 0 in S:
    exit(print(N))

r, ans, total = 0, 0, 1
for l in range(N):
    while r < N and total * S[r] <= K:
        total *= S[r]
        r += 1
    ans = max(ans, r - l)

    if l ==r:
        r += 1
    else:
        total //= S[l]
print(ans)
