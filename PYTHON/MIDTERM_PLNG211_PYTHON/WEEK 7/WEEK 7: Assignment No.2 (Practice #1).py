# WEEK 7
# PLNG Midterm Lab Practice #1
# Programs 1-5

def program_1():
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


def program_2():
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


def program_3():
    numbers = input("Enter Data in Array: ").split()

    print("Stored Data in Array:", " ".join(numbers))

    position = int(input("Enter poss. of Element to Delete: "))

    numbers.pop(position - 1)

    print("New data in Array:", " ".join(numbers))


def program_4():
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


def program_5():
    for i in range(4):
        print("*A" * i + "*")


def program_6():

    while True:
        print("\nChoose the program you want to run")
        print("Program #1 - Positive/negative numbers and minimum")
        print("Program #2 - Remove duplicates and find second smallest/largest")
        print("Program #3 - Delete an array element")
        print("Program #4 - Display even and odd elements")
        print("Program #5 - Print pattern")
        print("Program #6 - Salary calculator")
        print("0 - Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            program_1()
        elif choice == "2":
            program_2()
        elif choice == "3":
            program_3()
        elif choice == "4":
            program_4()
        elif choice == "5":
            program_5()
        elif choice == "6":
            basic = 12000

            da = basic * 0.12
            hra = 150
            ta = 120
            others = 450

            pf = basic * 0.14
            it = basic * 0.15

            net_salary = basic + da + hra + ta + others - (pf + it)

            print("Basic Salary:", basic)
            print("DA:", da)
            print("HRA:", hra)
            print("TA:", ta)
            print("Others:", others)
            print("PF:", pf)
            print("IT:", it)
            print("Net Salary:", net_salary)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

        answer = input("\nDo you want to continue? Y/N: ")

        if answer.upper() != "Y":
            break


if __name__ == "__main__":
    program_6()
