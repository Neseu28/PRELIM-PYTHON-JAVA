numbers = []

for i in range(10):
    number = float(input("Enter number: "))
    numbers.append(number)

positive_sum = 0
positive_count = 0

for number in numbers:
    if number > 0:
        positive_sum += number
        positive_count += 1

if positive_count > 0:
    positive_average = positive_sum / positive_count
else:
    positive_average = 0

print("Sum of positive numbers:", positive_sum)
print("Average of positive numbers:", positive_average)

negative_count = 0

for number in numbers:
    if number < 0:
        negative_count += 1

print("Count of negative numbers:", negative_count)

minimum = numbers[0]

for number in numbers:
    if number < minimum:
        minimum = number

print("Minimum value:", minimum)