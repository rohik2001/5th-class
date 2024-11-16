'''name=input("Enter batch student name")
if name.tolower()=="rohik":
    print("Hello Rohik")
else:
    print("you are unknown person")'''


'''age=int(input("Enter age: "))
if age<18:
    print("You are a kid")
elif age>=18 and age<=60:
    print("You are adult")
else:
    print("You are a Senior citizen")
## eligibility check 
age=int(input("Enter age: "))
citizen=input("Are you a citizen? (yes/no)").lower()
if age>=18 and citizen=="yes":
        print("you are elligible to vote")
else:
    print("you are not elligible to vote")

## Nested condition
##Positive/Nagetive and odd Even
x=int(input("Enter a number"))
if x>0:
    if x%2==0:
          print("Positive and Even Number")
    else:
          print("positive and odd Number")
elif x<0:
     print("Negative number")
else:
     print("zero")

#Using Logical Operator
weather=input("whats the weather like? (sunny/rainy/cold): ").lower()
if weather=="sunny":
     print("wear sunglases and drink water")
elif weather=="rainy":
     print("take Umbrella")
elif weather=="cold":
     print("wear jacket and i hate cold too much!!!")
else:
     print("may be its spring") 

actual_cost = float(input(" Please Enter the Actual Product Price: "))
sale_amount= float(input(" Please Enter the Sales Amount: "))
if (sale_amount > actual_cost):
     amount = sale_amount - actual_cost
     print("Total Profit = {0}".format(amount))
else:
     print("No Profit!!!")

#lerger number check
a=int(input("Enter the value1: "))
b=int(input("Enter the value2: "))
c=int(input("Enter the value3: "))
if a>b and a>c:
     print("a larger")
elif b>a and b>c:
     print("b larger")
else:
     print("c larger")'''

#password and user name check
username=input("Enter username: ").lower()
passowrd=input("Enter password: ").lower() 
if username== "admin" and passowrd=="12345":
    print("Login successful")
else:
    print("Invalid username or passowrd")
