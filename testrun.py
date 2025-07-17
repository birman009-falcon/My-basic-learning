print("Welcome to python simple calculator")
A=input("what operation you want to achieve?")
c=int(input("enter your first number"))
d=int(input("enter your second number"))
print(A)
list=["addition","multiplication","subtraction","division"]
i=0
while i<len(list):
    print(list[i])
    i+=1
    if list=="addition":
        print(c,"+",d,end="")
        print("=",c+d)
        i+=1
        break
 
    if list=="multiplication":
        print(c,"*",d,end="")
        print("=",c*d)

    if list=="subtraction":
        print(c,"-",d,end="")
        print("=",c-d)

    if list=="division":
        print(c,"/",d,end="")
        print("=",c/d)
