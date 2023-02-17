n, m = map(int, input().split())
colors = list(map(int, input().split()))
values = list(map(int, input().split()))
c = int(input())


def compute(cols, vals, c):

    tab = [0]
    last = {}

    for i in range(n):
        koralka = cols[i]

        if koralka not in last:
            tab.append(tab[-1] + c)
        elif last[koralka] == i-1:
            tab.append(tab[-1] + vals[koralka-1])
        else:
            opt1 = vals[koralka-1] + tab[last[koralka]+1] 
            opt2 = tab[-1] + c
            
            tab.append(max(opt1, opt2))
        last[koralka] = i
        
    return tab[-1]
        
print(compute(colors, values, c))

        
    
