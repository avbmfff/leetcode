def is_palindrome(x: int) -> bool:
    """
    :param x: palindrome or not palindrome
    :return: true or false
    """

    y = str(x)

    for i in range(0, len(y) - 1 // 2):
        if y[i] != y[len(y) - 1 - i]:
            return False

    return True
