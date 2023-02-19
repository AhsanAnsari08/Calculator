print("------Calculator-------")
x=float(input("Enter your First Number here: "))
y=float(input("Enter your Second Number here: "))
print(
"Enter 1 for 'Addition' \nEnter 2 for 'Subtraction' \nEnter 3 for 'Multiplication' \nEnter 4 for 'Division'"
)

num=int(input( "Enter Number for solving: "))

if num==1:
    print("Sum of your Number is: ",x + y)
      
elif num==2:
    print("Sub of your Number is: ",x - y)
    
elif num==3:
    print("prod of your Number is: ",x * y)
    
elif num==4:
    print("Division of your Number is: ",x / y)