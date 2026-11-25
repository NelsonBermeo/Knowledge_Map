def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    # 1 1 1 - if our right most value is any value below 9 then we just simply add 1 to that end are done.
    # 1 1 9 - if our right most value is 9 then we have to turn that into a 0 and then add a value to the next
    # 9 9 9 - if we have a cascading effect we should perhaps have a flag that can be used to see if we need to carry over

    if digits[-1] < 9:
        digits[-1] += 1
        return digits

    j = len(digits) - 1
    while j > 0:
        digits[j] = 0
        if digits[j - 1] < 9:
            digits[j - 1] += 1
            return digits
        else:
            j += 1
    out = [1] + digits
    return out


print(plusOne([9, 9]))
