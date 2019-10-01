'''1.  Напишіть скрипт-гру, яка генерує випадковим чином число 
з діапазону чисел від 1 до 100 і пропонує користувачу вгадати це число.
Програма зчитує числа, які вводить користувач і видає користувачу підказки про 
те чи загадане число більше чи менше за введене користувачем. Гра має тривати
 до моменту поки користувач не введе число, яке загадане програмою, тоді друкує
 повідомлення привітання. (для виконання завдання необхідно імпортувати 
  модуль random, а з нього функцію randint())'''
# import random
# guess_number = random.randint(1,100)
# print(guess_number)
# def interesting_game():
#     while 1:
#         my_number = int(input('Please enter a number '))
#         if my_number>guess_number:
#             print('Your number is larger than secret number')
#         elif my_number<guess_number:
#             print('Your number is smaller than secret number')
#         else:
#             print('You win!!!')
#             break
# interesting_game()

#################################################
# '''2.  Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2. 
# (для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі).'''
# import math
# def rectangle():
#     '''Function calculate square of rectangle'''
#     a1 = float(input('Enter a number '))
#     a2 = float(input('Enter second number '))
#     print( 'Square of rectangle is', a1*a2)
#     return a1*a2
# def circle():
#     '''Function calculate square of circle'''
#     r = float(input('Enter a radius of circle '))
#     print('Square of circle is ', round(math.pi*math.pow(r,2),3))
#     return math.pi*math.pow(r,2)
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

