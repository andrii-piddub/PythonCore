"""Створити батьківський клас Figure з методами init: ініціалізується колір, 
get_color: повертає колір фігури, info: надає інформацію про фігуру та колір,  
від якого наслідуються такі класи як Rectangle, Square,
які мають інформацію про ширину, висоту фігури, метод square,
який знаходить площу фігури."""
class Figure:
    def __init__(self,color,no_of_sides):
        self.color = 'white'
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
        
    def get_side_and_color(self):
        self.color = input('Enter a color of figure ')
        self.sides = [float(input("Enter side ")) for i in range(self.n)]


    def info(self):
        return self.color,self.sides
class Rectangle(Figure):
    def __init__(self):
        Figure.__init__(self,'white',2)   

    def findArea(self):
        a,b=self.sides
        square = a*b
        print('The area of the rectangle is %0.2f' %square)
# b = Rectangle()
# b.get_side_and_color()
# print(b.info())
# b.findArea()
class Square(Figure):
    def __init__(self):
        Figure.__init__(self,'white',1)
    def findArea(self):
        a = self.sides
        square_1 = a[0]**2
        print('The area of square is ',square_1)
# c = Square()
# c.get_side_and_color()
# print(c.info())
# c.findArea()