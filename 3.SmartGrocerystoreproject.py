# Smart Grocery Store Management.....
name=input("Enter Your Name:")
print(f"Hello {name} Welcome To My Store.")
fruits={
    "Mango":99,
    "Apple":50 ,
    "Banana":80 ,
    "Grapes":70 ,
    "Orange":60 ,
}
vegetables={
    "Potato":90,
    "Tomato":80,
    "Cucumber":70,
    "Carrot":60
}
cart=[]
total_bill=0
while True:
    choice=input("What Do You Wanna Buy(Vegetables/Fruits):").capitalize()
    if(choice=="Vegetables"):
        print(vegetables)
    elif(choice=="Fruits"):
        print(fruits)
    else:
        print("Sorry! Invalid Choice.")
        break
    item=input("Enter Item You Wanna Buy:").capitalize()
    if(item in fruits):
        cart.append(item)
        print("Your Item Added To Cart Successfully.")
        total_bill+=fruits[item]
        print("Your Total Bill Is:", total_bill)
    elif(item in vegetables):
        cart.append(item)
        print("Your Item Added To Cart Successfully.")
        total_bill=total_bill+vegetables[item]
        print("Your Total Bill Is:", total_bill)
    else:
        print("Sorry This Item In Our Store.")
    again=input("Do You Wanna Buy More Items(Yes/No):").capitalize()
    if(again=="Yes"):
        pass

    else:
        print("Thanks For Shaopping.")
        print("Your Bill Is Here...")
        print("Items:", cart)
        print("Total Bill:", total_bill)
        break
a=input("Plese press enter to exit")