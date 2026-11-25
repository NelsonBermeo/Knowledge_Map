# Given a binary array nums, return the maximum number of consecutive 1s in the array

# I wonder how this could be optimized to below O(n) but we can just keep a counter and a highest and loop through the list


def a(nums):
    largest = float("-inf")
    current_count = 0
    currently_1 = False
    for i in range(len(nums)):
        if nums[i] == 1:
            currently_1 = True
        if nums[i] == 1 and currently_1 == True:
            current_count += 1
        if nums[i] == 0:
            if current_count > largest:
                largest = current_count
            current_count = 0
            currently_1 = False
    if current_count > largest:
        largest = current_count
    return largest


if __name__ == "__main__":
    print(a([1, 1, 0, 1, 1, 1]))
