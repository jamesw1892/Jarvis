def suffix(num: int) -> str:
    """
    Returns the suffix of a positive integer
    """

    tens, units = divmod(num, 10)
    tens %= 10

    if tens != 1:
        if units == 1:
            return "st"

        if units == 2:
            return "nd"

        if units == 3:
            return "rd"

    return "th"
