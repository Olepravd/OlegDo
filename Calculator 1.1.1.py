#WOC Calculator
#Version 1.1.1
#OlegDo AB
#2024

print("WOC Calculator")
print("Version: 1.1.2")
print("OlegDo AB")
print("2024")
print("")

while True:
    print ("Watch the operations")
    print ("1-Sum")
    print ("2-Subtraction")
    print ("3-Multiplication")
    print ("4-Division")
    print ("5-Finish")

    choise=input("Write the number of the operation")
    if choise in ('1','2','3','4'):
    
        a=float(input("Write the first number"))
        b=float(input("Write the second number"))
        if choise=='1':
          print("Sum is",a+b)
        elif choise=='2':
          print("Subtraction is",a-b)
        elif choise=='3':
          print("Multiplication is",a*b)
        elif choise=='4':
          print("Division is",a/b)

    
    elif choise =='5':
        break
    elif choise != ('1','2','3','4'):
         print("Error I01")
         print("The information isn't correct.")
         print("Write right information")

    



