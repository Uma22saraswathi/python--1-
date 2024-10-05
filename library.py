class Library:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "available"
    
    def borrow(self):
        if self.status == "available":
            self.status = "borrowed"
            return f"You have successfully borrowed '{self.title}'"
        else:
            return f"'{self.title}' is currently not available"
    
    def return_book(self):
        if self.status == "borrowed":
            self.status = "available"
            return f"You have successfully returned '{self.title}'"
        else:
            return f"'{self.title}' is already available"

class Student:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_book_status(self, title):
        for book in self.books:
            if book.title == title:
                return book.status
        return "Book not found"

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                return book.borrow()
        return "Book not found"

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                return book.return_book()
        return "Book not found"


student = Student()


book1 = Library("To Kill a Mockingbird", "Harper Lee")
book2 = Library("1984", "George Orwell")


student.add_book(book1)
student.add_book(book2)


print(student.borrow_book("To Kill a Mockingbird"))  
print(student.get_book_status("To Kill a Mockingbird"))  
print(student.return_book("To Kill a Mockingbird"))  
print(student.get_book_status("To Kill a Mockingbird"))
