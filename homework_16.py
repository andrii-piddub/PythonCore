# 21 sticks
def make_move(sticks):
    '''function Create a robot that will always win the game, this robot will always go first.
     The function  take an integer and returns 1, 2, or 3'''
    return max(sticks%4, 1)

