def pipes(record, target):

    queue = [[]]
    positions = [[]]

    for index, value in enumerate(record):
        print(*queue, sep = "\n")
        print("-"*10)
        next_Q = []
        next_pos = []

        while queue:

            seq = queue.pop()
            pos = positions.pop()
            
            
            if sum(seq) == target:
                print(*queue,sep ="\n")
                print("nasiel _____")
                return pos

            next_Q.append(seq.copy())
            next_pos.append(pos.copy())
            
            seq.append(value)
            pos.append(index)
            
            next_Q.append(seq.copy())
            next_pos.append(pos.copy())

        queue = next_Q
        positions = next_pos

    print(*queue,sep="\n")
    

    #n = len(queue)//2
    for i in range(len(queue)):
        if sum(queue[i]) == target:
            return positions[i]
        
    return "nemozne"
                

    

if __name__ == "__main__":
    input()
    record = tuple(map(int,input().split()))
    target = int(input())

    result = pipes(record, target)
    if isinstance(result, str):
        print(result)
    else:
        print(*result)
