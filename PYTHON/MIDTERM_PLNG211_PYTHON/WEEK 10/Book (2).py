class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return (f"Book: {self.title} | Author: {self.author}\n"
                f"Price: PHP {self.price:.2f}")

class EBook(Book):
    def __init__(self, title, author, price, file_size_mb):
        super().__init__(title, author, price)
        self.file_size_mb = file_size_mb

    def __str__(self):
        return (f"EBook: {self.title} | Author: {self.author}\n"
                f"Price: PHP {self.price:.2f} | "
                f"File size: {self.file_size_mb} MB")


def main():
    books = [
        Book("Python Basics", "Maria Santos", 450),
        EBook("Learning OOP", "Ana Cruz", 300, 5),
        EBook("Python Projects", "Juan Reyes", 550, 8)
    ]


    for book in books:
        print(book)
        print()


if __name__ == "__main__":
    main()