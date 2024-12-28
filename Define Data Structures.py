class Book:
    def __init__(self, isbn, title, author, availability=True):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.availability = availability

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}, Available: {self.availability})"

# Example usage
book1 = Book(1001, "Things Fall Apart", "Chinua Achebe")
book2 = Book(1002, "1984", "George Orwell", False)

print(book1)
print(book2)