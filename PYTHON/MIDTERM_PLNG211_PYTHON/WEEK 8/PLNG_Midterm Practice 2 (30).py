"""LAB Activity #1 - Python Programming Practice /Pick a program number from the menu.
"""

import datetime
import math
import random


# ---------- Program 1 ----------
def program_1():
    print("Hello World")


# ---------- Program 2 ----------
def program_2():
    usertext = input("What is your name? ")
    print("Hello", usertext)


# ---------- Program 3 ----------
def program_3():
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    total = float(num1) + float(num2)
    print("The sum of {0} and {1} is {2}".format(num1, num2, total))


# ---------- Program 4 ----------
def program_4():
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    average = (float(num1) + float(num2)) / 2 # fixed: original never divided by 2
    print("average: {0}".format(average))


# ---------- Program 5 ----------
def program_5():
    visagrade = input("enter your visa grade : ")
    finalgrade = input("enter your final grade : ")
    average = (float(visagrade) * 0.3) + (float(finalgrade) * 0.7)
    print("average : {0}".format(average))


# ---------- Program 6 ----------
def program_6():
    firstexam = input("your first exam : ")
    secondexam = input("your second exam : ")
    thirdexam = input("your third exam : ")
    average = (float(firstexam) + float(secondexam) + float(thirdexam)) / 3
    print("average : {0}".format(average))


# ---------- Program 7 ----------
def program_7():
    average = float(input("enter average : ")) # float so decimals work
    if average >= 50:
        print("Passed")
    else:
        print("Failed")


# ---------- Program 8 ----------
def program_8():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("{0} is Even".format(num))
    else:
        print("{0} is Odd".format(num))


# ---------- Program 9 ----------
def program_9():
    num = float(input("Enter a number: "))
    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")


# ---------- Program 10 ----------
def program_10():
    print("body mass index calculation program")
    height = float(input("enter height (m): "))
    weight = float(input("enter weight (kg): "))
    if height <= 0:
        print("Height must be greater than 0.")
        return
    index = weight / (height * height)

    # Standard WHO categories (original labels/ranges were incorrect)
    if index < 18.5:
        label = "underweight"
    elif index < 25:
        label = "normal weight"
    elif index < 30:
        label = "overweight"
    else:
        label = "obese"
    print("\n {0} BMI: {1:.2f}".format(label, index))


# ---------- Program 11 ----------
def program_11():
    age = int(input("enter age : "))
    if age < 18:
        print("Your Age Is Not Eligible To Get A Driver's License")
    else:
        print("Your Age Is Eligible To Get Your License")


# ---------- Program 12 ----------
def program_12():
    for i in range(1, 101):
        print(i)


# ---------- Program 13 ----------
def program_13():
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)


# ---------- Program 14 ----------
def program_14():
    for i in range(1, 101):
        if i % 2 != 0:
            print(i)


# ---------- Program 15 ----------
def program_15():
    # Kept as in the PDF: divisible by 3 OR 5
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0:
            print(i)


# ---------- Program 16 ----------
def program_16():
    num = int(input("enter number : "))
    for i in range(1, num + 1):
        print(i)


# ---------- Program 17 ----------
def program_17():
    short = float(input("Enter short side : "))
    tall = float(input("Enter tall side : "))
    area = short * tall
    perimeter = 2 * (short + tall)
    print("area: {0}".format(area)) # fixed: original used undefined names
    print("perimeter: {0}".format(perimeter))


# ---------- Program 18 ----------
def program_18():
    word = input("Enter a text: ") # original hardcoded 'mrhuseyin'
    for char in word:
        print(char)


# ---------- Program 19 ----------
def program_19():
    sumofnumbers = 0
    num1 = input("first number: ")
    num2 = input("second number: ")
    for i in range(int(num1) + 1, int(num2)): # fixed: original used undefined names
        sumofnumbers += i
    print("Sum of numbers between {0} and {1} : {2}".format(num1, num2, sumofnumbers))


# ---------- Program 20 ----------
def program_20():
    selection = input("Press (1) for Cinema, (2) for Theater : ")
    student = input("Are you student(Y/N) : ")
    price = 0
    # non-discounted fee calculation
    if selection == "1":
        price = 10 # cinema
    elif selection == "2":
        price = 5 # theatre
    else:
        print("Invalid selection.")
        return
    # student discount
    if student == "Y" or student == "y":
        price = price / 2 # 50%
    print(" The fee you have to pay :{}".format(price))


# ---------- Program 21 ----------
def program_21():
    num = int(input("Enter a number: "))
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


# ---------- Program 22 ----------
def program_22():
    num_list = []
    even_sum = 0
    odd_sum = 0

    number = int(input("Please enter the Total Number of List Elements: "))
    for i in range(1, number + 1):
        value = int(input("Please enter the Value of %d Element : " % i))
        num_list.append(value)

    for j in range(number):
        if num_list[j] % 2 == 0:
            even_sum = even_sum + num_list[j]
        else:
            odd_sum = odd_sum + num_list[j]

    print("\nThe Sum of Even Numbers in this List = ", even_sum)
    print("The Sum of Odd Numbers in this List = ", odd_sum)


# ---------- Program 23 ----------
def program_23():
    salary = input("enter salary : ")
    raise_rate = input("salary raise rate(%) : ") # 'raise' is a reserved word
    newsalary = float(salary) + (float(salary) * float(raise_rate) / 100)
    print("increased salary :", newsalary)


