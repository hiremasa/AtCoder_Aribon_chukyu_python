N, K = map(int, input().split())
W=[]
P=[]
for _ in range(N):
	w, p = map(int, input().split())
	W.append(w)
	P.append(p)

def is_ok(x):
	Y=[P[i]*W[i]-x*W[i] for i in range(N)]
	Y.sort(reverse=True)

	sum=0
	for i in range(K):
		sum+=Y[i]
	return sum>=0

def meguru_bisect(ng, ok):
	for _ in range(1000):
		mid=(ok+ng)/2
		if is_ok(mid):
			ok=mid
		else:
			ng=mid
	return ok
print(meguru_bisect(101, -1))