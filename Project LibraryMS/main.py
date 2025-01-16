'''Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class 
and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist
the books after the program is stopped!'''

class Library:
  def __init__(self):            # Initializes the Library object with noBooks set to 0 and an empty books list.  
    self.noBooks = 0             # Tracks the number of books in the library.
    self.books = []              # A list that stores the names of the books in the library.

    
  def addBook(self, book):          # Adds a book to the books list.
    self.books.append(book)         # Updates self.noBooks to reflect the current number of books
    self.noBooks = len(self.books)


  def showInfo(self):                     # Displays the total number of books and lists the titles.
    print(f"The library has {self.noBooks} books. The books are")
    for book in self.books:
      print(book)


  def removeBook(self, book):                        # Removes a specified book from the library.
        if book in self.books:                # check if book exists or not                   
            self.books.remove(book)           # input book name to remove (a string value )
            self.noBooks = len(self.books)     # returns the updated no. of books after removal from the list
            print(f"'{book}' has been removed from the library.")
        else:
            print(f"'{book}' is not in the library.")        # if book not found , informs the user


  def searchBook(self, book):
        if book in self.books:  # Checks if a specified book is available in the
            print(f"'{book}' is available in the library.")
        else:         
            print(f"'{book}' is not available in the library.")      # Prints whether the book is available or not after searching


  def saveLibraryState(self, filename="library_state.txt"):                 # Saves the current state of the library (all books) to a file.
        with open(filename, "w") as file:                      # Input: filename (optional; default is "library_state.txt")
            for book in self.books:
                file.write(book + "\n")             # Writes each book in the books list to the file, one book per line.Prints a confirmation that the library state has been saved.
        print("Library state saved.")


  def loadLibraryState(self, filename="library_state.txt"):           # Loads the library state from a saved file.
        try:
            with open(filename, "r") as file:
                self.books = [line.strip() for line in file.readlines()]        # Reads the file and populates the books list with its content.
                self.noBooks = len(self.books)     # #Updates noBooks to match the number of books loaded. 
            print("Library state loaded.")
        except FileNotFoundError:          # Handles the case where the file does not exist, notifying the user.
            print("No saved library state found.")


  def borrowBook(self, book):
        if book in self.books:
            self.books.remove(book)
            self.noBooks = len(self.books)
            print(f"You have borrowed '{book}'. Please return it soon.")
        else:
            print(f"'{book}' is not available to borrow.")


  def returnBook(self, book):
        self.addBook(book)
        print(f"'{book}' has been returned. Thank you!")



# Example usage:
library = Library()
library.addBook("Harry Potter")
library.addBook("The Hobbit")
library.addBook("The Chronicles")
library.addBook("To Kill a Mockingbird")
library.addBook("1984")
library.addBook("The Great Gatsby")
library.addBook("The Catcher in the Rye")
library.addBook("Pride and Prejudice")
library.addBook("The Lord of the Rings")
library.addBook("The Hobbit")
library.addBook("Harry Potter and the Sorcerer’s Stone")
library.addBook("Harry Potter and the Chamber of Secrets")
library.addBook("Harry Potter and the Prisoner of Azkaban")
library.addBook("Harry Potter and the Goblet of Fire")
library.addBook("Harry Potter and the Order of the Phoenix")
library.addBook("Harry Potter and the Half-Blood Prince")
library.addBook("Harry Potter and the Deathly Hallows")
library.addBook("The Chronicles of Narnia: The Lion, the Witch, and the Wardrobe")
library.addBook("Animal Farm")
library.addBook("Jane Eyre")
library.addBook("Wuthering Heights")
library.addBook("Brave New World")
library.addBook("The Alchemist")
library.addBook("Little Women")
library.addBook("Gone with the Wind")
library.addBook("Moby Dick")
library.addBook("The Odyssey")
library.addBook("The Iliad")
library.addBook("The Kite Runner")
library.addBook("A Thousand Splendid Suns")
library.addBook("Memoirs of a Geisha")
library.addBook("The Book Thief")
library.addBook("Life of Pi")
library.addBook("The Fault in Our Stars")
library.addBook("The Hunger Games")
library.addBook("Catching Fire")
library.addBook("Mockingjay")
library.addBook("Divergent")
library.addBook("Insurgent")
library.addBook("Allegiant")
library.addBook("Percy Jackson and the Olympians: The Lightning Thief")
library.addBook("Percy Jackson and the Olympians: The Sea of Monsters")
library.addBook("Percy Jackson and the Olympians: The Titan's Curse")
library.addBook("Percy Jackson and the Olympians: The Battle of the Labyrinth")
library.addBook("Percy Jackson and the Olympians: The Last Olympian")
library.addBook("The Maze Runner")
library.addBook("The Scorch Trials")
library.addBook("The Death Cure")
library.addBook("The Giver")
library.addBook("The Outsiders")
library.addBook("Of Mice and Men")
library.addBook("Anne of Green Gables")
library.addBook("The Secret Garden")
library.showInfo()
library.searchBook("Harry")
library.removeBook("The Hobbit")
library.saveLibraryState()
library.loadLibraryState()


    
