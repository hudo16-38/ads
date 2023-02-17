class MaxHeap:
    
    class Item:
        
        def __init__(self, key, value):
            self.key = key
            self.value = value     
        def __eq__(self, other):
            return self.key == other.key
        
        def __lt__(self, other):
            return self.key < other.key
        def __gt__(self, other):
            return self.key > other.key
        def __repr__(self):
            return "<{}, {}>".format(self.key, self.value)
        
    def __init__(self, seq=[]):
        
        self.heapify(seq)
        self.data = seq

    def __len__(self):
        return len(self.data)
    
    @staticmethod
    def heapify(lst):

        n = len(lst)

        for i in range(n):
            lst[i] = MaxHeap.Item(*lst[i])

        
        for i in reversed(range(n//2)):

            node = i

            while node < n:
                son1 = 2*node + 1
                    
                if son1 >= n:
                    break
                    
                bigger = son1
                    
                son2 = 2*node + 2
                    
                if son2 < n and lst[son2] > lst[bigger]:
                    bigger = son2
                        
                if lst[bigger] > lst[node]:
                    lst[bigger], lst[node] = lst[node], lst[bigger]
                    node = bigger
                else:
                    break

                

                
                
            
    def heappush(self, key, value):
        self.data.append(self.Item(key, value))
        
        node = len(self) - 1
        
        while node > 0:
            
            daddy = (node-1)//2
            
            if self.data[daddy] < self.data[node]:
                self.data[daddy], self.data[node] = self.data[node], self.data[daddy]
                node = daddy
            else:
                break

            
    def remove_max(self):
        if len(self) == 0:
            raise ValueError("Empty")
        
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        output = self.data.pop()

        node = 0

        while node < len(self):
            son1 = 2*node + 1
                
            if son1 >= len(self):
                break
                
            bigger = son1
                
            son2 = 2*node + 2
                
            if son2 < len(self) and self.data[son2] > self.data[bigger]:
                bigger = son2
                    
            if self.data[bigger] > self.data[node]:
                self.data[bigger], self.data[node] = self.data[node], self.data[bigger]
                node = bigger
            else:
                break
                
        return output.key, output.value
    
    def __iter__(self):
        for it in self.data:
            yield it.key, it.value
            
    
n, p, d = map(int, input().split())

dost = []
nam = []

#dost_heap = MaxHeap()
#nam_heap = MaxHeap()

for _ in range(n):
    hodnota, vie = map(int, input().split())
    
    if vie == 1:
        dost.append((hodnota, vie))
    else:
        nam.append((hodnota, vie))
        
dost_heap = MaxHeap(dost)

final = 0
for _ in range(d):

    k, v = dost_heap.remove_max()
    final += k

  
for k, v in dost_heap:
    nam.append((k,v))

nam_heap = MaxHeap(nam)
    
for _ in range(p-d):
    k, v = nam_heap.remove_max()
    final += k

print(final)
