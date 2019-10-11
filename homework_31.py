###CLassy Clases
class Person:
    def __init__(self,name,age):
        self.info= "%ss age is %d" %(name,age)
    def show(self):
        print(self.info)