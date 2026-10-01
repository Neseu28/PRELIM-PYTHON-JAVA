while True:
    print("\nSTUDENT GRADE CALCULATOR")

    while True:
        try:
            java_score = float(input("Java Programming Score: "))
            if 0 <= java_score <= 100:
                break
            print("Invalid score. Please enter a score from 0 to 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric score.")

    while True:
        try:
            c_score = float(input("C Programming Score: "))
            if 0 <= c_score <= 100:
                break
            print("Invalid score. Please enter a score from 0 to 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric score.")

    while True:
        try:
            database_score = float(input("Database Handling Score: "))
            if 0 <= database_score <= 100:
                break
            print("Invalid score. Please enter a score from 0 to 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric score.")

    average = (java_score + c_score + database_score) / 3

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 75:
        grade = "C"
    else:
        grade = "F"

    print("\n===== RESULT =====")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

    while True:
        continue_program = input("\nDo you want to continue? (YES/NO): ").strip().upper()
        if continue_program == "YES":
            break
        elif continue_program == "NO":
            print("\nProgram terminated. Thank you!")
            raise SystemExit
        else:
            print("Invalid input. Please enter YES or NO.")