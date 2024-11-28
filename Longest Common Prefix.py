def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    min_length = 300

    for j in strs:
        if len(j) < min_length:
            min_length = len(j)

    for i in range(min_length - 1):
        common_str = strs[0][i]
        for k in strs:
            if k[i] == common_str:
                continue
            else:
                return strs[0][:i]