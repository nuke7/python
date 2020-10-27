bemenet = input().split()
fenyofa_db, hatar_ar = int(bemenet[0]), int(bemenet[1])

draga_fenyofa_arak = {"ar": [], "index": []}


for i in range(fenyofa_db):
    arak = int(input())
    # print(arak)

    if arak > hatar_ar:
        draga_fenyofa_arak["ar"].append(arak)
        draga_fenyofa_arak["index"].append(i)

# print(draga_fenyofa_arak)

if draga_fenyofa_arak:
    min_ar = min(draga_fenyofa_arak["ar"])
    hanyadik = draga_fenyofa_arak["ar"].index(min_ar)
    # print(hanyadik)
    index = draga_fenyofa_arak["index"][hanyadik]
    print(index+1, min_ar)
else:
    print(-1)
