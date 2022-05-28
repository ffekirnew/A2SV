def ValidParenthesis(arr):
	class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matching_parentheses = {'(': ')', '{': '}', '[': ']'}
        new_list = []

        for symbol in s:
            if symbol in matching_parentheses.keys(): new_list.append(symbol)

            else:
                if len(new_list) == 0: return False 
                else:
                    previous = new_list.pop()
                    if matching_parentheses[previous] != symbol: return False 

        if len(new_list) == 0: return True


