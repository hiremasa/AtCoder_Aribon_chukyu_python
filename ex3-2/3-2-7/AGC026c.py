"""
from collections import Counter
N = int(input())
S = input().rstrip()

left = [('', '')]
for s in S[:N]:
    left = [(x[0] + s, x[1]) for x in left] + [(x[0], x[1] + s) for x in left]
left = [x + ' ' + y for x, y in left]
counter_L = Counter(left)

right = [('', '')]

for s in S[N:][::-1]:
    right = [(x[0] + s, x[1]) for x in right] + [(x[0], x[1] + s) for x in right]
right = [x + ' ' + y for x, y in right]

answer = sum(counter_L[s] for s in right)
print(answer)
"""



from collections import defaultdict
N = int(input())
S = input()
SL = S[:N]
SR = S[N:][::-1]

ans = 0
memo = defaultdict(int)

for bit in range(1 << N):
    red = ""
    blue = ""
    for i in range(N):
        if bit & (1 << i):
            red += SL[i]
        else:
            blue += SL[i]
    memo[(red, blue)] += 1

for bit in range(1 << N):
    red = ""
    blue = ""
    for i in range(N):
        if bit & (1 << i):
            red += SR[i]
        else:
            blue += SR[i]
    ans += memo[(red, blue)]

print(ans)