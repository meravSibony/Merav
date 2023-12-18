def fix_age(age):
    if age >= 13 and age <= 19 and age != 15 and age != 16:
        return 0
    else:
        return age


def filter_teens(a: int = 13,
                 b: int = 13,
                 c: int = 13):
    return fix_age(a) + fix_age(b) + fix_age(c)
