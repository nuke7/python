name = input("mi a neved?\n")
age = int(input("hány éves vagy?\n"))
# ez csak string lesz, az input mindig string-ként tárolja az adatot

print("hello " + name + "!")
print("tíz év múlva " + str(int(age)+10) + " éves leszel!")

if (age) < 18:
    print("kiskorú")
else:
    print("nagykorú")
