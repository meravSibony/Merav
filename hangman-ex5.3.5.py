def distance(num1, num2, num3):
    if abs(num1 - num2) != 1 and abs(num1 - num3) != 1:
        return False
    if abs(num2 - num1) >= 2 and abs(num2 - num3) >= 2:
        return True
    if abs(num3 - num1) >= 2 and abs(num3 - num2) >= 2:
        return True
    else:
        return False
