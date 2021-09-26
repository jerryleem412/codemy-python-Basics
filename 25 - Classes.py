import os
#os.system('cls')


class Square:
    #Functions in a class is called a method
    def __init__(self, side_length):
         self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

    def parimeter(self):
        return self.side_length * 4

    def report(self):
        print("Side Length: %s" % self.side_length)
        print("Area: %s" % self.area())
        print("Parimeter %s" % self.parimeter())


my_square = Square(10)
my_square.report()

#print(my_square.area())