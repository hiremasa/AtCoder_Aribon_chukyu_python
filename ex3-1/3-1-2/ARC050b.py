def check(K):
	cnt=(R-K)//(x-1) + (B-K)//(y-1)
	return cnt>=K and R >= K and B >= K

def binary_search():
	l, r = 0, R+B

	while r-l>1:
		mid=(l+r)//2
		if check(mid):
			l=mid
		else:
			r=mid
	return l

if __name__=="__main__":
	R, B = map(int, input().split())
	x, y = map(int, input().split())
	print(int(binary_search()))

############### meguru bisect ###############
R, B = map(int,input().split())
x, y = map(int,input().split())
def is_ok(K):
	if K>R or K>B:
		return False
	if (R-K)//(x-1) + (B-K)//(y-1) >= K:
		return True
	return False

def meguru_bisect(ng, ok):
	while (abs(ok - ng) > 1):
		mid = (ok + ng) // 2
		if is_ok(mid):
			ok = mid
		else:
			ng = mid
	return ok
print(meguru_bisect(10**19,0))