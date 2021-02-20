from collections import defaultdict
P = int(input())
A = map(int, input().split())

All = set(A)
N = len(A)

#しゃくとり法
r, l, num = 0, 0, 0
cnt = dict()
res = P

while True:
    while t < P and num < n:
        if not a[t] in cnt: # 新しい事象が出現
            cnt[a[t]] = 0
            num += 1
        cnt[a[t]] += 1
        t += 1

    if num < N:
        break
    res = min(res, t - s)
    cnt[a[s]] -= 1

    if cnt[a[s]] ==0: # ある事柄の出現数が0になった
        num -= 1
    s += 1

print(res)
