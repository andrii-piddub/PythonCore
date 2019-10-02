#Double Char
def double_char(a):
  mystring=""
  list_1= []
  for i in a:
    i*=2
    list_1.append(i)
  mystring="".join(list_1)
  return mystring
