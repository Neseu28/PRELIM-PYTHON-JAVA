size = int(input("Enter Size of Array : "))

numbers = []

print("Enter any", size, "elements in Array:")

for i in range(size):
    number = int(input())
    numbers.append(number)

print("Even Elements:", end=" ")
for number in numbers:
    if number % 2 == 0:
        print(number, end=" ")

print()

print("Odd Elements:", end=" ")
for number in numbers:
    if number % 2 != 0:
        print(number, end=" ")