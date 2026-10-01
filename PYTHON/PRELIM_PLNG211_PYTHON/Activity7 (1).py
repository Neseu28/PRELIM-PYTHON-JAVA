while True:
    print("\n==============================")
    print(" ARITHMETIC CALCULATOR")
    print("==============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Increment")
    print("7. Decrement")

    while True:
        try:
            choice = int(input("\nSelect an arithmetic operation: "))
            if 1 <= choice <= 7:
                break
            print("Invalid option. Please select a number from 1 to 7.")
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 7.")

    if choice in [1, 2, 3, 4, 5]:
        while True:
            try:
                x = float(input("Enter the value of x: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        while True:
            try:
                y = float(input("Enter the value of y: "))
                if choice in [4, 5] and y == 0:
                    print("Error: y cannot be zero for division or modulus.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        print("\nVariable Values: x = {}, y = {}".format(x, y))

        if choice == 1:
            result = x + y
            print("Addition: x + y = {}".format(result))
        elif choice == 2:
            result = x - y
            print("Subtraction: x - y = {}".format(result))
        elif choice == 3:
            result = x * y
            print("Multiplication: x * y = {}".format(result))
        elif choice == 4:
            result = x / y
            print("Division: x / y = {}".format(result))
        else:
            result = x % y
            print("Modulus: x % y = {}".format(result))

    elif choice == 6:
        while True:
            try:
                x = float(input("Enter the value of x: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        result = x + 1
        print("\nVariable Value: x = {}".format(x))
        print("Increment: x + 1 = {}".format(result))

    else:
        while True:
            try:
                x = float(input("Enter the value of x: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        result = x - 1
        print("\nVariable Value: x = {}".format(x))
        print("Decrement: x - 1 = {}".format(result))

    while True:
        continue_program = input(
            "\nDo you want to continue? (YES/NO): "
        ).strip().upper()

        if continue_program == "YES":
            break
        elif continue_program == "NO":
            print("\nProgram terminated. Thank you!")
            raise SystemExit
        else:
            print("Invalid input. Please enter YES or NO.")