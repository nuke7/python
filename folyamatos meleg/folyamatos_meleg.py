bemenet = input().split()
varosok_szama, napok_szama, homerseklet = int(
    bemenet[0]), int(bemenet[1]), int(bemenet[2])

lista = []

for _ in range(varosok_szama):
    bemenet = input().split()
    counter = 0
    maximum = 0
    for i in bemenet:
        if int(i) > homerseklet:
            counter += 1
        else:
            if counter > maximum:
                maximum = counter
            counter = 0
    if counter > maximum:
        maximum = counter
    lista.append(maximum)

max_value = max(lista)

if max_value:
    print(lista.index(max_value)+1)
else:
    print(-1)
