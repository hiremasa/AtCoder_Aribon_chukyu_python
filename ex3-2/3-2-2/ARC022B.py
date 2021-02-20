N = int(input())
A = list(map(int, input().split()))

All = set(A)
kind = len(All)

l, r, num = 0, 0, 0
dd = dict()
res = 0

#しゃくとり法
for l in range(N):
    while r < N and num < kind:
        if not A[r] in dd:# 新しい事象が出現
            dd[A[r]] = 1
            num += 1

            res = max(res, r - l)


        dd[A[l]] -= 1
        if dd[A[l]] == 0:
            num -= 1

print(res)



N = int(input())
A = list(map(int, input().split()))
s = set()
l = 0
ans = 0
for r, a in enumerate(A):
    while a in s:
        s.remove(A[l])
        l += 1
    s.add(a)
    ans = max(ans, r-l)
print(ans+1)