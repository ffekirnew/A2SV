class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        index = 0

        for num in nums:
            if num == 0:
                nums.pop(index)
                nums.insert(0,0)
            index += 1

        for num in nums:
            if num == 2:
                nums.remove(num)
                nums.append(2)

        return nums