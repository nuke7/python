allomasok_szama = int(input())
koltsegek = input().split()
szemelyenkenti_koltseg, vonatut_koltseg = int(koltsegek[0]), int(koltsegek[1])

ossz_utas = {"felszallok": [], "leszallok": []}
allomasonkenti_utasok = []


for i in range(allomasok_szama):
    utasok = input().split(" ")
    leszallo, felszallo = int(utasok[0]), int(utasok[1])
    ossz_utas["felszallok"].append(felszallo)
    ossz_utas["leszallok"].append(leszallo)

# print(ossz_utas)

for j in range(len(ossz_utas["leszallok"])-1):
    allomasonketi = ossz_utas["felszallok"][0] + (
        ossz_utas["felszallok"][j] + ossz_utas["felszallok"][j+1]) - ossz_utas["leszallok"][j+1]
    allomasonkenti_utasok.append(allomasonketi)

# print(allomasonkenti_utasok)

ossz_bevetel = sum([u * szemelyenkenti_koltseg for u in allomasonkenti_utasok])


# print(ossz_bevetel)

if ossz_bevetel >= (allomasok_szama * vonatut_koltseg):
    print(1)
else:
    print(0)
