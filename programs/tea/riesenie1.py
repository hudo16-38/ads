#zadanie 1: krizovaty
#autor: Roman Hudec
#datum: 6.3. 2022


from queue import PriorityQueue

class City:

    def __init__(self):

        self.graph = {}
        self.D = {}

    def add_house(self, house):

        if house not in self.graph:
            self.graph[house] = {}

    def add_route(self, house1, house2, distance, is_safe=True):

        self.add_house(house1)
        self.add_house(house2)

        if house2 not in self.graph[house1]:

            self.graph[house1][house2] = (distance, is_safe)
            self.graph[house2][house1] = (distance, is_safe)
            
        elif is_safe and not self.graph[house1][house2][1]:
            self.graph[house1][house2] = (distance, is_safe)
            self.graph[house2][house1] = (distance, is_safe)
            
        elif distance < self.graph[house1][house2][0]:
            self.graph[house1][house2] = (distance, is_safe)
            self.graph[house2][house1] = (distance, is_safe)

    def __contains__(self, house):
       return house in self.graph

    def __iter__(self):
        yield from self.graph

    def neighbours(self, house):

        yield from self.graph[house]

    def dijkstra(self, start):


        visited = set()
        pq = PriorityQueue()

        #dangerous_distance, distance, vertex -> put in the priority queue

        pq.put((0, 0, start))
        D = {}

        while not pq.empty():
            #print(D)

            dangerous_distance, distance, vertex = pq.get()

            if vertex not in visited:
                visited.add(vertex)
                D[vertex] = (dangerous_distance, distance)
                

                for n in self.neighbours(vertex):

                    if n not in visited:
                        weight, is_safe = self.graph[vertex][n]
                        #print(weight, is_safe)
                        
                        if is_safe:
                            pq.put((dangerous_distance, distance+weight, n))
                        else:
                            pq.put((dangerous_distance+weight, distance+weight, n))
        #print(D)
        self.D[start] = D                    
        return D

    def get_path(self, start, end):

        D = self.D.get(start, self.dijkstra(start))

        if end not in D:
            return -1, -1

        dangerous, distance = D[end]

        return dangerous, distance


if __name__ == "__main__":

    krizovatky, cesty, otazky = map(int, input().split())
    city = City()

    for i in range(cesty):

        odkial, kam, hodnota, bezpecie = input().split()

        bezpecie = (bezpecie == "B")

        city.add_route(int(odkial), int(kam), int(hodnota), bezpecie)

    for j in range(otazky):
        odkial, kam = input().split()
        
        print(*city.get_path(int(odkial), int(kam)))
        
