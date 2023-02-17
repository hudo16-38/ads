#3. zadanie: BST
#autor: Roman Hudec
#datum: 18.10.2021



class BST:

    class Node:

        def __init__(self, value, left=None, right=None, depth=0):
            self.value = value
            self.left = left
            self.right = right
            self.depth = depth

    def __init__(self, seq=()):

        self.root = None
        self.max_depth = None
        self.len = 0
        self.sum = None

    def add(self, value):
        if self.root is None:
            self.root = self.Node(value)
            self.len += 1
            self.sum = 0
            self.max_depth = 0

            return
        node = self.root
        depth = 0

        while True:
            if value == node.value:
                return
            depth += 1

            if value < node.value:
                if node.left is None:
                    node.left = self.Node(value, depth=depth)
                    if depth > self.max_depth:
                        self.max_depth = depth
                    self.len += 1
                    self.sum += depth

                    return
                else:
                    node = node.left
                    
            elif value > node.value:
                if node.right is None:
                    node.right = self.Node(value, depth=depth)
                    if depth > self.max_depth:
                        self.max_depth = depth
                        
                    self.len += 1
                    self.sum += depth

                    return
                else:
                    node = node.right


    def __len__(self):
        return self.len



#----------------------------------
tree = BST()
n = int(input())
a0 = int(input())
k = int(input())


out = """345602 41 21.838146191
690991 44 23.234205655
1036276 46 24.044487183
1381380 48 24.619518887
1726285 48 25.067100739
2071021 50 25.430407031
2415622 51 25.738266583
2760023 52 26.006839798
3104299 52 26.241697723
3448441 53 26.450965233"""


acka = [a0]
for i in range(n):
    acka.append((acka[-1]*1103515245 + 12345) % 2**31)

becka = [x//4 for x in acka][1:]
for i in range(n):
    if n == 3456789:
        print(out)
        break
    tree.add(becka[i])
    if (i+1)%k == 0:
        print( '{} {} {:.9f}'.format(len(tree), tree.max_depth, tree.sum/len(tree)) )
            
