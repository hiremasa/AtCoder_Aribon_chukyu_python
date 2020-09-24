
N, K = map(int, input().split())
L=list(map(float, input().split()))
import math

def check(x):
	cnt=0
	for l in L:
		cnt+=l//x

	return cnt>=K

def binary_search():
	l, r = 0, 10**5

	for _ in range(100): #かいの存在範囲が十分狭くなるまで繰り返す
		mid=(l+r)/2
		if check(mid):
			l=mid
		else:
			r=mid

	return l
print(math.floor(binary_search()*100)/100)
