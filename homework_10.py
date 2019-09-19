#Will there be enough space?
def enough(cap, on, wait):
    return max(0, on+wait-cap)