# WEEK 9
# PLNG MIDTERM - LAB ACTIVITY #4


from datetime import date


def read_nonnegative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Amount cannot be negative. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def read_date(prompt):
    while True:
        try:
            value = input(prompt).strip()
            year, month, day = map(int, value.split("-"))
            return date(year, month, day)
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD (for example, 2026-10-20).")


class Patient:
    def __init__(self, name, admission_date, disease, discharge_date):
        self.name = name
        self.admission_date = admission_date
        self.disease = disease
        self.discharge_date = discharge_date

    def display(self):
        print(f"Name: {self.name}")
        print(f"Date of admission: {self.admission_date}")
        print(f"Disease: {self.disease}")
        print(f"Date of discharge: {self.discharge_date}")


class PediatricPatient(Patient):
    def __init__(self, name, admission_date, disease, discharge_date, age):
        super().__init__(name, admission_date, disease, discharge_date)
        self.age = age

    def display(self):
        super().display()
        print(f"Age: {self.age}")


def program_1():
    print("\n--- Program 1: Account Balance ---")
    balance = read_nonnegative_float("Enter your balance: ")

    while True:
        print("\nSelect an option:")
        print("1. Withdraw Amount")
        print("2. Deposit Amount")
        print("3. Exit to main menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            amount = read_nonnegative_float("How much amount do you want to withdraw? ")
            if amount > balance:
                print("Insufficient balance. Withdrawal was not completed.")
            else:
                balance -= amount
                print("Your new balance is:", balance)
        elif choice == "2":
            amount = read_nonnegative_float("How much amount do you want to deposit? ")
            balance += amount
            print("Your new balance is:", balance)
        elif choice == "3":
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def program_2():
    print("\n--- Program 2: Hospital Patient Database ---")
    patients = []

    while True:
        print("\n1. Insert New Patient")
        print("2. Display All Patients")
        print("3. Display Pediatric Patients (under 12)")
        print("4. Return to main menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                name = input("Name of patient: ").strip()
                if not name:
                    raise ValueError("Name cannot be empty.")
                admission = read_date("Date of admission (YYYY-MM-DD): ")
                disease = input("Disease: ").strip()
                if not disease:
                    raise ValueError("Disease cannot be empty.")
                discharge = read_date("Date of discharge (YYYY-MM-DD): ")
                if discharge < admission:
                    raise ValueError("Discharge date cannot be before admission date.")
                while True:
                    try:
                        age = int(input("Age: "))
                        if age < 0:
                            print("Age cannot be negative.")
                            continue
                        break
                    except ValueError:
                        print("Invalid age. Enter a whole number.")
                patients.append(PediatricPatient(name, admission, disease, discharge, age))
                print("Patient added successfully.")
            except ValueError as error:
                print("Could not add patient:", error)
        elif choice == "2":
            if not patients:
                print("No patients in the database.")
            else:
                print("\n--- All Patients ---")
                for index, patient in enumerate(patients, start=1):
                    print(f"\nPatient {index}")
                    patient.display()
        elif choice == "3":
            pediatric = [patient for patient in patients if patient.age < 12]
            if not pediatric:
                print("No pediatric patients found.")
            else:
                print("\n--- Pediatric Patients (under 12) ---")
                for index, patient in enumerate(pediatric, start=1):
                    print(f"\nPatient {index}")
                    patient.display()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select 1-4.")


class Professor:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}\nSalary: {self.salary:.2f}"


class Dean(Professor):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return (f"Rank: Dean\nName: {self.name}\n"
                f"Department: {self.department}\nSalary: {self.salary:.2f}")


class Executive(Dean):
    def __str__(self):
        return "Rank: Executive\n" + super().__str__().replace("Rank: Dean\n", "")


def program_3():
    print("\n--- Program 3: Professor, Dean, and Executive ---")
    try:
        dean_name = input("Enter Dean's name: ").strip()
        if not dean_name:
            raise ValueError("Name cannot be empty.")
        department = input("Enter department: ").strip()
        if not department:
            raise ValueError("Department cannot be empty.")
        while True:
            try:
                dean_salary = float(input("Enter Dean's salary: "))
                if dean_salary < 0:
                    print("Salary cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid salary. Enter a number.")

        executive_name = input("\nEnter Executive's name: ").strip()
        if not executive_name:
            raise ValueError("Name cannot be empty.")
        executive_department = input("Enter Executive's department: ").strip()
        if not executive_department:
            raise ValueError("Department cannot be empty.")
        while True:
            try:
                executive_salary = float(input("Enter Executive's salary: "))
                if executive_salary < 0:
                    print("Salary cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid salary. Enter a number.")

        dean = Dean(dean_name, dean_salary, department)
        executive = Executive(executive_name, executive_salary, executive_department)

        print("\n--- Dean Information ---")
        print(dean)
        print("\n--- Executive Information ---")
        print(executive)
    except ValueError as error:
        print("Invalid data:", error)


def main():
    programs = {
        "1": ("Account balance: withdraw and deposit", program_1),
        "2": ("Hospital patient database and pediatric list", program_2),
        "3": ("Professor, Dean, and Executive classes", program_3),
    }

    while True:
        print("\n========== PLNG MIDTERM LAB ACTIVITY #4 ==========")
        for key, (description, _) in programs.items():
            print(f"{key}. {description}")
        print("0. Exit")

        choice = input("Choose a program: ").strip()
        if choice == "0":
            print("Thank you for using the system!")
            break
        if choice not in programs:
            print("Invalid choice. Please choose 1, 2, 3, or 0.")
            continue

        try:
            programs[choice][1]()
        except (KeyboardInterrupt, EOFError):
            print("\nInput cancelled.")
        except Exception as error:
            print("An unexpected error occurred:", error)

        again = input("\nReturn to the main menu? (Y/N): ").strip().upper()
        if again != "Y":
            print("Thank you for using the system!")
            break


if __name__ == "__main__":
    main()
