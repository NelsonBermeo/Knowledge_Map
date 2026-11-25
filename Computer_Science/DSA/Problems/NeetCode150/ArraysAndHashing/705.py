# 705 - Design HashSet (easy)

# Topics: Array, Hash Table, Linked List, Design, Hash Function

# Design a HashSet without using any built in hash table libraries.
# The class should have:
# void add(key)
# bool contains(key)
# void remove(key)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


class MyHashSet:
    def __init__(self):
        self.ls = [0] * 10000

    def add(self, key):
        if self.contains(key) is True:
            return
        hashVal = key % 10000
        if self.ls[hashVal] == 0:
            self.ls[hashVal] = LinkedList()
            self.ls[hashVal].head = Node(key)
        else:  # It would have a value
            curr = self.ls[hashVal].head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(key)
        return

    def contains(self, key):
        hashVal = key % 10000
        if self.ls[hashVal] == 0:
            return False
        else:  # It would have a value
            curr = self.ls[hashVal].head
            while curr is not None:
                if curr.data == key:
                    return True
                curr = curr.next
            return False

    # Node -> Node -> Node -> None

    def remove(self, key):
        if self.contains(key) is False:
            return "Error: Key not in set"
        hashVal = key % 10000
        if self.ls[hashVal] == 0:
            return "Error: Nothing to Remove"
        else:  # It would have a value
            curr = self.ls[hashVal].head
            if curr.data == key:
                self.ls[hashVal].head = curr.next
                if self.ls[hashVal].head is None:
                    self.ls[hashVal] = 0
                return
            while curr.next is not None:
                if curr.next.data == key:
                    curr.next = curr.next.next
                    return  # This lets us avoid calling None.next which would lead to an attribute error
                curr = curr.next
        return


# Node -> Node -> Node -> None

#  Curr
# Node -> Our Node -> Node -> None

# Node -> Node -> Our Node -> None

#        C
# 5 -> 10005 -> None
#   ----------->

# I could do add with append, but I'd have to check through the list if the value is in it. Contains and removes is also like this so each operation with a for loop would be O(n)

# NOTE - at most 10000 operations will be done with our class so this isn't too large

# We have to deal with collisions, and we can use the simple way of chaining with linked lists.

# Simple hashing function would be with %
