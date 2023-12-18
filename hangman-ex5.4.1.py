def power(base, exponent):
    """This function calculates a number raised to a power.
    :param base: base value
    :param exponent: exponent value
    :type base: int
    :type exponent: int
    :return: The result of raising base to the power exponent
    :rtype: int
   """
    return base ** exponent


def main():
    help(power)
    num1 = int(input("Enter base number: "))
    num2 = int(input("Enter base exponent: "))
    print(power(num1, num2))


if __name__ == "__main__":
    main()
