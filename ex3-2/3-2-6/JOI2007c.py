from bisect import bisect_left, bisect_right
N, M = map(int,input().split())
P = [] #+ list(map(int, input().split()))
for _ in range(N):
    P.append(int(input()))


Q = set(P)
Q.add(0)
for i in range(N):
    for j in range(i, N):
        Q.add(P[i] + P[j])
Q = sorted(list(Q))


ans = 0
for q in Q:
    if q > M:
        tmp = 0
    else:
        tmp = q + Q[bisect_right(Q, M - q) - 1]

    ans = max(ans, tmp)
print(ans)