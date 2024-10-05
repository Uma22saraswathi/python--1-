class library:
    def __init__(self,listofbooks):
        self.books = listofbooks
        self.borrowed_books = {}

    def availablebooks(self):
        print("book present in this library are : ")    
        for index, book in enumerate (self.books,start =1):
            print(f"{index}. {book}")

    def borrowbook(self,bookname,borrower_name):
        if bookname  in self.books:
            print("you have been issued.")
            self.books.remove(bookname)
            self.borrowed_books[bookname] = borrower_name
            return True
        else:
            print("sorry this book is not available in this library")
            return False
        
    def returnbook(self,bookname):
        if bookname in self.borrowed_books:
          self.books.append(bookname)
          borrower_name = self.borrowed_books.pop(bookname)
          print("Thanks for returning the book.")
          print(f"Book was borrowed by: {borrower_name}, and now returned the book")
        else:
          print("This book was not borrowed from this library.")

    def show_borrowed_books(self):
        """Display the list of borrowed books and their borrowers."""
        if not self.borrowed_books:
            print("No books are currently borrowed.")
        else:
            print("Borrowed books and their borrowers:")
            for book, borrower in self.borrowed_books.items():
                print(f"{book} - Borrowed by: {borrower}")

class Student:
    def __init__(self):
        self.name = input(" Please Enter your name : ").strip()

    def requestbook(self):
         self.book = input("Enter the name of the book you want to borrow : ")
         return self.book
    
    def returnbook(self):
        self.book = input("Enter the name of the return book : ")
        return self.book
    
centrallibrary = library(["GK","Literature","History","Story book ","Newspaper"])  
student = Student() 

welcomemsg = """
    WELCOME TO OUR LIBRARY
    
press 1 books list in library
press 2 enter the name of the book you want to borrow
press 3 enter the name of return book
press 4 show borrowed books in the library
Press 5 exit the library

   PLEASE ENTER THE NUMBER BETWEEN 1 AND 5 
"""
print(welcomemsg)
while (True):
    a = int(input("Enter a choice : "))

    if a == 1:
        centrallibrary.availablebooks()

    elif a ==2:
        book_to_borrow = student.requestbook()
        centrallibrary.borrowbook(book_to_borrow, student.name)
          
    elif a ==3:
         book_to_return = student.returnbook()
         centrallibrary.returnbook(book_to_return)
         
    elif a== 4:
        centrallibrary.show_borrowed_books()

    elif a ==5:
        print("thanks for choosing our library.") 
        exit()
    else:
     print("invalid choice please enter a number between 1 to 4")       
