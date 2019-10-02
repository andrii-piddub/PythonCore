# def is_uppercase(inp):
#     '''Check every letter in string by uppercase'''
#     return inp.isupper()
# a= is_uppercase('FFF')
# print(a)

# def shorten_to_date(long_date):
#         b = long_date.split(',')
#         return b[0]
        
# def sorter(textbooks):
#     b = []
#     for i in textbooks:
#         b.append[i.lower()]
#     print(b)
a = ['Am','Pd','BS','aa','Ab','45']
b = sorted(a,key=lambda s:s.lower())
print(b)