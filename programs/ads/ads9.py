def skiing(n, z):

    tab = [[set() for _ in range(n)] for _ in range(n-1)]

    for i in range(z):
        from_where, where, colour = input().split()
        from_where = int(from_where) - 1
        where = int(where) - 1

        tab[from_where][where].add(colour)
        

    print(*tab,sep="\n")


if __name__ == "__main__":
    skiing(2, 2)
    print("-"*12)
    skiing(3,4)
        
