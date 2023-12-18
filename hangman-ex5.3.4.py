def last_early(my_str):
    my_str = my_str.lower()
    if (my_str.find(my_str[-1], 0, len(my_str)-1)) == -1:
        return False
    else:
        return True


#last_early("happy birthday")
#last_early("best of luck")
#last_early("Wow")
#last_early("X")

