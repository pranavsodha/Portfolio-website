# Smart Library Project
name=input("Enter Your Name:").capitalize()
print(f"Hello {name} Welcome To Library...")
history_books={
    "Mughal": 100,
    "Shivaji": 500,
    "British Empire": 150,
}
science_books={
    "Gravity":100,
    "Einstein":800,
    "APJ Abdul Kalam":200,
}
book=[]
total_bill=0
while True:
    books=input(f"Which Type Of Books You Wanna Read {name}(History/Science):").capitalize()
    if(books=="History"):
        print(history_books)
        item=input("Choose Books From Above:").capitalize()
        print(f"Price Of Your Book {item} Will Be {history_books[item]}")
        total_bill+=history_books[item]
        print("Thanks For Shopping.")
        book.append(item)
    elif(books=="Science"):
        print(science_books)
        item=input("Choose Books From Above:").capitalize()
        print(f"Price Of Your Book {item} Will Be {science_books[item]}")
        total_bill+=science_books[item]
        print("Thanks For Shopping.")
        book.append(item)
    else:
        print("Sorry Invalid Input...")
        break
    again=input("Do You Wanna Add More Books(Yes/No):").capitalize()
    if(again=="Yes"):
        pass


    else:
        print("Your Total Bill Is:", total_bill)
        print("You Have Purchased Books:", book)
        print("Thanks For Shopping.....")
        break
a=input("Plese press enter to exit")