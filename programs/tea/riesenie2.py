#zadanie 2: cesty
#autor: Roman Hudec
#datum: 14.3. 2022


class CityUnion:

    #--------vnorena trieda -------

    class City:

        def __init__(self):

            self.rank = 0 
            self.cities = 1 #pocet miest v komponente
            self.rep = self #reprezentant

    def __init__(self):

        self.D = {} 

    def __contains__(self, name):
        return name in self.D


    def find(self, name):

        if name not in self:
            self.D[name] = self.City()
            return self.D[name]

        city = self.D[name]

        while city.rep != city:
            city = city.rep

        self.D[name].rep = city

        return city

    def union(self, name1, name2):

        id1, id2 = self.find(name1), self.find(name2)

        if id1 == id2: #su v spolocnom komponente
            return 0

        if id1.rank == id2.rank: #rovnaky rank, pri spajani vraciame sucin
                                # poctu vrcholov v komponentoch
            id1.rank+=1

            result = id1.cities * id2.cities

            id1.cities += id2.cities
            id2.rep = id1

            return result
        if id1.rank < id2.rank:

            result = id1.cities * id2.cities

            id2.cities += id1.cities
            id1.rep = id2

            return result

        if id1.rank > id2.rank:
            result = id1.cities * id2.cities

            id1.cities += id2.cities
            id2.rep = id1

            return result


if __name__ == "__main__":

    city = CityUnion()

    N = int(input())

    for _ in range(N):

        name1, name2 = input().split()

        print(city.union(name1, name2))


            
        
