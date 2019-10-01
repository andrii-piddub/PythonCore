# No Yelling
def filter_words(st):
    '''function take string and transfer it (make new string - capitalized and properly spaced)'''
    d = st.split()
    New_string = ""
    for i in d:
        i = i.lower()
        New_string+=str(i) + " "
        New_string = New_string.capitalize()
    New_string = New_string[0:-1]
    return New_string
