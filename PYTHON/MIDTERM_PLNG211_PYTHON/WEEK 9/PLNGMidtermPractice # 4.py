from datetime import datetime, date
import math

def main():
    print("=== Welcome Nestor Guerrero ===")

    while True:
        try:
            total_pages = int(input("Enter total pages of the book: "))
            if total_pages <= 0:
                print("Warning: Total pages must be greater than 0. Try again.\n")
            else:
                break
        except ValueError:
            print("Warning: Invalid input. Please enter a valid number.\n")

    while True:
        try:
            pages_read = int(input("Enter pages you have read: "))
            if pages_read < 0 or pages_read > total_pages:
                print(f"Warning: Pages read cannot be negative or more than total pages ({total_pages}). Try again.\n")
            else:
                break
        except ValueError:
            print("Warning: Invalid input. Please enter a valid number.\n")

    while True:
        try:
            issue_date_str = input("Enter issue date (YYYY-MM-DD): ")
            # Parse string directly into a date object
            issue_date = datetime.strptime(issue_date_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Warning: Invalid date format. Please use YYYY-MM-DD.\n")

    while True:
        try:
            due_date_str = input("Enter due date (YYYY-MM-DD): ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
            
            if due_date < issue_date:
                print("Warning: Due date cannot be before issue date. Try again.\n")
            else:
                break
        except ValueError:
            print("Warning: Invalid date format. Please use YYYY-MM-DD.\n")

    today = date.today()
    percentage = (pages_read / total_pages) * 100
    pages_left = total_pages - pages_read
    
    remaining_days = (due_date - today).days

    print("\n=== SUMMARY ===")
    print(f"You have read {percentage:.0f}% of the book.")

    if remaining_days < 0:
        print("Your book is overdue.")
    elif remaining_days == 0:
        print("Your book is due today.")
    else:
        print(f"You have {remaining_days} days remaining to return the book.")

    print(f"You have {pages_left} pages left to read.")

    if pages_left == 0:
        print("You have finished the book!")
    elif remaining_days > 0:
        pages_per_day = math.ceil(pages_left / remaining_days)
        print(f"You should read {pages_per_day} pages per day.")
    else:
        print("The book must be returned now.")

if __name__ == "__main__":
    main()
