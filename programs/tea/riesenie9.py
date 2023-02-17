def check(C, p, s):
    points = 0
    hod = [p, 0]
    for x in C:
        if x >= p:
            points += 1
        else:
            if x < hod[0]:
                hod[0] -= x
                hod[1] += x
            else:
                points += 1
                hod[0], hod[1] = p - (x - hod[0]), x - hod[0]
    if points >= s:
        return True
    return False

def solve():
    t, s = map(int, input().split())
    C = list(map(int, input().split()))

    z, e = 0, 10**20
    while e - z > 1:
        mid = (z + e) // 2
        if check(C, mid, s):
            z = mid
        else:
            e = mid
    
    print(z)

q = int(input())
for _ in range(q):
    solve()
