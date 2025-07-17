#
class car:
    def __init__(self,color):
        self.color=color
    def mycolor(self):
        print("mycolor",self.color)

my_car3=car("red")
print(my_car3.color)
my_car3.mycolor()
my_car4=car("blue")
my_car4.mycolor()

