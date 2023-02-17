class Point():
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return self.x*other.y - self.y*other.x
    def __init__(self,x,y):
        self.x, self.y = x,y
        
n = int(input())
A,B,C = [],[],[]
for i in range(n):
    x,y = [int(x) for x in input().split()]
    A.append(Point(x,y))
A.sort(key=lambda point: (point.x, point.y))

# horny konvexny obal
for a in A:
    while len(B) > 1 and (B[-1]-B[-2])*(a-B[-2]) >= 0:
        B.pop()
    B.append(a)

# dolny konvexny obal
for a in reversed(A):
    while len(C) > 1 and (C[-1]-C[-2])*(a-C[-2]) >= 0:
        C.pop()
    C.append(a)

# cely konvexny obal
A = B[:-1]+C[:-1]

# aby sme nemuseli modulovat
A.append(A[0])

# obsah
S = 0
for i in range(len(A)-1):
    S += A[i+1]*A[i]

print(str(S // 2)+".5" if S%2 else str(S//2))
