# Stacks

# 682. Baseball Game

# We are given a list of strings called operations and the ith operation must be applied to the record
# x records a new score of x
# + records a new score that is the sum of the prev 2
# D records a new score that is double of the prev
# C invalidates the prev score
# Return the sum of all the score on the record
# How does everything fitting in a 32 bit int effect this problem?

# Example:
# Input: ["5","2","C","D","+"]
#

# Runtime here should be O(n) we just loop through and all stack operations are O(1) and the space complexity is O(n) since we used a stack


def calPoints(ops):
    stack = []
    for i in range(len(ops)):
        if ops[i] != "C" and ops[i] != "+" and ops[i] != "D":
            stack.append(int(ops[i]))
        if ops[i] == "C":
            stack.pop()
        if ops[i] == "D":
            stack.append(stack[-1] * 2)
        if ops[i] == "+":
            stack.append(stack[-1] + stack[-2])

    return sum(stack)


print(calPoints(["5", "2", "C", "D", "+"]))
