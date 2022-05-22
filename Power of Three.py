class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power_list = []
        counter = 0
        while True:
            if 3 ** counter <= n:
                power_list.append(3 ** counter)
                counter += 1
            else:
                break
        
        if n not in power_list:
            return False
        return True
        