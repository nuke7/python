bemenet = input().split()
fenyofa_db, hatar_ar = int(bemenet[0]), int(bemenet[1])

draga_fenyofa_arak = []
index = []


for i in range(fenyofa_db):
    arak = int(input())
    # print(arak)

    if arak > hatar_ar:
        draga_fenyofa_arak.append(arak)
        index.append(i)

# print(draga_fenyofa_arak)

if draga_fenyofa_arak:
    min_ar = min(draga_fenyofa_arak)
    hanyadik = draga_fenyofa_arak.index(min_ar)
    # print(hanyadik)
    index_i = index[hanyadik]
    print(index_i+1, min_ar)
else:
    print(-1)
