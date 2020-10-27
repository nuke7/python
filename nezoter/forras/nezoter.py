kat_file = open("kategoria.txt", "r")
fog_file = open("foglaltsag.txt", "r")

foglaltsag = []
for _ in range(15):
    sor = fog_file.readline().strip()
    foglaltsag.append(sor)

kategoriak = []
for _ in range(15):
    sor = kat_file.readline().strip()
    kategoriak.append(sor)

# print(foglaltsag)
# print(kategoriak)

# feladat2
f2_sor = int(input("sor szam: "))
f2_szek = int(input("szek szam: "))

if foglaltsag[f2_sor-1][f2_szek-1] == "x":
    print("foglalt")
else:
    print("szabad")
