N = int(input())
V_kat = "NINCS"  # 0 if we want to use this as boolean
VI_kat = "NINCS"  # 0 if we want to use this as boolean
VII_kat = "NINCS"  # 0 if we want to use this as boolean
for i in range(N):
    varos = input()
    lelekszam = int(input())
    indulok = int(input())

    if lelekszam >= 8000 and lelekszam < 25000:
        V_kat = "VAN"
    elif lelekszam >= 25000 and lelekszam < 70000:
        VI_kat = "VAN"
    elif lelekszam >= 70000:
        VII_kat = "VAN"

print(V_kat, VI_kat, VII_kat)

# if V_kat:
#     print("VAN ", end="")
# else:
#     print("NINCS ", end="")
# if VI_kat:
#     print("VAN ", end="")
# else:
#     print("NINCS ", end="")
# if VII_kat:
#     print("VAN")
# else:
#     print("NINCS")
