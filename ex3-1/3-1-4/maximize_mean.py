N, K = map(int, input().split())
W=[]
V=[]
for _ in range(N):
	w, v = map(int, input().split())
	W.append(w)
	V.append(v)
Y=[0]*N
def is_ok(x):
	Y=[V[i] - x * W[i] for i in range(N)]
	Y.sort(reverse = True)

	#Yの大きい方からk個の和を計算
	sum=0
	for i in range(K):
		sum+=Y[i]

	return sum>=0

def meguru_bisect(ng, ok):
	for _ in range(10**2):
		mid=(ok+ng)/2
		if is_ok(mid):
			ok=mid
		else:
			ng=mid
	return ok

print('{:2f}'.format(meguru_bisect(10**6+1, 0)))