# ---------- Program 24 ----------
def find_diameter(radius):
    return 2 * radius


def find_circumference(radius):
    return 2 * math.pi * radius


def find_area(radius):
    return math.pi * radius * radius


def program_24():
    r = float(input(" Please Enter the radius of a circle: "))
    diameter = find_diameter(r)
    circumference = find_circumference(r)
    area = find_area(r)
    print("\n Diameter Of a Circle = %.2f" % diameter)
    print(" Circumference Of a Circle = %.2f" % circumference)
    print(" Area Of a Circle = %.2f" % area)


# ---------- Program 25 ----------
def area_rectangle(a, b):
    return a * b


def perimeter_rectangle(a, b):
    return 2 * (a + b)


def program_25():
    a = float(input("Enter width: ")) # original hardcoded 5 and 6
    b = float(input("Enter height: "))
    print("Area = ", area_rectangle(a, b))
    print("Perimeter = ", perimeter_rectangle(a, b))


# ---------- Program 26 ----------
def program_26():
    lower = int(input("Enter Lower bound:- "))
    upper = int(input("Enter Upper bound:- "))
    if upper < lower:
        print("Upper bound must be >= lower bound.")
        return

    x = random.randint(lower, upper)
    max_tries = math.log(upper - lower + 1, 2)
    print("\n\tYou've only ", round(max_tries), " chances to guess the integer!\n")

    count = 0
    guessed = False
    while count < max_tries:
        count += 1
        guess = int(input("Guess a number:- "))
        if x == guess:
            print("Congratulations you did it in ", count, " try")
            guessed = True
            break
        elif x > guess:
            print("You guessed too small!")
        else:
            print("You Guessed too high!")

    if not guessed: # fixed: original also printed this after a late correct guess
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")


# ---------- Program 27 ----------
def program_27():
    date = input("Enter the date(for example:09 02 2019): ")
    day_name = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]
    parsed = datetime.datetime.strptime(date, "%d %m %Y")
    print("Day of the week:", day_name[parsed.weekday()])
    # The title asks for the day of the year, so this is shown too
    print("Day of the year:", parsed.timetuple().tm_yday)


# ---------- Program 28 ----------
def find_missing(lst):
    if not lst:
        return []
    present = set(lst)
    return [x for x in range(lst[0], lst[-1] + 1) if x not in present]


def program_28():
    lst = [1, 2, 4, 6, 7, 9, 10]
    print(find_missing(lst)) # [3, 5, 8]


# ---------- Program 29 ----------
def program_29():
    char_list = ["a", "b", "c"]
    string = "abcd"
    matched_list = [characters in char_list for characters in string]
    print(matched_list) # [True, True, True, False]

    string_contains_chars = all(matched_list)
    print(string_contains_chars)


# ---------- Program 30 ----------
def program_30():
    total = 0
    evens = []
    odds = []
    while True:
        user_in = input("Give me an integer or type 'done' to be done. ")
        if user_in.lower() == "done":
            break
        try:
            value = int(user_in)
        except ValueError:
            print("Please enter a whole number or 'done'.")
            continue
        total += value
        if value % 2 == 0:
            evens.append(value)
        else:
            odds.append(value)

    print(total)
    if evens:
        print("Even Average: " + str(sum(evens) / len(evens)))
    else:
        print("Even Average: no even numbers entered")
    if odds:
        print("Odd Average: " + str(sum(odds) / len(odds)))
    else:
        print("Odd Average: no odd numbers entered")


# ---------- Menu ----------
TITLES = {
    1: "Print Hello World",
    2: "Hello + username",
    3: "Add 2 numbers",
    4: "Average of 2 numbers",
    5: "Visa and final grade average",
    6: "Average of 3 exam grades",
    7: "Pass / fail status",
    8: "Odd or even",
    9: "Positive, negative or zero",
    10: "Body mass index",
    11: "Driver's license eligibility",
    12: "List 1-100",
    13: "List even numbers 1-100",
    14: "List odd numbers 1-100",
    15: "Numbers 1-100 divisible by 3 or 5",
    16: "List 1 to entered number",
    17: "Rectangle area and perimeter",
    18: "Letters of a text, one per line",
    19: "Sum of numbers between two numbers",
    20: "Cinema / theater ticket price",
    21: "Prime or not",
    22: "Sum of odd and even list values",
    23: "Salary raise",
    24: "Circle diameter, circumference, area",
    25: "Rectangle area and perimeter (functions)",
    26: "Number guessing game",
    27: "Weekday and day of year of a date",
    28: "Missing numbers in a sorted list",
    29: "Characters check in a string",
    30: "Odd and even averages",
}

PROGRAMS = {n: globals()["program_%d" % n] for n in TITLES}


def main():
    while True:
        print("\n=== LAB Activity #1 ===")
        for n, title in TITLES.items():
            print("{:>2}. {}".format(n, title))
        print(" 0. Exit")

        choice = input("Choose a program number: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        if choice.isdigit() and int(choice) in PROGRAMS:
            print()
            try:
                PROGRAMS[int(choice)]()
            except ValueError as err:
                print("Invalid input:", err)
            except (EOFError, KeyboardInterrupt):
                print("\nInput cancelled.")
        else:
            print("Please enter a number from 0 to 30.")


if __name__ == "__main__":
    main()