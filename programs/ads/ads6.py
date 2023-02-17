from itertools import combinations
from queue import PriorityQueue

a, b = int(input()), int(input())
tab = [list(map(int, input().split())) for _ in range(a)]
transpose = list(map(list, zip(*tab)))

teamA = range(a)
teamB = range(b)

combA = [list(c) for c in combinations(teamA, 5)]

optimal = None

for comb in combA:
    for capt in comb:
        
        team_A = comb + [capt]
        queue = PriorityQueue()
        
        for num, playerB in enumerate(transpose):
            overall = 0
            
            for rival in team_A:
                overall += playerB[rival]
            queue.put((overall, num))
            
        team_B = []
        
        for _ in range(5):
            ov, pl = queue.get()
            
            team_B.append(pl)
            if _ == 0:
                team_B.append(pl)
        
        output = 0
        
        for playerA in team_A:
            for playerB in team_B:
                
                output += tab[playerA][playerB]
                
        if optimal is None or output > optimal:
            optimal = output
        
print(optimal)
            
            
                
                
    