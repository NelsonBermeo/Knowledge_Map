# 125 - Valid Palindrome (easy)

# Given a phrase/word return if it is a palindrome
# It is a palnindrome if after converting all uppercase to lowercase and remove non alphabetalic chars it reads the same forward and backword

# Space Complexity O(n) with s_lower and ls_alpha
# Time Complexity O(n) with 2 for loops


def palindrome(s):
    s_lower = s.lower()
    ls_alpha = []
    for i in range(len(s_lower)):
        code = ord(s_lower[i])
        if code >= 97 and code <= 122:
            ls_alpha.append(s_lower[i])
        if code >= 48 and code <= 57:
            ls_alpha.append(s_lower[i])
    s_alpha = "".join(ls_alpha)
    i = 0
    j = len(s_alpha) - 1
    while i < j:
        if s_alpha[i] != s_alpha[j]:
            return False
        i += 1
        j -= 1
    return True


print(palindrome("A man, a plan, a canal: Panama"))
