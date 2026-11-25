# Task:
# Count the number of occurances in a string:

# Ex:
# Input: "the, boy has the bag"
# Output:
# {the: 1, boy: 1, ...}

import string


def countWords(str):
    ls_nopunc = []
    for i in range(len(string)):
        # should not effect time complexity since we searching through a constant list
        if ls_nopunc not in string.punctuation:
            ls_nopunc.append(string[i])
    string_punc = "".join(ls_nopunc)
    dic = {}
    ls = string_punc.split()
    for i in range(len(ls)):
        if dic.get(ls[i]) is None:
            dic[ls[i]] = 1
        else:
            dic[ls[i]] += 1
    for key, value in dic.items():
        print(f"Word: {key}, Count: {value}")
    return
