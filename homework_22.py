#Grasshopper - Summation
def summation(num):
    '''this function finds the summation of every number from 1 to num'''
    sum = 0
    for i in range(1,num+1):
        sum+=i
    return sum