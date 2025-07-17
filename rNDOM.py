number=int(input("Enter a positive integer"))
while number<=0:
    print("Please enter a positive integer.")
    number=int(input("Enter a positive integer"))
    
print("countdown")
while number<=1:
    print(number)
    number-=1


    number=int(input("guess a number"))
secret_number=5
while number!=secret_number:
    print("wow you are a fool!")
    number=int(input("guess a number"))
    print("you won the game")    


for i in range(5):
     for i in range(5):
        print("hi")
