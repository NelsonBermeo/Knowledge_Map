# Event Statistics Aggregator - Wells Fargo - Medium
# https://www.fastprep.io/problems/wellsfargo-event-statistics-aggregator

# Process a finite sequence of operations for an event-statistics aggregator. Each event name keeps its count, sum, min, and max

# Every operation is a string array

# A formatted dict lists event names in ascending lexicographic order as name:value pairs separated by one space

# Ex:
"""
operations = [
    ["count"],
    ["avg"],
    ["add","click","2"],
    ["add","purchase","10"],
    ["add","click","4"],
    ["count"],
    ["avg"],
    ["min"],
    ["max"]
]

We can think of this as 9 commands our programming executes one at a time from top to bottom

return = [
    "0",
    "",
    "3",
    "click:3.000000 purchase:10.000000",
    "click:2.000000 purchase:10.000000",
    "click:4.000000 purchase:10.000000"
]


"""


def aggregateEventStats(operations):
    return
