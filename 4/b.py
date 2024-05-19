print("Masukkan jumlah bilangan: ", end="")
size = int(input())
numbers = [1]
for i in range(1, size):
    numbers.append(numbers[i-1]+2)
numbers.reverse()
for number in numbers:
    for _ in range(number):
        print("*", end="")
    print("")
