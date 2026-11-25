# 14 - Longest Common Prefix (easy)
# Topics - Array, Strings, Trie

# Find the longest common prefix string amongst an array of strings, if there are nont return an empty string

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Currently I've only seen problems with hashing solutions so I am always thinking how can I use a hashtable, but I don't always have to think like that. I just need to ask myself, "does this problem need fast lookups for some sort of matching." Here I don't see that because we are sort of creating something.

# Alright let's think.
#
# The solution I did was have an index i and loop through every i++ and for every i++ we'd check every str in strs to see if the val at i equals curr. This was O(n^2)
#
# The sorting solution would be like:
# Sort the list. When strings are sorted lexiographically the first and last strings in the sorted order are the most different from each other. If these two extremes share a common prefix, then all strings in between must also share the same prefix. So we just need to compare the first and last strings after sorting. Sorting a list of strings would be n * m log m because sorting needs to check the strings to compare.

# This is what I did:


def a(strs):
    for string in strs:
        if len(string) == 0:
            return ""
    prefix = []
    i = 0
    while True:
        try:
            curr = strs[0][i]
        except IndexError:
            prefix_str = "".join(prefix)
            return prefix_str
        for string in strs:
            try:
                if string[i] != curr:
                    prefix_str = "".join(prefix)
                    return prefix_str
            except IndexError:
                prefix_str = "".join(prefix)
                return prefix_str
        i += 1
        prefix.append(curr)


# Attempt 2


def longestCommonPrefix(strs):
    """
    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    """
    prefix = ""
    p = 0
    while True:
        try:
            prefix = prefix + strs[0][p]
        except IndexError:
            return prefix
        for i in range(len(strs)):
            if strs[i][p] != prefix[p]:
                break
        p += 1
    return prefix[:-1]
