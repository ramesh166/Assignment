# # QUESTION 1


ip = {"Fiction", 1980}
books = [
    ("The Alchemist", "Fiction", 1988, 250),
    ("The Da Vinci Code", "Mystery", 2003, 300),
    ("A Brief History of Time", "Science", 1988, 150),
    ("The Theory of Everything", "Science", 2002, 100),
    ("Pride and Prejudice", "Fiction", 1813, 200),
    ("To Kill a Mockingbird", "Fiction", 1960, 180),
    ("The Catcher in the Rye", "Fiction", 1951, 220),
    ("Angels & Demons", "Mystery", 2000, 210),
    ("The Grand Design", "Science", 2010, 90),
    ("1984", "Fiction", 1949, 190)
]

def filter_book (genre, year):
    result = [ book[0] for book in books if book[1] == genre and book[2] >= year]
# # this will first iterate through index of books, i.e. books[0] = ("The Alchemist", "Fiction",1988,250),, after that 
# # then the iterate variable book goes through the all index index of books[0] i.e.. book = ["The Alchemist", "Fiction", 1988,250]
# # after that it will check the 1st index to be user inputed 'genre' and 3rd index to be either greater or equl to user inputed year
# # if the condition is matched it will store the 0th index of that items and move on to next index and if the condiction is not matched it will leave that particular index without storing the 0th index value and go to next index .
    print(result)
filter_book("Science", 1980)


# # QUESTION 2
def borrowing (genre = "Fiction"):
    output = {book[0]:book[3] for book in books if book[1] == genre }
    print(output)

borrowing()


#QUESTION 3
####sorted_books =


#QUESTION 4
  
def write_to_file(filename, content):
  a = open(filename, 'w')
  a.write(content)

def read_from_file(filename):
  b = open(filename, 'r')
  c = b.read()
  print(c)

write_to_file("greetings.txt", "Hello, Python!")
read_from_file("greetings.txt")