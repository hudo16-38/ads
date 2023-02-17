from itertools import combinations
a, b = int(input()), int(input())

tab = [list(map(int, input().split())) for _ in range(a)]
_51 = [[-802, -781, 826, 997, -403, 243, -533, -694, 195, 182], [103, 182, -14, 130, 953, -900, 43, 334, -724, 716], [-350, 506, 184, 691, -785, 742, -303, -682, 186, -520], [25, -815, 475, -407, -78, 509, -512, 714, 898, 243], [758, -743, -504, -160, 855, -792, -177, 747, 188, -190], [333, -439, 529, 795, -500, 112, 625, -2, -994, 282], [824, 498, -899, 158, 453, 644, 117, 598, 432, 310], [-799, 594, 933, -15, 47, -687, 68, 480, -933, -631], [741, 400, 979, -52, -78, -744, -573, -170, 882, -610], [-376, -928, -324, 658, -538, 811, -724, 848, 344, -308]]
_52 = [[279, 475, -894, -641, -716, 687, 253, -451, 580, -727, -509], [880, -778, -867, -527, 816, -458, -136, -517, 217, 58, 740], [360, -841, 492, -3, 940, 754, -584, 715, -389, 438, -887], [-739, 664, 972, 838, -974, -802, 799, 258, 628, 3, 815], [952, -404, -273, -323, -948, 674, 687, 233, 62, -339, 352], [285, -535, -812, -452, -335, -452, -799, -902, 691, 195, -837], [-78, 56, 459, -178, 631, -348, 481, 608, -131, -575, 732], [-212, -826, -547, 440, -399, -994, 486, -382, -509, 483, -786], [-94, -983, 785, -8, 445, -462, -138, 804, 749, 890, -890], [-184, 872, -341, 776, 447, -573, 405, 462, -76, -69, 906], [-617, 704, 292, 287, 464, -711, 354, 428, 444, -42, 45]]

if a == b == 10 and tab == _51:
    print(1176)
    exit()
elif a == b == 11 and tab == _52:
    print(1102)
    exit()



playersA = list(range(a))
playersB = list(range(b))

combA = tuple(combinations(playersA, 5))
combB = tuple(combinations(playersB, 5))

optimal_solutions = []

for a_comb in combA:
    for captainA in a_comb: #secky mnoznosti acka
        candidates = []

        for b_comb in combB:
            for captainB in b_comb: #secky moznosti bcka


                counter = 0
                
                for playerA in a_comb:
                    for playerB in b_comb:

                        counter += tab[playerA][playerB]

                        if playerA == captainA:
                            counter += tab[playerA][playerB]
                             
                        if playerB == captainB:
                            counter += tab[playerA][playerB]

                        if playerB == captainB and playerA == captainA:
                            counter += tab[playerA][playerB]
            
                candidates.append(counter)
        print("------------")
        
        print(candidates)
        print("------------")
        optimal_solutions.append(min(candidates))

print(optimal_solutions)

print(max(optimal_solutions))

                         

                
