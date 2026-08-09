# ATM Machine Project....
balance=0
name=input("Enter Your Name:")
paisa=[0]
history=[]
balance5=[]
def atm():
    
    countinue=True
    while(countinue):
        opt=input("What Do You Want?\n(WithDraw/Deposit/Check Balance/Exit)").capitalize()

        if(opt=="Deposit"):
            def deposit():
                amount1=int(input("Enter Amount You Wanna Deposit:"))
                print("Amount Deposited Succesfully.")
                balance1=balance+amount1
                print("Your Current Balance Is:", balance1)
                paisa.append(balance1)
                history.append(f"Your Account Has deposited: {balance1-amount1}")
                balance5.append(balance1)
            deposit()
            break
        elif(opt=="Withdraw"):
            def withdraw():
                amount=int(input("Enter Amount You Wanna Withdraw:"))
                if(amount>balance5[0]):
                    print("insufficent Balance.")
                else:
                    print("Amount Witdraw Succesfully.")
                    balance2=balance-amount
                    print("Your Current Balance Is:", balance5[0]-amount)
                    paisa.append(balance2)
                    history.append(f"Your Account Has Withdrawn:{balance2}")
            withdraw()
            break
        elif(opt=="Balance"):
            def check_balance():
                print("Your Current Balance Is:", balance5)
            check_balance()
            break
        if(opt=="Exit"):
            def exit():
                print("Exit Succsesfully.")
            exit()
            break
    countinue=input("Do You Wanna Countinue(Yes/No):").capitalize()
    if(countinue=="Yes"):
        print("Total Money Is:", paisa)
        atm()
    else:
        print("Thanks For Visiting ATM.....")
atm()

a=input("Plese press enter to exit")