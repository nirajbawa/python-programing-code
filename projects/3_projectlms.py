class library:
    
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("books present in this library are: ")
        for index,book in enumerate(self.books):
            print("\t "+str(index+1)+") "+book)

    def borrowbook(self, bookname):
        if bookname  in  self.books:
            print("you have been issued. " + bookname+ " please keep it safe and return it withinn 30 days")
            self.books.remove(bookname)
        else:
            print("sorry, this book has already bee issued to  someone else. please wait until the book  is available")   
            return False     
             
    def returnbook(self, bookname):
        self.books.append(bookname)
        print("thanks for returning this book! hope you enjoyed it. have a great day a head!")

class student :
    def requestbook(self):
        self.book = raw_input("enter the name  of book you want to borrow : ")
        return self.book

    def returnbook(self):
        self.book = raw_input("enter the name  of book you want to return : ")
        return self.book

if __name__ == "__main__":
    centralibrary = library(["algorithms", "django", "clrs", "python notes"])

    student = student()


    while(True):
        welcomemsg = '''\n
        =======welcome to centeral library=========
                 please choose an option :
                 1. list all the books
                 2. request a book
                 3. add/return a book
                 4. exit the library
         '''

        


        print(welcomemsg)
        a = int(input("enter a choice : "))


        try:


                if a == 1:
                    centralibrary.displayAvailableBooks()
                elif a==2:
                    centralibrary.borrowbook(student.requestbook())
                elif a ==3:
                    centralibrary.returnbook(student.returnbook())
                elif a==4:
                    print("thanks  of using this library. have a  great day a head")
                    exit()
                else:
                    print("invalid  choice!")

        except Exception as e:
            print(e)
       

