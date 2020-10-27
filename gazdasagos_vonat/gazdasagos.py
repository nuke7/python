allomasok_szama = int(input())
koltsegek = input().split()

jegyar_allomasonkent, vonat_koltseg_allomasonkent = int(
    koltsegek[0]), int(koltsegek[1])

vonatut_koltseg = allomasok_szama * vonat_koltseg_allomasonkent

osszesen = []

for i in range(allomasok_szama):
    utasok = input().split()
    leszallo, felszallo = int(utasok[0]), int(utasok[1])
    osszesen.append(felszallo)

# print(osszesen)

bevetel = sum(osszesen) * jegyar_allomasonkent

if bevetel >= vonatut_koltseg:
    print(1)
else:
    print(0)
