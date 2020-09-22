def suffix(num: int) -> str:
    """
    Returns the suffix of an integer
    """

    num = abs(num)

    # Suffix only depends on last 2 digits
    tens, units = divmod(num, 10)
    tens %= 10

    # suffix is always 'th' unless the tens digit
    # is not 1 and the units is either 1, 2 or 3
    if tens != 1:
        if units == 1:
            return "st"

        if units == 2:
            return "nd"

        if units == 3:
            return "rd"

    return "th"
