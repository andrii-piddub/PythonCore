"""3. Поміняти між собою значення 2 змінних, не використовуючи третьої змінної"""
a = 125
b = False
print('a =',a,'b = ',b)
a,b = b,a 
print('a = ',a,'b = ',b)

#Another way to do this
c  = 345
d = 'some_text'
print('c = ',c,'d =',d)
c = [c]
c.append(d)
d = c[0]
c = c[1]
print('c =',c, 'd = ',d)
