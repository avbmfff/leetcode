def is_palindrome(x: int) -> bool:
    """
    :param x: palindrome or not palindrome
    :return: true or false
    """

    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    reversed_x = 0
    x_copy = x

    while reversed_x < x:
        reversed_x = reversed_x * 10 + x_copy % 10
        print(reversed_x)
        x_copy //= 10

    if reversed_x == x:
        return True
    else:
        return False

print(is_palindrome(1001))