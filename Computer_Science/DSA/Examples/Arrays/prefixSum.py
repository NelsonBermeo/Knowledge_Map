nums = [1, 3, -2, 4]
p_sum = [0] * len(nums)
j = 0
val = 0
for i in range(len(nums)):
    val = val + nums[i]
    p_sum[j] = val
    j += 1
print(p_sum)
