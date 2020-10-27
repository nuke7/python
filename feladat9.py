persons, age, wage = (input()).split()
data = []
for i in range(int(persons)):
    data.append(input())

employee = 0

for x in data:
    min = int(x.split()[0])
    max = int(x.split()[1])
    if min > int(age) and max < int(wage):
        employee += 1

print(employee)
