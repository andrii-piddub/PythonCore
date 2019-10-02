#Sorted my Textbooks
def sorter(textbooks):
    '''This function sorts list despite case sensitive'''
    return sorted(textbooks,key=lambda s:s.lower())
    