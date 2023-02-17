from queue import PriorityQueue

class Vertex:

    def __init__(self):

        self.rank = 0
        self.rep = self

class Country:

    def __init__(self, n):

        self.g = {i:dict() for i in range(-1,n)}

    def add_well(self, city, price):

        self.g[-1][city] = price
            
        #self.g[city][-1] = price

    def add_connection(self, city1, city2, price):

##        if city1 not in self.g:
##            self.g[city1] = dict()
##
##        if city2 not in self.g:
##            self.g[city2] = dict()

        self.g[city1][city2] = price

        #self.g[city2][city1] = price


    def build_pipes(self):

        #-------------------

        def find(v):

            v = D[v]

            while v != v.rep:
                v = v.rep
            return v

        #-------------------

        pq = PriorityQueue()

        D = {v:Vertex() for v in self.g}

        for v in self.g:
            for w in self.g[v]:
                price = self.g[v][w]

                pq.put((price, v, w))

        result = 0
        while not pq.empty():

            price, v, w = pq.get()

            id1, id2 = find(v), find(w)

            if id1 != id2:
                result += price

                if id1.rank < id2.rank:

                    id1.rep = id2

                elif id1.rank > id2.rank:
                    id2.rep = id1

                else:
                    id2.rep = id1
                    id1.rank += 1

        return result


if __name__ == "__main__":

    N = int(input())

    country = Country(N)

    for i in range(N):

        country.add_well(i, int(input()))

    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(i+1, N):

            country.add_connection(i, j, line[j])

    print(country.build_pipes())

            

                

                

                

        
        

            

            
                

    

            
                
                
