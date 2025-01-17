import os

userData = []
bookData = []
activeUser = ""

class User:
    def __init__(self, username, password, fullName, birtOfDate, school):
        self.username = username
        self.password = password
        self.fullName = fullName
        self.bod = birtOfDate
        self.school = school

class Book:
    def __init__(self, title, author, year, count):
        self.title = title
        self.author = author
        self.year = year
        self.count = count
    
    def isBorrow(self):
        if self.count != 0:
            self.count -= 1
        else:
            print("Faild to borrow the book!")
            return False
        print(f"Successfull to borrow {self.title} ({self.year}, {self.author}, {self.category})")
        return True
    
    def returnBook(self):
        self.count += 1
        print(f"Success to return {self.title}")

class Comic(Book):
    def __init__(self, title, author, year, count):
        super().__init__(title, author, year, count)
        self.category = "Comic"

class Novel(Book):
    def __init__(self, title, author, year, count):
        super().__init__(title, author, year, count)
        self.category = "Comic"

class Education(Book):
    def __init__(self, title, author, year, count):
        super().__init__(title, author, year, count)
        self.category = "Comic"

def userRegister():
    try:
        print("Please fill in the following form!")
        username = input("Username: ")

        # Check username
        for i in userData:
            if username == i.username:
                raise NameError

        password = input("Password: ")
        fullName = input("Full Name: ")
        bod = input("Birth of Date: ")
        school = input("School: ")

        newUser = User(username, password, fullName, bod, school)

        userData.append(newUser)

        print("Thanks for registering!")
    except NameError:
        print("Username alredy used! Please select another username")

def userLogin():
    global activeUser
    try:
        print("Please Login First!")
        username = input("Username: ")
        pasword = input("Password: ")

        for i in userData:
            if username == i.username:
                if pasword == i.password:
                    activeUser = i
                    return True;
                else:
                    raise RuntimeError
        else:
            raise NameError
    except RuntimeError:
        print("Password doesn't match")
        return False;
    except NameError:
        print("User nor found, please register first!")
        return False

def donateBook():
    try:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = int(input("Enter book realesed year: "))
        category = int(input("Enter book category!\n1. Comic\n2. Novel\n3. Education\n>"))
        count = int(input("How many books would you like to donate: "))

        if category == 1:
            newBook = Comic(title, author, year, count)
            bookData.append(newBook)
            print(f"Thank you {activeUser.fullName} for the book donation!")
        elif category == 2:
            newBook = Novel(title, author, year, count)
            bookData.append(newBook)
            print(f"Thank you {activeUser.fullName} for the book donation!")
        elif category == 3:
            newBook = Education(title, author, year, count)
            bookData.append(newBook)
            print(f"Thank you {activeUser.fullName} for the book donation!")
        else:
            print("Please select the valid category!")
    except ValueError:
        print("Please enter the valid value!")

def returnBook():
    try:
        os.system("clear")
        if len(bookData) == 0:
            print("There are no books in library!")
            return

        print("Please select a book, you want to return!")
        count = 0
        num = 1
        for i in bookData:
            if i.count == 0:
                count += 1
                print(f"{num}. {i.title} ({i.category})")
            num +=1
        
        if count != 0:
            userInput = int(input("-> "))
            bookData[userInput-1].returnBook()

            question = input("Do you want to return another book? (Y/N): ")
            if question.lower() == "y":
                returnBook()
        else:
            print("Books are still available to borrow!")
    except ValueError:
        input("Please enter the valid option!")
        returnBook()
    except IndexError:
        input("Please enter the valid option!")
        returnBook()

def borrowBook():
    try:
        if len(bookData) == 0:
            print("There are no books in library!")
            return
        
        print("Please select a book you want to borrowed!")
        num = 1
        for i in bookData:
            print(f"{num}. {i.title} ({i.category})")
            num +=1
        userSelected = int(input("-> "))
        if bookData[userSelected-1].isBorrow() != True:
            option = input("Do you want to return the book first (Y/N): ")
            if option.lower() == "y":
                returnBook()
    except ValueError:
        print("Please enter the valid value!")
    except IndexError:
        print("Please select the valid book title!")
        
def librarySystem():
    global activeUser
    if userLogin() != True:
        return

    while True:
        os.system("clear")
        try:
            print(f"Welcome back {activeUser.fullName}")
            inputUser = int(input("What do you want to do?\n1. Borrow a book\n2. Return a book\n3. Donate book\n4. Log Out\nYour choice: "))

            if inputUser == 1:
                borrowBook()
            elif inputUser == 2:
                returnBook()
            elif inputUser == 3:
                donateBook()
            elif inputUser == 4:
                break
        except ValueError:
            print("Please enter the valid option!")
        input("Press enter to continue ...")

while True:
    os.system("clear")
    try:
        print("Library Management System!")
        inputUser = int(input("1. Login\n2. Register\n3. Quit\nYour choice: "))

        if inputUser == 1:
            librarySystem()
        elif inputUser == 2:
            userRegister()
        elif inputUser == 3:
            break
        else:
            print("Please select the valid option!")
    except ValueError:
        print("Please enter the valid option!")
    input("Press enter to continue ...")