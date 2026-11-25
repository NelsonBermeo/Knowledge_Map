"""
3 - Longest Substring Without Repeating Characters (medium)

Given:
string s
Find:
length of longest substring without duplicates characters
Ex:
Input: s = "bbcabcbb"
Output: 3
"""


def lengthOfLongestSubstring(s):
    l = 0
    r = 1
    res = 0
    while r < len(s):
        if s[l] == s[r]:
            l += 1
            r += 1
            res = 1
            continue
        longest = r - l
        if longest > res:
            res = longest
