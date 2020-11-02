lovak_szama = int(input())


for i in range(lovak_szama):
    lo_ero = int(input())
    if lo_ero <= 50:
        print(0)
    elif lo_ero > 50 and lo_ero <= 55:
        print(5)
    elif lo_ero > 55 and lo_ero <= 60:
        print(10)
    elif lo_ero > 60 and lo_ero <= 65:
        print(15)
    elif lo_ero > 65 and lo_ero <= 70:
        print(20)
    elif lo_ero > 70 and lo_ero <= 75:
        print(25)
    elif lo_ero > 75 and lo_ero <= 80:
        print(30)
    elif lo_ero > 80 and lo_ero <= 85:
        print(35)
    elif lo_ero > 85 and lo_ero <= 90:
        print(40)
    elif lo_ero > 90:
        print(45)
