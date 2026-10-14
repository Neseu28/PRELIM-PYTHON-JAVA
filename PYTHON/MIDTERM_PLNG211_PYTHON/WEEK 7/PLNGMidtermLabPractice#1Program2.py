numbers = []

# Input
for i in range(8):
    number = int(input("Enter integer: "))
    numbers.append(number)

# Remove duplicate
unq_numbers = []

for number in numbers:
    if number not in unq_numbers:
        unq_numbers.append(number)

print("Array without duplicates:", unq_numbers)

unq_numbers.sort()

sec_smallest = unq_numbers[1]

sec_largest = unq_numbers[-2]

print("Second smallest:", sec_smallest)
print("Second largest:", sec_largest)