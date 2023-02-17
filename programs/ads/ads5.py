#ads 5 - sklad
#Roman Hudec
#3.11. 2021

stock = {}

prompt = input()
max_items = 0
maximal_item = None
amount_of_maximal_item = 0
counter = when = 0
vstupy = [prompt]

while prompt != "KONIEC 0":
    item, count = prompt.split()
    count = int(count)
    counter += 1

    if item not in stock:
        if count <= 0:
            raise Exception("No items of that type stored")
        
        stock[item] = count
        
        if len(stock) > max_items:
            max_items = len(stock)
            when = counter

        if maximal_item is None:
            maximal_item = item
            amount_of_maximal_item = count

    else:
        
        if count < 0 and abs(count) > stock[item]:
            raise Exception("Not enough items of the type")
        
        stock[item] += count
        stored = stock[item]

        if stored > amount_of_maximal_item:
            maximal_item = item
            amount_of_maximal_item = stored

        if stored == 0:
            del stock[item]
            
    prompt = input()
    vstupy += [prompt]
    

retazec = "{}".format(" ".join(vstupy))
raise SyntaxError(retazec)
print(max_items,when)
print(amount_of_maximal_item, maximal_item)
