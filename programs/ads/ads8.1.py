def subset_sum(record, target):
    
    tab = [[False for _ in range(target+1)] for _ in range(len(record)+1)]

    for i in range(len(record)+1):
        tab[i][0] = True
    
    for i in range(1,len(record)+1): #rows
        for j in range(1,target+1): #columns
            
            if j < record[i-1]:
                tab[i][j] = tab[i-1][j]
            else:
                if tab[i-1][j]:
                    tab[i][j] = tab[i-1][j]
                else:
                    tab[i][j] = tab[i-1][j - record[i-1]]
    #print(*tab,sep="\n")

    if not tab[len(record)][target]:
        return "nemozne"
    else:
        output = []
        col_index = target
        row_index = len(record)

        while col_index > 0 or row_index > 0:
            if tab[row_index][col_index] == tab[row_index-1][col_index]:
                row_index-=1
            else:
                output.append(row_index-1)
                col_index -= record[row_index-1]
                row_index -=1

        return output

    
if __name__ == "__main__":
    input()
    record = tuple(map(int,input().split()))
    target = int(input())
    
    #result = subset_sum([5,2,1,3], 9)
    result = subset_sum(record, target)
    if isinstance(result, str):
        print(result)
    else:
        print(*result)
