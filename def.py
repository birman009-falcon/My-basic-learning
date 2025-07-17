
print("Welcome to python simple calculator")
print("Please use lower case letters.")
print("List: addition,multiplication,subtraction,division,power")
list_1=["addition","multiplication","subtraction","division","power"]
while True:
     A=input("what operation you want to perform?\nchoose from the above list below,or enter exit: ")
     if A=="exit":
        print("Goodbye,thanks for using the calculator.")
        break
    
     elif A not in list_1:
        print("Invalid syntax, please re-enter your values ",end=" ")
        print()
        continue

 
     c=float(input("enter your first number: "))
     d=float(input("enter your second number: "))
     print(A)

     if A=="addition":
        print(c,"+",d,end="")
        print("=",c+d)

     elif A=="multiplication":
        print(c,"*",d,end="")
        print("=",c*d)

     elif A=="subtraction":
        print(c,"-",d,end="")
        print("=",c-d)

     elif A=="division":
         print(c,"/",d,end="")
         print("=",c/d)
     elif A=="power":
        print(c,"**",d,"=",end="")
        print(c**d)




