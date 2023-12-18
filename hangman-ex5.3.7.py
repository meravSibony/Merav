def chocolate_maker(small, big, x):
    if big !=0:
        num = x // (big * 5)
        if num == 0:
            return True
        x = x - big * 5
    if x == small:
        return True
    else:
        return False
