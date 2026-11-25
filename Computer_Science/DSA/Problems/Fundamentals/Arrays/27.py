# Given an integer array nums and a integer val remove all occurances of val in nums IN PLACE

# [0,1,2,2,3,0,4,2] & 2 ->
# [0,1,3,0,4]

# With python this is as simple as using the .pop, we can try that, shoot, this is O(n^2) because we keep popping so everything needs to shift


def a(nums, val):
    count_val = nums.count(val)
    i = 0
    while i <= len(nums) - count_val:
        if nums[i] == val:
            nums.pop(i)
            i -= 1
        i += 1
    if nums[-1] == val:
        nums.pop(len(nums) - 1)
    return nums


# Gosh this part took me so long and its not even the whole problem.


def b(nums, val):
    # This solution uses a 2 pointer solution with a starting index and then an index that traverses the whole array, we simply overwrite
    # The array with values thats are not val and then return a simple slice this would be O(n)
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return nums[:k]


# Revisit Date: ...


print(b([0, 1, 2, 2, 3, 0, 4, 2], 2))
