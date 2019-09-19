###Are you playing Banjo
def areYouPlayingBanjo(name):
    b = name.upper()
    if b[0] == 'R':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

