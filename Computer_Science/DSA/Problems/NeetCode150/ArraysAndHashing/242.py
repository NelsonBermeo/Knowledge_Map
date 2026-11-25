# 242 - Valid Anagram (easy)
# Topics - Hashing, String, Sorting

# Given two strings s and t return true if t is an anagram of s and false otherwise. I believe an anagram is another word that can be made with the same chars as another

# s = "anagram", t = "ngaram" -> false

# You couldn't really double loop for this because you could count a char twice in the 2nd string by accident

# Solution 1: Sorting & Comparing
# We could sort each string and then loop through them and see if they are the same
# Time - O(nlog(n)) because sorting
# Space - O(1) unless sorting uses a linear data structure

# Solution 2: HashMap
# We could loop through each word and make a seperate hashmap for each and compare the hashmaps.
# Time - O(n) because we have to loop through the strings
# Space - O(n) because we have those maps in storage now


def a(s, t):
    s_map = {}
    t_map = {}
    for i in s:
        if s_map.get(i) == None:
            s_map[i] = 1
        else:
            s_map[i] += 1
    for i in t:
        if t_map.get(i) == None:
            t_map[i] = 1
        else:
            t_map[i] += 1
    if t_map == s_map:
        return True
    return False


print(a("anagram", "ngaram"))

# Attempt 2 ->

# Given 2 strings s and t return true if they are anagrams of eachother and false otherwise.
# brute force would be hard here because if for every value in s you search for the same val in t you could accidently return true but this could not be good for copies of that character
# sort both and check if they are equal -> O(nlog(n))
# put both in hashmap and check if they are equal -> O(n)


def valid_anagram(s, t):
    s_map = {}
    t_map = {}
    for i in range(len(s)):
        if s_map.get(s[i]) is None:
            s_map[s[i]] = 1
        else:
            s_map[s[i]] += 1
    for j in range(len(t)):
        if t_map.get(t[j]) is None:
            t_map[t[j]] = 1
        else:
            t_map[t[j]] += 1
    return s_map == t_map
