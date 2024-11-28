def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    x = str(x)
    if x[::-1] == x:
        return True
    else:
        return False