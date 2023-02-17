from math import ceil, log

class Node:

    def __init__(self):
        self.value = 0
        self.lazy = 0

class SegmentTree:

    def __init__(self, capacity):
        

        self.n = int(pow(2, ceil(log(capacity)/log(2))))

        self.tree = [Node()]*(2*self.n - 1)

        for i in range(self.n - 1, self.n - capacity, - 1):
            self.tree[i].beg = i
            self.tree[i].end = i+1
        for _ in range(len(data), self.n):

            self.data.append(0)


        for j in range(self.n - 2, -1, -1):

            left_son = 2*j + 1
            right_son = 2*j + 2

            self.tree[j].end = self.tree[right_son].end
            self.tree[j].beg = self.tree[left_son].beg

    def __repr__(self):
        return f"SegmentTree{tuple(self.tree)}"
    __str__ = __repr__

    def update(self, index):

        index += self.n - 1
        self.tree[index] += 1

        while index > 0:
            index = (index-1)//2
            self.tree[index] += 1

    def __getitem__(self, index):

        return self.tree[index + self.n -1]

    def update_interval(self, a, b):
        for i in range(a-1, b):
            self.update(i) 
    


if __name__ == "__main__":

    t = SegmentTree([4, 3, 1, 4])
    print(t)
    t.update(0)
    print(t[0])
    print(t)

##    n, q = map(int, input().split())
##
##    t = SegmentTree([0]*n)
##
##    for _ in range(q):
##
##        task = input().split()
##        if  len(task) == 2:
##            j, i = task
##
##            print(t.get(int(i)-1))
##
##        else:
##            j, a, b = task
##            t.update_interval(int(a),int(b))
##            
    
    
