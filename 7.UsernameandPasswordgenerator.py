# Project 1
# Username Generator System.
name=input("Enter Your Full Name:").lower()
year=int(input("Enter Your Birth Year:"))
new=name.split()
first_name=new[0]
surname=new[1]
print("According To Your Name 3 Username Are Available:")
# UserName 1
username=first_name[0:3]
username1=surname[-4:]
year1=str(year)
year2=year1[-2:]
a=username+username1+year2
print("Username 1 Wiil be:", a)
# Username 2
username2=first_name[0:]
year3=year1[0:]
b=username2+year3
print("Username 2 Will Be:", b)
# Username 3
username3=first_name[0]
username4=surname[0:]
year4=year1[-3:]
c=username3+username4+year4
print("Username 3 Will Be:", c)
# Project 2
password=input("Enter Your Password:")
has_upper=any(c.isupper() for c in password)
has_lower=any(c.islower() for c in password)
has_digit=any(c.isdigit() for c in password)
special_char=("@","#","$","%","&","*")
has_special=any(c in special_char for c in password)
if(len(password)>=8 and has_lower and has_digit and has_upper and has_special):
    print("Your Password Is Strong.")
elif(len(password)<=6 and has_special):
    print("Your Password Is Medium.")
else:
    print("Your Password Is Weak.")
    
a=input("Plese press enter to exit")