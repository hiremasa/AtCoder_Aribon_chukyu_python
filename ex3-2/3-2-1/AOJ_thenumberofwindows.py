N, Q = map(int, input().split())
A=list(map(int, input().split()))
X=list(map(int, input().split()))

def count_two_idx(A,q):
    ans ,left, csum = 0, 0, 0
    for right in range(N):
        csum += A[right]
        while csum > q:
            csum -= A[left]
            left += 1
        ans += right - left + 1
    return ans

for q in X:
    print(count_two_idx(A,q))