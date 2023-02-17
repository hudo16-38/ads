def meetings(n):
    if n == 0: return 0
    names, visited = [input()], set()

    for _ in range(n-1):
        name = input()
        if names[-1] != name:
            names.append(name)
    n = len(names)

    for start in range(n):
        set1 = set()
        for end in range(start, n):
            set1.add(names[end])
            if "Baska" in set1:
                visited.add(frozenset(set1))

    return len(visited)

print(meetings(int(input())))




        
