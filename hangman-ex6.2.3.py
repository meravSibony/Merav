def format_list(my_list):
    """Chains all even elements of a list-of-strings into one string.
        Elements in the list are separated by ",". The last element will be added
        after the even element, with "and" between them.
        :param my_list: an even-length list of strings.
        :type my_list: list
        :return: the new chained string.
        :rtype: string.
    """
    return ', '.join(my_list[:-1:2]) + ', and ' + my_list[-1]