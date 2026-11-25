# 206 Reverse Linked List (easy)

# Given head reverse the list


def reverse_ls(head):

    ls = []
    curr = head
    while curr is not None:
        ls.append(curr.val)
        curr = curr.next

    i = 0
    j = len(ls) - 1
    while i <= j:
        a = ls[i]
        ls[i] = ls[j]
        ls[j] = a
        i += 1
        j -= 1
    k = 0
    curr = head
    while curr is not None:
        curr.val = ls[k]
        k += 1
        curr = curr.next

    return head


def reverse(ls):
    i = 0
    j = len(ls) - 1
    while i <= j:
        a = ls[i]
        ls[i] = ls[j]
        ls[j] = a
        i += 1
        j -= 1
    return ls


print(reverse([1, 2, 3, 4, 5]))
