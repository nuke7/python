M = int(input())
homersekletek = []
for i in range(M):
    homersekletek.append(int(input()))

nap = 0

for x in homersekletek:
    if x < 0:
        nap += 1

print(nap)
