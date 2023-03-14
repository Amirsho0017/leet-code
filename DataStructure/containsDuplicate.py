class Solution(object):
    def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)

nums = '[' + input('Input nums: ') + ']'
print(Solution.containsDuplicate(nums))