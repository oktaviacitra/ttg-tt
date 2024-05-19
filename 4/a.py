print("Masukkan jumlah bilangan: ", end="")
size = int(input())
print("")

print("Masukkan jumlah kelompok: ", end="")
group = int(input())
print("")

count = int(size/group)
members = []
member = size
for i in range(group):
    if member-count > count:
        members.append(count)
        member = member - count
    else:
        members.append(size - (i * count))

numbers = []
number = 2
for i in range(group):
    temp = []
    for _ in range(members[i]):
        temp.append(number)
        number += 2
    numbers.append(temp)

for i in range(len(numbers)):
    print(numbers[i], end="")
print("")
