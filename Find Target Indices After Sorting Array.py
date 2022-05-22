class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        frequency_of_target = 0
        numbers_less_than_target = 0
            
        for num in nums:
            if num == target:
                frequency_of_target += 1
            elif num < target:
                numbers_less_than_target += 1
        
        index_list = []
        for indes in range((numbers_less_than_target), (numbers_less_than_target + frequency_of_target)):
            index_list.append(index)
        
        return index_list