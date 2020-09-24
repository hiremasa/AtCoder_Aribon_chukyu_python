R, B = map(int, input().split())
x, y = map(int, input().split())

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
	print(int(binary_search()))

