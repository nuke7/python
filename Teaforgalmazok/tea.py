vasarlasok = int(input())

fajtak = []

for _ in range(vasarlasok):
    fajta = input()
    mennyiseg = input()
    if fajta not in fajtak:
        fajtak.append(fajta)

print(len(fajtak))
