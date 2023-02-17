#2. zadanie: halda stupna 4
#autor: Roman Hudec
#18.10. 2021


class Heap:

    def __init__(self):
        self.__data = []
        self.__insert = 0
        self.__pop = 0

    def pop(self):

        if self.is_empty():
            raise Exception("empty heap")
            

        self.__data[0], self.__data[-1] = self.__data[-1], self.__data[0]

        out = self.__data.pop()

        node = 0

        while True:
            syn1 = node*4 + 1
            vacsi = node

            if syn1 < len(self):
                self.__pop += 1
                if self.__data[syn1] > self.__data[vacsi]:
                     vacsi = syn1

            syn2 = node*4 + 2
   
            if syn2 < len(self):
                
                self.__pop += 1
                
                if self.__data[syn2] > self.__data[vacsi]:
                    vacsi = syn2

            syn3 = node*4 + 3
   
            if syn3 < len(self):
                
                self.__pop += 1
                
                if self.__data[syn3] > self.__data[vacsi]:
                    vacsi = syn3

            syn4 = node*4 + 4
   
            if syn4 < len(self):
                
                self.__pop += 1
                
                if self.__data[syn4] > self.__data[vacsi]:
                    vacsi = syn4
            
            if vacsi != node:
                self.__data[node], self.__data[vacsi] = self.__data[vacsi], self.__data[node]
                node = vacsi
            else:
                break
            
        return out
    def push(self,value):
        self.__data.append(value)

        node = len(self) - 1

        while node > 0:

            daddy = (node - 1)//4
            
            self.__insert += 1
            if self.__data[node] > self.__data[daddy]:
                
                self.__data[node], self.__data[daddy] = self.__data[daddy], self.__data[node]
                
                node = daddy
            
            else:
                break
            
            

                
    def __len__(self):
        return len(self.__data)
    
    def __repr__(self):
        return str(self.__data)
      


    def is_empty(self):
        return self.__data == []

    def __getitem__(self,atribute):
        if atribute not in {"pop", "insert"}:
            raise Exception("Atribute doesn't exist")
        
        if atribute == "pop":
            return self.__pop
        
        return self.__insert
    def vynuluj(self):
        self.__data.clear()
        self.__pop = self.__insert = 0

class BinaryHeap:

    def __init__(self):
        self.__data = []
        self.__insert = 0
        self.__pop = 0

    def pop(self):

        if self.is_empty():
            raise Exception("empty heap")
            

        self.__data[0], self.__data[-1] = self.__data[-1], self.__data[0]

        out = self.__data.pop()

        node = 0

        while True:
            syn1 = node*2 + 1
            vacsi = node

            if syn1 < len(self):
                self.__pop += 1
                if self.__data[syn1] > self.__data[vacsi]:
                     vacsi = syn1

            syn2 = node*2 + 2
   
            if syn2 < len(self):
                
                self.__pop += 1
                
                if self.__data[syn2] > self.__data[vacsi]:
                    vacsi = syn2
            
            if vacsi != node:
                self.__data[node], self.__data[vacsi] = self.__data[vacsi], self.__data[node]
                node = vacsi
            else:
                break
            
        return out
    def push(self,value):
        self.__data.append(value)

        node = len(self) - 1

        while node > 0:

            daddy = (node - 1)//2
            
            self.__insert += 1
            if self.__data[node] > self.__data[daddy]:
                
                self.__data[node], self.__data[daddy] = self.__data[daddy], self.__data[node]
                
                node = daddy
            
            else:
                break
            
            

                
    def __len__(self):
        return len(self.__data)
    
    def __repr__(self):
        return str(self.__data)

    def is_empty(self):
        return self.__data == []

    
    def __getitem__(self,atribute):
        if atribute not in {"pop", "insert"}:
            raise Exception("Atribute doesn't exist")
        
        if atribute == "pop":
            return self.__pop
        
        return self.__insert
    
    def vynuluj(self):
        self.__data.clear()
        self.__pop = self.__insert = 0





halda = Heap()
halda2 = BinaryHeap()
pocet = int(input())
a0 = int(input())

pole = [a0]
for i in range(pocet):
    pole.append((pole[-1]*1103515245 + 12345) % 2**31)
    
becka = [x//4 for x in pole][1:]

testy = [[0]*pocet, list(range(1,pocet+1)), range(pocet,0,-1), becka]

for test in testy:

    for i in range(pocet):
        halda.push(test[i])
        halda2.push(test[i])

    while not halda.is_empty():
        halda.pop()
        halda2.pop()

    print(halda2["insert"],halda2["pop"], halda["insert"],halda["pop"])

    halda2.vynuluj()
    halda.vynuluj()



