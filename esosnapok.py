M = int(input())
eso_mennyisegek = []
for i in range(M):
    eso_mennyisegek.append(int(input()))

nap = 0

for x in eso_mennyisegek:
    if x > 0:
        nap += 1

print(nap)
