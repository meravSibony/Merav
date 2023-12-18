def extend_list_x(list_x, list_y):
    """CThe function receives two lists list_y, list_x. The function expands list_x (modifies) so that
        it also contains list_y, and returns list_x itself.
        :param list_x: the end of the desire string.
        :param list_y: the start of the desire string.
        :type list_x: list
        :type list_y: list
        :return: the new chained string.
        :rtype: string.
    """
    list_y.extend(list_x)
    return list_y
