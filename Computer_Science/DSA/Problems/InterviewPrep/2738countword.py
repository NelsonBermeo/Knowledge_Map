# 2738 (premium) Count Word Occurences in Text

# Problem Desc:
# Delivers text in chunks instead of one complete string
# Given an iterable stream of text chunks and list of requested words

# stream ["text", "text", "text"]
# list of requested words, count how many time each requested word appears

# Notes: matching is case insenstive
# Two Problems:
# - our chunks have punctuation in them -
# - a words list can have case insensitive duplicates - handled

# import string


# def count_stream_words(chunks, words):
#     dic = {}

#     for i in range(len(words)):
#         if dic.get(words[i].lower()) is None:
#             dic[words[i]] = 0
#     for i in range(len(chunks)):
#         # we have to go through all the chunks
#         # for each chunk well have to check every word
#         # assuming no punc in these chunks
#         # we break the string up into all the words (seperated by spaces)
#         cleaned_chunk = []
#         for k in range(len(chunks[i])):
#             if chunks[i][k] not in string.punctuation:
#                 cleaned_chunk.append(chunks[i][k])
#         cleaned_chunk_str = "".join(cleaned_chunk)
#         chunk_ls = cleaned_chunk_str.split()
#         for j in range(len(chunk_ls)):
#             # instead of looping through and finding words we'll query them from the dictionary
#             if dic.get(chunk_ls[j].lower()) is not None:
#                 dic[chunk_ls[j].lower()] += 1
#     return dic


# print(
#     count_stream_words(
#         ["the boy! has the bag", "chicken crossed the road", "the girl has the bag"],
#         ["boy", "bag", "muffin"],
#     )
# )


# Attempt 2 ->

# Desc:
# Text may come in chunks rather than one complete string

# Given:
# ls of strings
# ls of requested words
#
# Count the number of times each requested word appears

# Notes:
# Matching is case-insensitive -> aa = AA
# Words can start in one chunk and end in another, the are only seperated by spaces or non-letter chars: ["nel", "son"] -> means that "nelson" was inputted
# Only ascii letters (no numbers nothing else)
# We cannot concatenate the entire stream before processing

"""
Ex:
{ words:
    ["pikachu", "met", "eevee"],
  chunks:
    ["Pikachu met pi", "kachu. Pikachu!"]
}

buffer = [pikachu], check if in acccepted_words, then add then clear buffer -> []

out = {
    "pickachu" : 1
    "met" : 1
    "eevee" : 0
}
"""

# import string


# def count_stream_words(chunks, words):
#     # out = {}

#     # Optimal querying with words_dictionary
#     words_dic = {}
#     for i in range(len(words)):
#         if words_dic.get(words[i].lower()) is None:
#             words_dic[words[i].lower()] = 0

#     # Process the chunks
#     buffer = []
#     for i in range(len(chunks)):
#         # buffer = None
#         # if i == 0:
#         #     buffer = []

#         # For every chunk we process a string
#         # We want to sperate on all non-letter chars
#         # contains all the words, so then I can go through this list and check if they are accepted words
#         cleaned_ls = []
#         # Our chunk: "Pikachu met!pi"
#         # cleaned: "Pikachu met pi"
#         for j in range(len(chunks[i])):
#             if chunks[i][j].lower() in string.ascii_lowercase:
#                 cleaned_ls.append(chunks[i][j].lower())
#             else:
#                 cleaned_ls.append(" ")
#         cleaned_str = "".join(cleaned_ls)
#         if cleaned_ls.strip() == "":
#             continue
#         cleaned_split_str_ls = cleaned_str.split()
#         if i != 0:
#             for x in range(len(cleaned_split_str_ls[0])):
#                 buffer.append(cleaned_split_str_ls[0][x])

#             buffer_wrd = "".join(buffer)
#             if words_dic.get(buffer_wrd) is not None:
#                 words_dic[buffer_wrd] += 1

#         for k in range(len(cleaned_split_str_ls)):
#             if words_dic.get(cleaned_split_str_ls[k]) is not None:
#                 words_dic[cleaned_split_str_ls[k]] += 1
#         # now let us full up our buffer
#         buffer = []
#         for x in range(len(cleaned_split_str_ls[-1])):
#             buffer.append(cleaned_split_str_ls[-1][x])

#     return words_dic


# print(
#     count_stream_words(
#         ["Pikachu met pi", "kachu. Pikachu!"],
#         ["pikachu", "met", "eevee"],
#     )
# )
import string


def count_stream_words(chunks, words):
    out = {}
    for i in range(len(words)):
        if out.get(words[i].lower()) is None:
            out[words[i].lower()] = 0
    buffer = ""
    for i in range(len(chunks)):
        for j in range(len(chunks[i])):
            if chunks[i][j].lower() in string.ascii_lowercase:
                buffer = buffer + chunks[i][j].lower()
            else:
                if out.get(buffer) is not None:
                    out[buffer] += 1
                buffer = ""
    if out.get(buffer) is not None:
        out[buffer] += 1
    return out


print(
    count_stream_words(
        ["ca", "t ca", "t catalog"],
        ["cat", "catalog"],
    )
)
