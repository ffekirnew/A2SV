class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list = []
        for num in range(1, n + 1):
            if (num % 3 == 0) and (num % 5 == 0):
                list.append("FizzBuzz")
            elif (num % 3 == 0):
                list.append("Fizz")
            elif num % 5 == 0:
                list.append("Buzz")
            else:
                list.append(num)
        
        print(list)