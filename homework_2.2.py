"""2.Задано чотирицифрове натуральне число.
	Знайти добуток цифр цього числа.
	Записати число в реверсному порядку
	Посортувати цифри, що входять в дане число
"""
number1 = 7891
number1 = str(number1)
n1 = int(number1[0])
n2 = int(number1[1])
n3 = int(number1[2])
n4 = int(number1[3])
print('Multiplication of all digits', n1*n2*n3*n4)


#Another way to find multiplication
mult = 1
for i in number1:
	i = int(i)
	mult*=i
print('Multiplication of all digits', mult)


print('This number but in reverse', int(number1[::-1]))

list_of_digit = [n1,n2,n3,n4]
list_of_digit.sort()
print('This is sorted list of digits',list_of_digit)