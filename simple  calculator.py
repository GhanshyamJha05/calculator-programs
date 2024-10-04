def addition(num1,num2):
    print("Addition=",num1+num2)

def subtraction(num1,num2):
    print("Subtraction=",num1-num2)

def multiplication(num1,num2):
    print("Multiplication=",num1*num2)

def division(num1,num2):
    print("Division=",num1/num2)

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")    
    print("5. Exit")
    choice=int(input("Enter your choice(1-5):"))

    if choice==1:
        num1=int(input("Enter 1st Number:"))
        num2=int(input("Enter 2nd Number:"))
        addition(num1,num2)


    elif choice==2:
        num1=int(input("Enter 1st Number:"))
        num2=int(input("Enter 2nd Number:"))
        subtraction(num1,num2)
    
    elif choice==3:
        num1=int(input("Enter 1st Number:"))
        num2=int(input("Enter 2nd Number:"))
        multiplication(num1,num2)
    
    elif choice==4:
        num1=int(input("Enter 1st Number:"))
        num2=int(input("Enter 2nd Number:"))
        if num2 == 0:
            print('Infinity')
        else:
            division(num1,num2)
                
    elif choice==5:
        print("exit")
        break
    else:
        print("Wrong Choice")
