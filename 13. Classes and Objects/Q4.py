"""
Q. Define a class Book to store book related information like bookid, title, price, author, publisher. 
Define functions to input show, change price.
"""

class Book:
    def __init__(self):
        self.bookid = int(input("Enter the bookid: "))
        self.title = input("Enter the title: ")
        self.amount = int(input("Enter the price: "))
        self.author = input("Enter the author: ")
        self.publisher = input("Enter the publisher: ")
        self.stock = int(input("Enter the stock:  "))
        
    def price(self):
        stock = int(input("Enter the quantity to be purchased: "))
        if self.stock >= stock:
            print("New stock of book: ", self.stock-stock)
            print("New price of book: ", self.amount+20)
        else:
            print("Book out of stock")
            

s = Book()
s.price()            
        
        