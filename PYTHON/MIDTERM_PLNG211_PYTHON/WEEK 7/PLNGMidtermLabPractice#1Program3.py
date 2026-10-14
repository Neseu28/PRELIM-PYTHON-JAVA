numbers = input("Enter Data in Array: ").split()

print("Stored Data in Array:", " ".join(numbers))

position = int(input("Enter poss. of Element to Delete: "))

numbers.pop(position - 1)

print("New data in Array:", " ".join(numbers))