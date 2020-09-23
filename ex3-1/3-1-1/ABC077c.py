from bisect import bisect_left
import heapq
N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
C=list(map(int, input().split()))

heapq.heapify(A)
heapq.heapify(B)
heapq.heapify(C)

ans=0
for a in A:
	temp=1

	b_idx = bisect_left(B, a)
	if b_idx==len(B):
		continue
	temp*=b_idx
	b_temp = B[b_idx]

	c_idx = bisect_left(C, b_temp)
	temp*=c_idx

	ans+=temp
print(ans)



N = int(input())
A = np.array(input().split(), dtype=np.int32)
B = np.array(input().split(), dtype=np.int32)
C = - np.array(input().split(), dtype=np.int32)
 
A.sort()
B.sort()
C.sort()
 
cnt_A = np.searchsorted(A,B,side='left')
cnt_C = np.searchsorted(C,-B,side='left')
 
answer = (cnt_A * cnt_C).sum()
print(answer)