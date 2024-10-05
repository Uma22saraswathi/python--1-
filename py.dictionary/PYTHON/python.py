class library:
    def __init__(self,listofbooks):
        self.books = listofbooks
    def availablebooks(self):
        print("library books : ")
        for book in self.books:
            print(" "+ book)
    def  borrowbook(self,bookname):
        if bookname in self.books:
            print(f"you have been issued {bookname}. Please keep it safe and return within 30 days")
            self.books.remove(bookname)
            return True
        else:
            print("sorry, this book is not available in the library")
            return False
    def returnbook(self,bookname):
        self.books.append(bookname)
        print("thanks for returning the book")
            
class student:
    def requestbook(self):
        self.book = input ("enter the name of the book you want to borrow :")
        return self.book
    def  returnbook(self):
        self.book = input ("enter the name of the book in return : ")
        return self.book
if __name__=="__main__":
  centrallibrary = library(["javascript","php","python","c++","java"])
  student = student()
  while(True):
    welcomeMsg = "welcome to simple library"
    print(welcomeMsg)
    a=(input("enter a choice : "))
    if a == 1:
        centrallibrary.availablebooks()
    elif a ==2:
        centrallibrary.borrowbook(student.requestbook())
    elif a ==3:
        centrallibrary.returnbook(student.returnbook())
    elif a ==4:
        print("Thanks for choosing our library. ")
        exit()
    else:
        print("invalid choice")                
    
    

        
        
                    
                
                    
