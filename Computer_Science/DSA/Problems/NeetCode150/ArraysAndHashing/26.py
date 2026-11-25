def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    remove_len = set(nums)
    dic = {}
    i = 0
    while i < len(remove_len):
        if dic.get(nums[i]) is None:
            dic[nums[i]] = 0
            i += 1
        else:
            # temp = nums[i]
            # how can we move everything over 1 and then throw the temp to the back?
            for j in range(i, len(nums) - 1):
                # swap
                nums[j] = nums[j + 1]
            # nums[-1] = "_"
    return len(dic)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

print(removeDuplicates(nums))
