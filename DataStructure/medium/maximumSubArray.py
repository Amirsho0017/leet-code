class Solution(object):
    def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_n = len(nums)

        if len_n == 1:
            return nums[0]

        sums = [nums[0]]
        max_sum = nums[0]

        for i in range(1, len_n):
            sums.append(max(sums[i - 1] + nums[i], nums[i]))
            max_sum = max(max_sum, sums[i])

        return max_sum

# creating an empty list
nums = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())

    nums.append(ele)  # adding the element

print(Solution.maxSubArray(nums))
