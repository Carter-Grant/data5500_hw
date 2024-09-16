
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

my_rectangle= Rectangle(5,3)   
print(my_rectangle.area())

#Q:Create a class called Rectangle with attributes length and width. Implement a method within the class to calculate the area of the rectangle. Instantiate an object of the Rectangle class with length = 5 and width = 3, and print its area. what is wrong with my area code here? code:
#class rectangle(self,length,width):
#def area(self):
#return length * width