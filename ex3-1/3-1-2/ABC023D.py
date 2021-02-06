N = int(input())
H = []
S = []
for _ in range(N):
    h, s = map(int, input().split())
    H.append(h)
    S.append(s)

def is_ok(arg):
    timelst = []
    for i in range(N):
        t_i = (arg - H[i])/S[i]
        timelst.append(t_i)
    timelst.sort()

    for i in range(N):
        if timelst[i] < i:
            return False
    return True

def meguru_bisect(ng, ok):

    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(-1, max(H)*(max(S)*50)))