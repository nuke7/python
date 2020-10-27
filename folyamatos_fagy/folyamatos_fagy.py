bemenet = input().split()
napok, idotartam = int(bemenet[0]), int(bemenet[1])

napi_min = []
napi_max = []
index = []
counter = 0
megoldas = 0

for i in range(napok):
    homerseklet = input().split()
    min_hom, max_hom = int(homerseklet[0]), int(homerseklet[1])
    napi_max.append(max_hom)
    napi_min.append(min_hom)
    index.append(i)
    if napi_min[i] < 0 and napi_max[i] < 0:
        counter += 1
        if counter == idotartam:
            megoldas = 1
            break
        else:
            megoldas = 0
    else:
        counter = 0


if megoldas:
    print((index[i-idotartam+1])+1, index[i]+1)
else:
    print(-1)
