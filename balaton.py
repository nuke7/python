N = int(input())
jegvastagsagok = []
for i in range(N):
    jegvastagsagok.append(int(input()))

napok = 0

for x in range(len(jegvastagsagok)):
    if jegvastagsagok[x] > 0:
        napok += 1

print(napok)
