class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        unsorted_list = s.split(" ")
        index_list = []
        sorted_string = ""

        for i in range(1, len(unsorted_list)+1):
            index_list.append(i)

        for j in index_list:
            for k in unsorted_list:
                if str(j) in k:
                    sorted_string += k.replace(str(j), '')
                    if j != index_list[-1]:
                        sorted_string += " "

        return sorted_string