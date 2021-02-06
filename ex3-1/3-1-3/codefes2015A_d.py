N, M = map(int, input().split())
X = [int(input())-1 for _ in range(M)]

def is_ok(t):

    last = 0
    for x in X:
        if x <= last:
            last = max(x + t + 1, last)
        else:
            if x - t > last:
                return False
            else:
                move = x - last
                right_path = x + max(t - move * 2, 0) + 1
                left_path = x + max((t- move)//2, 0) + 1

                last = max(right_path, left_path)
                #last = max(last, last + t - 2 * (x - last), last + (t - x + last)//2, x)
    if last<N:
        return False
    return True



def meguru_bisect(ng, ok):
    while abs(ng-ok)>1:
        mid=(ng+ok)//2
        if is_ok(mid):
            ok=mid
        else:
            ng=mid
    return ok

print(meguru_bisect(-1, 2*10**9+1))