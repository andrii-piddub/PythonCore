#Fix the loop
def list_animals(animals):
    list = []
    my_String=""
    i=1
    for k in animals:
      k ='{}. {}\n'.format(i,k)
      list.append(k)
      i+=1
    my_String= "".join(list)
    return my_String