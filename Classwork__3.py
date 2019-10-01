# ### 1.Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел. 
# def average_number(*args):
#     '''This function find average number'''
#     sum_1 = 0
#     q = 0
#     for i in args:
#         sum_1+=i
#         q+=1
#     return int(sum_1/q)
# a = average_number(5,15,5,15)
# print(a)


######################################
# 2.Написати функцію, яка повертає абсолютне значення числа
# def absolute():
#     '''This function is looking for absolute value of a number'''
#     number = float(input('Please enter a number '))
#     if number>0:
#         return number
#     else:
#         return -number

# print(absolute())
    

########################################
#3.Написати функцію, яка знаходить максимальне число з двох чисел, а також в функції використати рядки документації DocStrings.
# def maximum(a1,a2):
#     """This function find the largest of two numbers"""
#     if a1>a2:
#         return a1
#     else:
#         return a2

# b=maximum(10,23)
# print(b)
# print(maximum.__doc__)

########################################
'''4.Написати програму, яка обчислює площу прямокутника, трикутника та кола 
(написати три функції для обчислення площі, і викликати їх в головній програмі
#  в залежності від вибору користувача)'''

# def rectangle():
#     '''Function calculate square of rectangle'''
#     a1 = float(input('Enter a number '))
#     a2 = float(input('Enter second number '))
#     print( 'Square of rectangle is', a1*a2)
#     return a1*a2
# def circle():
#     '''Function calculate square of circle'''
#     r = float(input('Enter a radius of circle '))
#     print('Square of circle is ', 3.14*r*r)
#     return 3.14*r*r
# def triagle():
#     '''Function claculate square of triagle'''
#     a = float(input('Enter length of side of triangle '))
#     h = float(input('Enter a height '))
#     print('Square of triangle is', 0.5*a*h)
#     return 0.5*a*h

# def main_function():
#     '''Main function to calculate square of different  figure'''
#     name = input('Please choose: rectangle, circle or triagle? ')
#     if name == 'rectangle':
#         rectangle()
#     elif name == 'circle':
#         circle()
#     elif name =='triagle':
#         triagle()

# main_function()
###################################
# 5.Написати функцію, яка обчислює суму цифр введеного числа.
# def sum_of_digits():
#     '''function will find a sum of all digits of number'''
#     number = input('Please enter a number ')
#     sum_1 = 0
#     for i in number:
#         i=int(i)
#         sum_1+=i
#     return sum_1
# print(sum_of_digits())
    



###################################

'''6.  Написати програму калькулятор, яка складається з наступних функцій: 

головної, яка пропонує вибрати дію та додаткових, які реалізовують вибрані дії, 
калькулятор працює доти, поки ми не виберемо дію вийти з калькулятора, 
після виходу, користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!'''
# def calculate():
#     '''Function operate with mathematical operations'''
#     operation = ""
#     while operation!='End':
#         operation = input("""Please choose operation : multiplication, division, addition, subtraction (if you want go out from from please input 'End') """)
#         if operation == 'multiplication':
#             multiplication()
#         elif operation == 'division':
#             division()
#         elif operation == 'addition':
#             addition()
#         elif operation == 'subtraction':
#             subtraction()
#         else:
#             print('Please choose correctly')
#     print('Thank you user!!!')
# def multiplication():
#     '''function make multiplication of 2 numbers'''
#     a1 = float(input('Please enter first multiplier ' ))
#     a2 = float(input('Please enter second multiplier '))
#     Result_1 = a1*a2
#     print('Result is ',Result_1)
# def division():
#     '''function make division of 2 numbers'''
#     a1 = float(input('Please enter divided number ' ))
#     a2 = float(input('Please enter divider number '))
#     Result_2 = a1/a2
#     print('Result is ', Result_2)
# def addition():
#     '''function add one number to another'''
#     a1 = float(input('Please enter addition number ' ))
#     a2 = float(input('Please enter addition number '))
#     Result_3 = a1+a2
#     print('Result is ', Result_3)
# def subtraction():
#     '''function find subtraction of 2 numbers'''
#     a1 = float(input('Please enter decreasing number ' ))
#     a2 = float(input('Please enter subtrahend number '))
#     Result_4 = a1-a2
#     print('Result is ', Result_4)
    
# calculate()
