while True:
    print("Choose the program you want to run")
    print("Program #1")
    print("Program #2")
    print("Program #3")
    print("Program #4")
    print("Program #5")
    print("Program #6")

    choice = int(input("Enter your choice: "))

    if choice == 1:
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

    elif choice == 2:
        print("Program #2 selected")

    elif choice == 3:
        print("Program #3 selected")

    elif choice == 4:
        print("Program #4 selected")

    elif choice == 5:
        print("Program #5 selected")

    elif choice == 6:
        print("Program #6 selected")

    else:
        print("Invalid choice")

    answer = input("Do you want to continue? Y/N: ")

    if answer.upper() != "Y":
        break