#Multiples of 3 or 5
def solution(number):
    ''' it returns the sum of all the multiples of 3 or 5 below the number passed in'''
    s = 0
    for i in range(1,number):
        if i%3==0 or i%5==0:
            s+=i
    return s