# Student Marks analyzer
# Ask User For Number for Subjects.
subjects=int(input("Enter The Number Of Subjects You Have Given Exam:"))
i=0
sum=0
dict={}
list=[]
fail_list=[]
# Ask Name and Marks for each subject
while(i<subjects):
    name=input("Enter The Name Of Subject:")
    marks=int(input(f"Enter The Marks Of {name}:"))
    if(marks<40):
        print(f"You Are Fail In {name}")
        fail_list.append(name)
# Store Marks and Subjects In Dictionary.
    dict[name]=marks
    sum+=marks
    list.append(marks)
    i+=1
print("Final Dictionary")
print(dict)
# Total Of Marks
print("Sum Of All Numbers Are:", sum)
# Average Of Marks
average=(sum/subjects)
print("Average Of Marks Are:",average)
list.sort()
print("The Highest Marks Of Subject Is:",list[-1])
print("You Failed In:")
print(fail_list)

a=input("Plese press enter to exit")