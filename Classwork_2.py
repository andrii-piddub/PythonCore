"""
 Створити список цілих чисел, які вводяться з терміналу
 та визначити серед них максимальне та мінімальне число.
 """

a = input('Please enter all numbers, but separete them by ",": ')
a = a.split(',')
b =[int(i) for i in a]
print('The largest number is',max(b),'and the smallest number is',min(b))

################################################
"""
2.  В інтервалі від 1 до 10 визначити числа 
•  парні, які діляться на 2,
•  непарні, які діляться на 3, 
•  числа, які не діляться на 2 та 3.
"""
a =[i for i in range(1,11) if i%2 == 0]
print(a)
b = [i for i in range(1,11) if i%3 == 0]
print(b)
c = [i for i in range (1,11) if i%2 != 0  and i%3 != 0]
print(c)

#####################################################
"""
3.3.  Написати програму, яка обчислює факторіал
 числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)
"""
a =int(input('Please enter a number '))
factorial = 1
for i in range(1,a+1):
    factorial = factorial*i
print(factorial)

##########################################################

"""
4.  Напишіть скрипт, який перевіряє логін, який вводить користувач. 
Якщо логін вірний (First), то привітайте користувача. 
Якщо ні, то виведіть повідомлення про помилку. 
(використайте цикл while)
"""
login_1 = 'First'
login_2 = ""
while login_1!=login_2:
    login_2 = input('Please enter your login ')
    if login_1 != login_2:
        print('Dear visitor you enter wrong login')
print('Welcome dear USER')
