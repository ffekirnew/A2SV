class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list = []
        for num1 in nums:
            counter = 0
            for num2 in nums:
                if num1 > num2:
                    counter += 1
            list.append(counter)
        return list