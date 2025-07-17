str_1="its a great oppurtinity ro meet you"
str_1=str_1.replace("ro","to")
print(str_1)
print(len(str_1))
print(str_1.capitalize())
print(str_1[6])

A=str_1.count("o")
print(A)
#conditional statements

age=int(input("what is your age?"))
if age >18:
    if age>=70:#nested , i added a condition with in a condition
        print("We are sorry, you are not eligible for driving")
    else:
        print("You are eligible of getting driving license")
elif age==18:
    print("you are young, you will get license after six months of your driving school experience ")
else:
    print("We are sorry you are to young")
    
#using if condition compiler checks and runs all conditions that have been made when true
#using elif compiler will execute only first conditon if it is true, it will not go to second condition even if true,
#because elif checks and jumps to second condition when first one is false.

#write a progrma whether a number is enev or odd
num=int(input("enter your number"))
if num%2==0:
    print("Your number",num,"is even")
else:
    print("number:",num,"is odd")