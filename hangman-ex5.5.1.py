def is_valid_input(letter_guessed):
    """This function check if character is valid.
    :param letter_guessed: guess character
    :type letter_guessed: string
    :return: Whether the function parameter is correct or not
    :rtype: bool
    """
    return len(letter_guessed) == 1 and (letter_guessed.isalpha())
 