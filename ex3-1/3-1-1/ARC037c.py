"""
############### TLE ###############
N, K = map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
from collections import deque
import bisect
d=deque()
for a in A:
	for b in B:
		d.append(a*b)
print(sorted(d)[K-1])
"""
############### 2分探索 ###############
import bisect
N, K=map(int,input().split())
A=list(map(int, input().split()))
B=sorted(list(map(int, input().split())))
M=max(A)*max(B)


def check(x):
	cnt=0
	for a in A:
		b=x//a
		cnt+=bisect.bisect_right(B, b) #b以下の数
	return cnt>=K


def binary_search():
	l, r = 0, 10**18

	while r-l>1:
		mid=(l+r)//2

		if check(mid):
			r=mid
		else:
			l=mid
	return r

print(binary_search())