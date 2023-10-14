def roman_to_int(s: str) -> int:
    """
    :param s: roman numerals
    :return: integer
    """
    dct = {"I": 1,
           "V": 5,
           "X": 10,
           "L": 50,
           "C": 100,
           "D": 500,
           "M": 1000}

    num = 0
    j = 0
    for i in range(0, len(s)):
        if j < len(s):
            if j + 1 < len(s) and dct[s[j]] < dct[s[j + 1]]:
                num = num + dct[s[j + 1]] - dct[s[j]]
                j += 2
            else:
                num += dct[s[j]]
                j += 1

    return num

