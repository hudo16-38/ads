ludi, namornikov, dostojnikov = map(int,input().split())

namornici = []
dostojnici = []

for _ in range(ludi):
    hodnota, vie = map(int,input().split())
    if vie == 1:
        dostojnici.append(hodnota)
    else:
        namornici.append(hodnota)

vysl = 0
dostojnici.sort(reverse=True)

vysl += sum(dostojnici[:dostojnikov])

namornici.extend(dostojnici[dostojnikov:])
namornici.sort(reverse=True)

vysl += sum(namornici[:namornikov-dostojnikov])
    
print(vysl)

    
    
