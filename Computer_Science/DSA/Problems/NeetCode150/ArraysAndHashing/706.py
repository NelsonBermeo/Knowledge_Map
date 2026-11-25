# 706 - Design HashMap (easy)

# Make a hash map class without using any built-in hash table libraries

# Alright lets think about this real quick

# Very similar to hashset, i could handle collisions with a linked list. But I just overwrote here. Nothing crazy


class MyHashMap(object):

    def __init__(self):
        # There will be 10000 entries in our list
        self.ls = [0] * 10000

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # Our hash function will be %
        # A hashmap looks like -> [ ["Nelson", 1] , ["Bradley", 2] ... ]
        # We have to hash our key and then put the value there
        keyHash = key % 10000
        if self.ls[keyHash] == 0:
            self.ls[keyHash] = [key, value]
        else:
            print("Value being overwritten")
            self.ls[keyHash] = [key, value]

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        keyHash = key % 10000
        if self.ls[keyHash] == 0:
            print("There is no value at this key")
        else:
            return self.ls[keyHash][1]

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        keyHash = key % 10000
        if self.ls[keyHash] == 0:
            print("Error: There is no key, value pair for this key")
        else:
            self.ls[keyHash] = 0


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
