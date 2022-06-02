class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        maximum = None
        nums = [int(i) for i in nums]
        
        for i in range(k):
            maximum = max(nums)
            nums.remove(maximum)
        
        return str(maximum)