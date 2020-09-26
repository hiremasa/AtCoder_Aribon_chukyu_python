N=int(input())
M=int(input())
X=sorted(list(map(int,input().split())))

def is_ok(d):
	last=0
	for i in range(1,M):
		crt=last+1
		while crt<N and X[crt]-X[last]<d:
			crt+=1
		if crt==N:
			return False
		last=crt
	return True


def meguru_bisect(ng, ok):
	while abs(ng-ok)>1:
		mid=(ng+ok)//2
		if is_ok(mid):
			ok=mid
		else:
			ng=mid
	return ok

print(meguru_bisect(10**9+1,-1))